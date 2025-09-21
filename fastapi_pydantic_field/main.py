from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class BookSchema(BaseModel):
    title: str = Field(..., example="The Great Gatsby", description="The title of the book")
    category: str = Field(..., example="Fiction", description="The category of the book")
    publish_year: int = Field(default=None, example=1925, description="The year the book was published")
    price: float = Field(..., example=10.99, description="The price of the book: 0 < price <= 1000", gt=0, le=1000)
    
@app.post("/books/", response_model=BookSchema)
async def create_book(book: BookSchema):
    return book