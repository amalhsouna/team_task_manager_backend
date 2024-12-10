from core import ma
from marshmallow import Schema, fields
from core.schema.task_schema import TaskSchema


class TeamSchema(ma.SQLAlchemySchema):
    id = ma.Integer(dump_only=True)
    name = ma.String(required=True)
    created_at = ma.Date(required=True)
    tasks = ma.Nested(TaskSchema, many=True)


class CreateTeamSchema(Schema):
    name = fields.String(required=True, description="Name of team")
