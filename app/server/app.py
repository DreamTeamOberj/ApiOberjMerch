from fastapi import FastAPI
from starlette.responses import RedirectResponse
from server.routes.products import products as productRoute
from server.routes.users import users as usersRoute


app = FastAPI()

app.include_router(productRoute,tags=["Products"])
app.include_router(usersRoute,tags=["Users"])


@app.get("/")
async def read_root():
    response = RedirectResponse(url='/docs')
    return response
