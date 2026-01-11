from pydantic import BaseModel, EmailStr, Field

class ReviewCreate(BaseModel):
    name: str
    email: EmailStr
    rating: int = Field(..., ge=1, le=5)
    review: str

class ReviewResponse(BaseModel):
    name: str
    email: EmailStr
    rating: int
    review: str
    ai_response: str
