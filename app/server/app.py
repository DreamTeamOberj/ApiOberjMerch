from fastapi import FastAPI
from starlette.responses import RedirectResponse
from app.server.routes.products import productRouter
from app.server.routes.users import userRouter

app = FastAPI()

app.include_router(productRouter,tags=["Product routes"])
app.include_router(userRouter,tags=["User routes"])


@app.get("/")
async def read_root():
    response = RedirectResponse(url='/docs')
    return response
