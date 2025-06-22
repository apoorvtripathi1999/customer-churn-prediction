from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Hello":"World"}

@app.get("/items/{items_id}")
def get_items(items_id:int, q: Union[str,None] = None):
    return {"Item ID": items_id, "Q": q}
