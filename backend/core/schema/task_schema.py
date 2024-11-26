from core import ma
from marshmallow import Schema, fields

class TaskSchema(ma.SQLAlchemySchema):
    id = ma.Integer(dump_only=True)
    title = ma.String(required=True)
    description = ma.String(required=True)

class CreateTaskSchema(Schema):
    title = fields.String(required=True, description="Name of task")
    description = fields.String(required=True, description="Desciption of task")