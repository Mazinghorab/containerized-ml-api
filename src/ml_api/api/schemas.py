from pydantic import BaseModel, Field

class PredictInput(BaseModel):
  distance_km: float = Field(..., gt=0)
  passengers: int = Field(1, ge=1, le=8)

class PredictResponse(BaseModel):
  duration_min: float
