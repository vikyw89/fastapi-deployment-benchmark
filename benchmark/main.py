import asyncio
import time
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/sync/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    time.sleep(1)
    return {"item_id": item_id, "q": q}


@app.get("/async/{item_id}")
async def aread_item(item_id: int, q: Union[str, None] = None):
    await asyncio.sleep(1)
    return {"item_id": item_id, "q": q}
