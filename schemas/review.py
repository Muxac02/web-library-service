from pydantic import BaseModel, Field

class ReviewCreate(BaseModel):
    book_id: int = Field(..., example=0)
    rating: int = Field(..., example=5)
    review_text: str = Field(..., example="Lorem epsum")