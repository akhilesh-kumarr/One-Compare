from pydantic import BaseModel, Field


class PlatformPrice(BaseModel):
    platform: str = Field(..., examples=["Amazon"])
    price: int = Field(..., ge=0, examples=[69999])
    original_price: int = Field(..., ge=0, alias="originalPrice", examples=[79999])
    delivery: str = Field(..., examples=["Free delivery by tomorrow"])
    rating: float = Field(..., ge=0, le=5, examples=[4.5])


class ElectronicsRecommendation(BaseModel):
    label: str = Field(default="Best Deal")
    platform: str
    price: int
    savings: int
    reason: str


class ElectronicsProduct(BaseModel):
    id: str
    name: str
    image_url: str = Field(..., alias="imageUrl")
    specifications: dict[str, str]
    platforms: list[PlatformPrice]
    recommendation: ElectronicsRecommendation | None = None


class ElectronicsSearchResponse(BaseModel):
    query: str
    count: int
    results: list[ElectronicsProduct]
