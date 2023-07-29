# Copyright 2023 Marin Pejcin


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


api = FastAPI()

origins = ["*"]

api.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"]
)


@api.get("/")
async def root():
    return {"status": "working"}
