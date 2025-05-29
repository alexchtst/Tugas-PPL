from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory database
items = []

# Pydantic model
class Item(BaseModel):
    id: int
    name: str
    description: str = None

# Home route
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# Get all items
@app.get("/items/", response_model=List[Item])
def get_items():
    return items

# Get item by ID
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# Add new item
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

# Delete item by ID
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for i, item in enumerate(items):
        if item.id == item_id:
            del items[i]
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")

print("hahaha")