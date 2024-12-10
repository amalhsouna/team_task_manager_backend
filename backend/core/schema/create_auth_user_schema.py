from marshmallow import Schema, fields


class CreateAuthUserSchema(Schema):
    username = fields.String(required=True, description="Username of the user")
    password = fields.String(required=True, description="Password of the user")
