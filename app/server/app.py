from starlette.responses import RedirectResponse

from server.routes.products import productRouter
from server.routes.users import userRouter
from fastapi.middleware.cors import CORSMiddleware

### GRAPHQL DEPEDENCIES ###

import strawberry

from server.models.schema import Query
from server.models.schema import Mutation
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

#########

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    "https://oberj-merch-nuxt.vercel.app/",
    "http://project.rom1mart.com/"
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


# GRAPHQL

product_schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(product_schema)

app.include_router(graphql_app, prefix="/graphql")
