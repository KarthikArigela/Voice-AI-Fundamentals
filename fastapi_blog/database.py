from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from config import settings

if "sqlite" in settings.database_url:
    connect_args = {"check_same_thread": False}
else:
    connect_args = {"statement_cache_size": 0}

engine = create_async_engine(
    settings.database_url,
    connect_args=connect_args,
)

AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session