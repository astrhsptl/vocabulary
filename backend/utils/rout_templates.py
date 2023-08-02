from typing import List
from tortoise.models import Model
from fastapi import HTTPException
from tortoise.contrib.pydantic.base import PydanticModel

async def get_record_by_id(id: int, pydantic_model: PydanticModel, model: Model) -> PydanticModel:
    return await pydantic_model.from_queryset_single(model.get(id=id))


async def get_serialized_list(pydantic_model: PydanticModel, model: Model, offset: int = 0, limit: int = 10) -> List[PydanticModel]:
    return await pydantic_model.from_queryset(model.all().offset(offset).limit(limit))


async def create_and_return_created_record(post_data: PydanticModel, pydantic_model: PydanticModel, model: Model) -> dict:
    current_word = await model.create(**post_data.dict())
    return await pydantic_model.from_tortoise_orm(current_word)


async def update_data(id: int, patch_data: PydanticModel, pydantic_model: PydanticModel, model: Model) -> PydanticModel:
    await model.filter(id=id).update(**patch_data.dict(exclude_unset=True))
    return await pydantic_model.from_queryset_single(model.get(id=id))



async def delete_record(id: int, pydantic_model: PydanticModel, model: Model) -> HTTPException | dict:
    deleted_count = await model.get(id=id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User {id} not found")
    return { "detail": "successfule deleted" }
