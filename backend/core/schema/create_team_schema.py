from marshmallow import Schema, fields

class CreateTeamSchema(Schema):
    name = fields.String(required=True, description="name of equipe")
    description = fields.String(required=False, description="Description of tema")
