from fastapi import FastAPI
from starlette.responses import RedirectResponse
from app.server.routes.products import products as productRoute
from app.server.routes.users import users as usersRoute


app = FastAPI()

app.include_router(productRoute)
app.include_router(usersRoute)


@app.get("/")
async def read_root():
    response = RedirectResponse(url='/docs')
    return response
