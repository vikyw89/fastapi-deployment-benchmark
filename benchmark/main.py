import asyncio
import json
import time
from typing import Union
from contextlib import asynccontextmanager
from fastapi import FastAPI
from benchmark.dependencies.db import async_session, engine, prisma
from sqlalchemy import text
import logging

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await prisma.connect()
    yield
    await engine.dispose()
    await prisma.disconnect()

app = FastAPI(lifespan=lifespan)


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

@app.get("/sqlalchemy_aiomysql")
async def aiomysql():

    async with async_session() as session:
        result = await session.execute(statement=text("SHOW TABLES;"))
        parsed_result = result.all()

    return json.dumps(parsed_result,default=str)

@app.get("/prisma_mysql")
async def get_prisma():
    result = await prisma.query_raw(query="SELECT name FROM sqlite_master WHERE type='table';")

    return json.dumps(result)