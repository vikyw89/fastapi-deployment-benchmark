from datetime import timedelta
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import URL
import os
import logging
from prisma import Prisma

prisma = Prisma(
    connect_timeout=timedelta(hours=1),
    http={
        "timeout": 360,
    },
)


logger = logging.getLogger(__name__)
url_object = URL.create(
    "mysql+aiomysql",
    username=os.getenv("RDB_USERNAME", "root"),
    password=os.getenv("RDB_PASSWORD", "password"),
    host=os.getenv("RDB_HOST", "localhost"),
    port=int(os.getenv("RDB_PORT", 3306)),
    database=os.getenv("RDB_DATABASE", "kepler"),
)

engine = create_async_engine(
    url=url_object,
    pool_size=90,  # Increase pool size
    pool_recycle=3600,  # Recycle connections after 1 hour
    pool_timeout=36000,
)

async_session = async_sessionmaker(bind=engine, expire_on_commit=True)
