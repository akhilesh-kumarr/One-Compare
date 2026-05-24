import os

os.environ["TESTING"] = "true"

import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app
from app.models.schemas import RecommendationRequest
from app.services.recommendation_service import RecommendationService


@pytest.mark.asyncio
async def test_health_check():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


@pytest.mark.asyncio
async def test_recommendation_prefers_balanced_best_deal():
    payload = RecommendationRequest(
        options=[
            {
                "id": "cheap-low-rating",
                "title": "Budget Earbuds",
                "platform": "Shop A",
                "price": 899,
                "rating": 3.2,
                "delivery_time": 5,
            },
            {
                "id": "balanced",
                "title": "Reliable Earbuds",
                "platform": "Shop B",
                "price": 999,
                "rating": 4.7,
                "delivery_time": 1,
            },
        ],
        preferences={"price_weight": 0.35, "rating_weight": 0.40, "speed_weight": 0.25},
    )

    response = await RecommendationService().recommend(payload)

    assert response.best_deal_id == "balanced"
    assert response.used_ai is False
    assert response.ranked_options[0]["score"] >= response.ranked_options[1]["score"]

