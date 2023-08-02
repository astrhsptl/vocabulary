from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from db.config import TORTOSE_CONFIG

from words.routs import router as word_router

app = FastAPI()

app.include_router(word_router)

register_tortoise(
    app,
    **TORTOSE_CONFIG
)
