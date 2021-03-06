from marshmallow import Schema, fields, post_load

from program.pojo import ThreeValues, MyPoint


class ThreeValuesSchema(Schema):
    value1 = fields.Float()
    value2 = fields.Float()
    value3 = fields.Float()

    @post_load
    def make_obj(self, data):
        return ThreeValues(**data)


class MyPointSchema(Schema):
    x = fields.Float()
    y = fields.Float()

    @post_load
    def make_obj(self, data):
        return MyPoint(**data)
