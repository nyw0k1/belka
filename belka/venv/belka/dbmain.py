# импорты #######################################################
import asyncio                                                 ##
import sqlite3 as sq                                           ##
from sqlalchemy import BigInteger, Integer, select             ##
from sqlalchemy.orm import DeclarativeBase, Mapped             ##
from sqlalchemy.orm import mapped_column                       ##
from sqlalchemy.ext.asyncio import AsyncAttrs                  ##
from sqlalchemy.ext.asyncio import create_async_engine         ##
from sqlalchemy.ext.asyncio import async_sessionmaker          ##
#################################################################


engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')
async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    rep = mapped_column(Integer)


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)





##########################################################################    HANDLERS    ########################################################################

#async def sync_user(tg_id):
#    async with async_session() as session:
#        user = await session.scalar(select(User).where(User.tg_id == tg_id))
#
#        if not user:
#            session.add(User(tg_id=tg_id))
#            await session.commit()

#async def get_rep(item_id):
 #  async with async_session() as session:
 #       return await session.scalar(select(Item).where(Item.id == item_id))