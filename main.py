from fastapi import FastAPI
from databases import Database
import sqlalchemy

DATABASE_URL = "postgresql://user:1234@localhost:5432/library"

database = Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(length=100)),
    sqlalchemy.Column("email", sqlalchemy.String(length=100), unique=True),    
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()
    
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/users/")
async def read_users():
    query = users.select()
    return await database.fetch_all(query)

@app.post("/users/")
async def create_user(name: str, email: str):
    query = users.insert().values(name=name,email=email)
    await database.execute(query)
    return {"name": name, "email": email}

@app.delete("/users/")
async def delete_user(id: int):
    query = users.delete().where(users.c.id==id)
    query2 = users.select().where(users.c.id==id)
    result = await database.fetch_one(query2)
    if (result!=None):
        await database.execute(query)
        return {"name": result.name, "email": result.email}
    return {"message": "Nothing to delete"}

@app.put("/users/")
async def update_user(id: int, name: str, email: str):
    query = users.update().where(users.c.id==id).values(name=name, email=email)
    query2 = users.select().where(users.c.id==id)
    result = await database.fetch_one(query2)
    if (result!=None):
        await database.execute(query)
        return {"old info":{"name": result.name, "email": result.email},
                "new info":{"name": name, "email": email}}
    return {"message": "Nothing to update"}