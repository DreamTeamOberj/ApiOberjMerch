from fastapi import FastAPI
from starlette.responses import RedirectResponse
from server.routes.products import productRouter
from server.routes.users import userRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://oberj-merch-nuxt.vercel.app",
    "http://project.rom1mart.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(productRouter,tags=["Product routes"])
app.include_router(userRouter,tags=["User routes"])


@app.get("/")
async def read_root():
    response = RedirectResponse(url='/docs')
    return response
