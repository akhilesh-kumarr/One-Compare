import json
from pathlib import Path

from fastapi import APIRouter, HTTPException, Query, status

from app.schemas.electronics import ElectronicsProduct, ElectronicsSearchResponse
from app.services.recommendation import get_best_electronics_deal

router = APIRouter(prefix="/electronics", tags=["Electronics"])

DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "electronics.json"


async def load_electronics_data() -> list[dict]:
    """Load mock electronics data from the local JSON file."""

    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def add_recommendation(product: dict) -> dict:
    """Attach a best-deal recommendation to a product response."""

    product_with_recommendation = product.copy()
    product_with_recommendation["recommendation"] = get_best_electronics_deal(
        product.get("platforms", [])
    )
    return product_with_recommendation


@router.get("/search", response_model=ElectronicsSearchResponse)
async def search_electronics(
    q: str = Query(..., min_length=1, description="Product search keyword"),
) -> ElectronicsSearchResponse:
    """Search electronics products by name or specification value."""

    products = await load_electronics_data()
    normalized_query = q.strip().lower()

    matched_products = [
        add_recommendation(product)
        for product in products
        if normalized_query in product["name"].lower()
        or any(
            normalized_query in str(value).lower()
            for value in product.get("specifications", {}).values()
        )
    ]

    return ElectronicsSearchResponse(
        query=q,
        count=len(matched_products),
        results=[ElectronicsProduct.model_validate(product) for product in matched_products],
    )


@router.get("/{product_id}", response_model=ElectronicsProduct)
async def get_electronics_product(product_id: str) -> ElectronicsProduct:
    """Return one electronics product by id."""

    products = await load_electronics_data()

    for product in products:
        if product["id"] == product_id:
            return ElectronicsProduct.model_validate(add_recommendation(product))

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Electronics product with id '{product_id}' was not found.",
    )
