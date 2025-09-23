from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Category(BaseModel):
    category_id: int
    category_name: str
    
class Item(BaseModel):
    item_id: int
    item_name: str
    category_id: int
    
@app.get("/categories/", response_model=dict)
async def read_categories():
    return {"message": "List of categories", "categories": []}
  
@app.post("/categories/", response_model=dict)
async def create_category(category: Category):
    return {"message": "Category created", "category": category}

@app.put("/categories/{category_id}", response_model=dict)
async def update_category(category_id: int, category: Category):
    return {"message": "Category updated", 
            "category_id": category_id, "category": category}
    
@app.delete("/categories/{category_id}", response_model=dict)
async def delete_category(category_id: int):
    return {"message": "Category deleted", "category_id": category_id}



@app.get("/items/", response_model=dict)
async def read_items():
    return {"message": "List of items", "items": []}

@app.post("/items/", response_model=dict)
async def create_item(item: Item):
    return {"message": "Item created", "item": item}

@app.put("/items/{item_id}", response_model=dict)
async def update_item(item_id: int, item: Item):
    return {"message": "Item updated", "item_id": item_id, "item": item}

@app.delete("/items/{item_id}", response_model=dict)
async def delete_item(item_id: int):
    return {"message": "Item deleted", "item_id": item_id}