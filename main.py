from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

App = FastAPI(
    title="Valux API",
    version="1.0.0",
)


@App.get("/")
async def Root():
    return {
        "Name": "Valux API",
        "Status": "Running",
    }


@App.get("/health")
async def Health():
    return {
        "Status": "OK",
    }