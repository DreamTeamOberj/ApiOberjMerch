from fastapi import FastAPI
from starlette.responses import RedirectResponse
from routes.products import products as productRoute
from routes.users import users as usersRoute

app = FastAPI()

app.include_router(productRoute, tags=["Products"])
app.include_router(usersRoute, tags=["Users"])


@app.get("/")
async def read_root():
    response = RedirectResponse(url='/docs')
    return response
