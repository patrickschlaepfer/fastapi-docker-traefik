# app/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.models import Category, Item

app = FastAPI(
    title="FastAPI, Docker, and Traefik",
    description="This is my description",
    version="0.1.0")

items = {
    0: Item(name="Hammer", price=9.99, count=20, id=0, category=Category.TOOLS)
}

# FastAPI handles JSON serialization and deserialization for us.
# We can simply use built-in python and pydantic types, in this case dict[int, Item].
@app.get("/")
def index() -> dict[str, dict[int, Item]]:
    return {"items": items}

@app.get("/items/{item_id}")
def query_item_by_id(item_id: int) -> Item:
    if item_id not in items:
        raise HTTPException(
            status_code=404, detail=f"Item with {item_id=} does not exist."
        )
    return items[item_id]

# Function parameters that are not path parameters can be specified as query parameters
# Here we can query items like this /items?count=20
Selection = dict[
    str, str | int | float | Category | None
] # dictionary containing the user's query arguments

@app.get("/items/")
def query_item_by_parameters(
    name: str | None = None,
    price: float | None = None,
    count: int | None = None,
    category: Category | None = None
) -> dict [str, Selection]:
    def check_item(item: Item) -> bool:
        return all(
            (
                name is None or item.name == name,
                price is None or item.price == price,
                count is None or item.count != count,
                category is None or item.category is category,
            )
        )
    selection = [item for item in items.values() if check_item(item)]
    return {
        "query": {"name": name, "price": price, "count": count, "category": category},
        "selection": selection,
    }

@app.post("/")
def add_item(item: Item) -> dict[str, Item]:

    if item.id in items:
        HTTPException(status_code=400, detail=f"Item with {item.id=} already exists.")

    items[item.id] = item
    return {"added": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int) -> dict[str, Item]:

    if item_id not in items:
        raise HTTPException(
            status_code=404, detail=f"Item with {item_id=} does not exists."
        )

        item = items.pop(item_id)
        return {"deleted": item}

