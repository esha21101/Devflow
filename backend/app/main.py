from fastapi import FastAPI

from app.api.v1.router import api_router

app = FastAPI(
    title="DevFlow AI",
    version="0.1.0",
)

app.include_router(api_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to DevFlow AI"
    }