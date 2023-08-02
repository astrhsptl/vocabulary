


TORTOSE_CONFIG = {
    "db_url": "sqlite://sqlite.db",
    "modules": {"models": ["rules.models", "words.models"], "aerich.models": ["rules.models", "words.models"]},
    "generate_schemas": True,
    "add_exception_handlers": True,
}