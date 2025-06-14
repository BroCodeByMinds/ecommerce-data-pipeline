from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="E-Commerce Order Stats API")

# Register route module
app.include_router(router)
