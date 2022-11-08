from dataclasses import dataclass
import marshmallow
import marshmallow_dataclass


@dataclass
class Query:
    cmd: str
    value: str

    class Meta:
        unknown = marshmallow.EXCLUDE


QuerySchema = marshmallow_dataclass.class_schema(Query)
