import json
from pathlib import Path

from fastapi import APIRouter, HTTPException, Query, status

from app.schemas.cabs import CabEstimateResponse
from app.services.recommendation import get_best_cab_deal

router = APIRouter(prefix="/cabs", tags=["Cabs"])

DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "cabs.json"


async def load_cab_data() -> list[dict]:
    """Load mock cab route data from the local JSON file."""

    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def normalize_location(value: str) -> str:
    """Normalize location text for flexible matching."""

    return " ".join(value.strip().lower().split())


@router.get("/estimate", response_model=CabEstimateResponse)
async def estimate_cab_fare(
    pickup: str = Query(..., min_length=2, description="Pickup location in Bangalore"),
    drop: str = Query(..., min_length=2, description="Drop location in Bangalore"),
) -> CabEstimateResponse:
    """Return mock cab fare estimates for a Bangalore route."""

    routes = await load_cab_data()
    pickup_key = normalize_location(pickup)
    drop_key = normalize_location(drop)

    for route in routes:
        if (
            normalize_location(route["pickup"]) == pickup_key
            and normalize_location(route["drop"]) == drop_key
        ):
            response = route.copy()
            response["recommendation"] = get_best_cab_deal(route.get("estimates", []))
            return CabEstimateResponse.model_validate(response)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=(
            "No mock cab estimate found for this route. Try routes like "
            "'Indiranagar' to 'Koramangala' or 'Whitefield' to 'MG Road'."
        ),
    )
