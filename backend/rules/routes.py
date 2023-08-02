from fastapi import APIRouter, HTTPException

from .models import (
    Rule as RuleModel, RuleInDBPydanticModel, RulePydanticModel)
from .schemas import RuleUpdateSchema

router = APIRouter()


@router.get("/{id}", response_model=RulePydanticModel)
async def get_rule_list(id: int):
    return await RulePydanticModel.from_queryset_single(RuleModel.get(id=id))

@router.get("/", response_model=[RulePydanticModel])
async def rule_list():
    return await RulePydanticModel.from_queryset(RuleModel.all())

@router.post('/', response_model=RulePydanticModel)
async def create_rule(rule: RuleInDBPydanticModel):
    current_rule = await RuleModel.create(**rule.dict())
    rule_schema = await RulePydanticModel.from_tortoise_orm(current_rule)
    return dict(rule_schema)


@router.patch("/{id}", response_model=RulePydanticModel,)
async def update_user(id: int, rule: RuleUpdateSchema):
    await RuleModel.get(id=id).update(**rule.dict(exclude_unset=True))
    return await RulePydanticModel.from_queryset_single(RuleModel.get(id=id))


@router.delete("/{id}")
async def delete_user(id: int):
    deleted_count = await RuleModel.get(id=id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User {id} not found")
    return { "detail": "successfule deleted" }
