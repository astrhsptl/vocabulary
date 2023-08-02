from typing import List
from fastapi import APIRouter, HTTPException

from .models import Word as WordModel, WordInDBPydanticModel, WordPydanticModel
from .schemas import WordtUpdateSchema
from utils.rout_templates import (
    get_record_by_id, get_serialized_list,
    create_and_return_created_record, update_data, delete_record
)

router = APIRouter(
    prefix="/words",
    tags=["words"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{id}", response_model=WordPydanticModel)
async def get_word_list(id: int):
    return await get_record_by_id(id=id, pydantic_model=WordPydanticModel, model=WordModel)

@router.get("/", response_model=List[WordPydanticModel])
async def word_list(offset: int =  0, limit: int = 10):
    return await get_serialized_list(pydantic_model=WordPydanticModel, model=WordModel, offset=offset, limit=limit)

@router.post('/', response_model=WordPydanticModel)
async def create_word(word: WordInDBPydanticModel):
    word = await create_and_return_created_record(post_data=word, pydantic_model=WordPydanticModel, model=WordModel)
    return dict(word)


@router.patch("/{id}", response_model=WordPydanticModel,)
async def update_user(id: int, word: WordtUpdateSchema):
    return await update_data(id=id, patch_data=word, pydantic_model=WordPydanticModel, model=WordModel)


@router.delete("/{id}")
async def delete_user(id: int):
    return await delete_record(id=id, pydantic_model=WordPydanticModel, model=WordModel)
