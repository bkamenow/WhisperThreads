from marshmallow import Schema, fields


class UserRequestBase(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)


class UserResponseBase(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    email = fields.Email(required=True)