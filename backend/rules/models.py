from tortoise import models, fields
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator


class Rule(models.Model):
    id = fields.IntField(pk=True)
    image = fields.CharField(max_length=256, null=True)
    description = fields.CharField(max_length=1024, null=True)
    example = fields.CharField(max_length=256, null=True)

    class PydanticMeta:
        allow_cycles = False

RulePydanticModel  = pydantic_model_creator(Rule, name="Rule")
RuleInDBPydanticModel = pydantic_model_creator(Rule, name="RuleIn", exclude_readonly=True)
RulePydanticListModel = pydantic_queryset_creator(Rule)