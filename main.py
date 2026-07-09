from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

load_dotenv()

#Inicializacion de Modelos Pydantic SQLAlchemy
import database.models

from routes.products import router as ProductsRouter



app = FastAPI(
    title="Valux API",
    version="1.0.0",
)

app.include_router(ProductsRouter)


@app.get("/")
async def Root():
    return {
        "Name": "Valux API",
        "Status": "Running",
    }


@app.get("/health")
async def Health():
    return {
        "Status": "OK",
    }


app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static",
)