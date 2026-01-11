from fastapi import APIRouter
from pymongo import MongoClient
from .models import ReviewCreate, ReviewResponse
from .llm import generate_ai_response

# ✅ router MUST be defined before use
router = APIRouter()

# MongoDB connection (use your existing DB)
client = MongoClient("mongodb://localhost:27017")
db = client["review_db"]
collection = db["reviews"]

@router.post("/reviews", response_model=ReviewResponse)
def create_review(data: ReviewCreate):
    ai_response = generate_ai_response(
        review=data.review,
        rating=data.rating
    )

    document = {
        "name": data.name,
        "email": data.email,
        "rating": data.rating,
        "review": data.review,
        "ai_response": ai_response
    }

    collection.insert_one(document)
    return document
