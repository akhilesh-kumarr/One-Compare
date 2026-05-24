from pydantic import BaseModel, Field


class CabProviderEstimate(BaseModel):
    provider: str = Field(..., examples=["Uber"])
    cab_type: str = Field(..., alias="cabType", examples=["Sedan"])
    fare: int = Field(..., ge=0, examples=[420])
    eta_minutes: int = Field(..., ge=0, alias="etaMinutes", examples=[6])
    travel_time_minutes: int = Field(..., ge=0, alias="travelTimeMinutes", examples=[34])
    availability: str = Field(..., examples=["Available"])
    rating: float = Field(..., ge=0, le=5, examples=[4.4])


class CabRecommendation(BaseModel):
    label: str = Field(default="Best Deal")
    provider: str
    cab_type: str = Field(..., alias="cabType")
    fare: int
    reason: str


class CabEstimateResponse(BaseModel):
    pickup: str
    drop: str
    distance_km: float = Field(..., alias="distanceKm")
    estimates: list[CabProviderEstimate]
    recommendation: CabRecommendation | None = None
