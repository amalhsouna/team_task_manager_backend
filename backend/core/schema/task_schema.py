from core import ma


class TaskSchema(ma.SQLAlchemySchema):
    id = ma.Integer(dump_only=True)
    title = ma.String(required=True)
    description = ma.String(required=True)
    #team_id = ma.auto_field()

