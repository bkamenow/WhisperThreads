from marshmallow import fields

from schemas.base import UserRequestBase


class UserRegisterRequestSchema(UserRequestBase):
    username = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.String(required=True)
    password = fields.String(required=True, min_length=8, max_length=55)


class UserLoginRequestSchema(UserRequestBase):
    pass