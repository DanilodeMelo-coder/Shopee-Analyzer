from fastapi import FastAPI
from app.routers import upload, metricas_gerais

app = FastAPI()

app.include_router(upload.router, prefix="/api/v1")
app.include_router(metricas_gerais.router, prefix="/api/v1")


@app.get("/")
async def home():
    return("Api funcionando")

