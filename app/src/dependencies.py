from .database import driver

async def get_db():
    async with driver.session(database='rule') as session_:
        yield session_