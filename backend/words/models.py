from tortoise import models, fields
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator


class Word(models.Model):
    id = fields.IntField(pk=True)
    original = fields.CharField(max_length=124, unique=False)
    translate = fields.CharField(max_length=124)
    description = fields.CharField(max_length=124, null=True)
    example = fields.CharField(max_length=256, null=True)

    class PydanticMeta:
        allow_cycles = False

WordPydanticModel  = pydantic_model_creator(Word, name="Word")
WordInDBPydanticModel = pydantic_model_creator(Word, name="WordIn", exclude_readonly=True)
WordPydanticListModel = pydantic_queryset_creator(Word)

