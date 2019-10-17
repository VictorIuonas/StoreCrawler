from marshmallow import Schema, fields


class ProductSchema(Schema):
    id = fields.Integer()
    title = fields.Str()
    price = fields.Integer()
    currency = fields.Str()
    description = fields.Str(allow_none=True, required=False)
