from core import ma


class TeamSchema(ma.SQLAlchemySchema):
    id = ma.Integer(dump_only=True)
    name = ma.String(required=True)
    #tasks = ma.Nested(TaskSchema, many=True)

