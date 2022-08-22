from typing import Optional, Union

from fastapi import FastAPI, Header

from pydantic import BaseModel

class Item(BaseModel):
    id: int
    descricao: str
    valor: float

app = FastAPI()


@app.get("/")
def read_root(user_agent: Optional [str] = Header(None)):
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/item")
def add_item(novo_item: Item):
    return novo_item    