from fastapi import APIRouter
from schemas.item import Item

router = APIRouter()

@router.get("/items/", response_model=dict)
async def read_items():
    return {"message": "List of items", "items": []}

@router.post("/items/", response_model=dict)
async def create_item(item: Item):
    return {"message": "Item created", "item": item}

@router.put("/items/{item_id}", response_model=dict)
async def update_item(item_id: int, item: Item):
    return {"message": "Item updated", "item_id": item_id, "item": item}

@router.delete("/items/{item_id}", response_model=dict)
async def delete_item(item_id: int):
    return {"message": "Item deleted", "item_id": item_id}