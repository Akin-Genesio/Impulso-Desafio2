from typing import Union
import time

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    current_time = time.ctime()
    return current_time


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}