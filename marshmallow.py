from marshmallow import Schema, fields

UserSchema = Schema.from_dict(
    {"name": fields.Str(), "email": fields.Email(), "created_at": fields.DateTime()}
)