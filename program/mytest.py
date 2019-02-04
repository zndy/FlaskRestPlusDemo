import unittest

from program.pojo import ThreeValues
from program.schema import ThreeValuesSchema


class MyTest(unittest.TestCase):

    def test1(self):
        values = ThreeValues(1.0, 2.0, 3.0)
        print("values: " + str(values))
        schema = ThreeValuesSchema()
        json_result = schema.dumps(values)
        print("json Result: " + str(json_result))
