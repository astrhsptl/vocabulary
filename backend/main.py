from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from tortoise.contrib.fastapi import register_tortoise
from db.config import TORTOSE_CONFIG

from settings import MEDIA_URL, MEDIA_DIR
from words.routs import router as word_router
from rules.routes import router as rule_router

app = FastAPI()

app.include_router(word_router)
app.include_router(rule_router)

app.mount(MEDIA_URL, StaticFiles(directory=MEDIA_DIR), name='media')

register_tortoise(
    app,
    **TORTOSE_CONFIG
)
