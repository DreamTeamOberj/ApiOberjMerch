import motor
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from routes.products import products as productRoute
from routes.users import users as usersRoute

MONGO_URL = "mongodb+srv://groupe6:groupe6@bddoberjmerch.t2yjt.mongodb.net/oberjMerch?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client.oberj

student_collection = db.get_collection("oberjMerch")


app = FastAPI()

app.include_router(productRoute,tags=["Products"])
app.include_router(usersRoute,tags=["Users"])


@app.get("/")
async def read_root():
    response = RedirectResponse(url='/docs')
    return response
