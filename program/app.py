from flask import Flask, request
from flask_restplus import Resource, Api

from program.pojo import MyPoint
from program.schema import ThreeValuesSchema, MyPointSchema

app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


@api.route('/three')
class Test1(Resource):
    def post(self):
        json_data = request.json
        schema = ThreeValuesSchema()
        result = schema.load(json_data).data
        print("result': " + str(result))

        json_result = schema.dumps(result)
        print(json_result)
        return json_result

@api.route('/three2')
class Test2(Resource):
    def post(self):
        json_data = request.json
        schema = ThreeValuesSchema()
        threeValues = schema.load(json_data).data

        point1 = MyPoint(threeValues.value1,threeValues.value2)
        point2 = MyPoint(threeValues.value1/2,threeValues.value2/2)
        point3 = MyPoint(threeValues.value1/3,threeValues.value2/3)
        point4 = MyPoint(threeValues.value1/4,threeValues.value2/4)
        points = [point1,point2,point3,point4]
        pointSchema = MyPointSchema()
        json_result = pointSchema.dumps(points, many=True)
        return json_result

if __name__ == '__main__':
    app.run(debug=True)
