from fastapi import FastAPI
from starlette.responses import RedirectResponse
from routes.products import productRouter
from routes.users import userRouter

app = FastAPI()

app.include_router(productRouter)
app.include_router(userRouter)


@app.get("/")
async def read_root():
    response = RedirectResponse(url='/docs')
    return response
