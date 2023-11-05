# Copyright 2023 Marin Pejcin


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import services, users, login, car


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"]
)


app.include_router(users.router)
app.include_router(login.router)
app.include_router(services.router)
app.include_router(car.router)


@app.get("/")
async def root():
    return {"status": "healthy"}
