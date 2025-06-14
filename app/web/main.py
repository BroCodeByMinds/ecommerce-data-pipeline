from fastapi import FastAPI
from app.web.api.routes import router

app = FastAPI(title="E-Commerce Order Stats API")

app.include_router(router)
