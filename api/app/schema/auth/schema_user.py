from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=3, max=100))
    email = fields.Email(required=True, validate=validate.Length(max=200))
    password = fields.Str(required=True, validate=validate.Length(min=6, max=200))
    role_id = fields.Int(required=True)
    gender = fields.Str(validate=validate.OneOf(["male", "female", "other", None]))
    location = fields.Str(validate=validate.Length(max=100))
    birthdate = fields.Date(allow_none=True)
    avatar = fields.Str(allow_none=True)
    signature = fields.Str(missing="这个人很懒，什么都没留下！")
    phone_number = fields.Str(validate=validate.Length(max=20), allow_none=True)
