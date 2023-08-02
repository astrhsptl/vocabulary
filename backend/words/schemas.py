from tortoise.contrib.pydantic.base import PydanticModel

class WordtUpdateSchema(PydanticModel):
    original: str | None
    translate: str | None
    description: str | None
    example: str | None

    class Config:
        orm_mode = True