import aiofiles
from typing import Annotated, List
from time import time
from os.path import join
from fastapi import APIRouter, HTTPException, UploadFile, File, Form, Depends

from settings import MEDIA_ROOT
from .models import (
    Rule as RuleModel, RuleInDBPydanticModel, RulePydanticModel)
from .schemas import RuleUpdateSchema
from utils.utils import image_preprocessing
from utils.rout_templates import (
    get_record_by_id, get_serialized_list,
    create_and_return_created_record, update_data, delete_record
)

router = APIRouter(
    prefix="/rules",
    tags=["rules"],
    responses={404: {"description": "Not found"}},
)

async def create_parameters(
        description: str =  Form(),
        example: str | None = Form(None),
        image: UploadFile | None = File(None),):
    return { 
        "description": description, 
        "example": example,
        "image": image,   
        }

async def update_create_parameters(
        description: str | None =  Form(None),
        example: str | None = Form(None),
        image: UploadFile | None = File(None),):
    return { 
        "description": description, 
        "example": example,
        "image": image,   
        }

@router.get("/{id}", response_model=RulePydanticModel)
async def get_rule_by_id(id: int):
    return await get_record_by_id(id=id, pydantic_model=RulePydanticModel, model=RuleModel)

@router.get("/", response_model=List[RulePydanticModel])
async def rule_list(offset: int =  0, limit: int = 10):
    return await get_serialized_list(pydantic_model=RulePydanticModel, model=RuleModel, offset=offset, limit=limit)

@router.post("/", )
async def post_endpoint(commons: Annotated[dict, Depends(create_parameters)]):
    commons = await image_preprocessing(commons=commons)
    current_rule = await RuleModel.create(**commons)
    return await RulePydanticModel.from_tortoise_orm(current_rule)

@router.patch("/{id}", response_model=RulePydanticModel,)
async def update_user(id: int, commons: Annotated[dict, Depends(update_create_parameters)]):
    commons = await image_preprocessing(commons=commons)
    await RuleModel.get(id=id).update(**RuleUpdateSchema(**commons).dict(exclude_unset=True, exclude_none=True))
    return await RulePydanticModel.from_queryset_single(RuleModel.get(id=id))


@router.delete("/{id}")
async def delete_user(id: int):
    return await delete_record(id=id, pydantic_model=RulePydanticModel, model=RuleModel)