from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import scraping

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return scraping.getData('TesteApi', 'main')