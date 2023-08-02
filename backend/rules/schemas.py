from tortoise.contrib.pydantic.base import PydanticModel

class RuleUpdateSchema(PydanticModel):
    image: str | None
    description: str | None
    example: str | None

    class Config:
        orm_mode = True