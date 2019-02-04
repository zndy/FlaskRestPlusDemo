from flask import Flask, request
from flask_restplus import Resource, Api

from program.schema import ThreeValuesSchema

app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


@api.route('/three')
class user(Resource):
    def post(selfself):
        json_data = request.json
        schema = ThreeValuesSchema()
        result = schema.load(json_data)
        print("result': " + str(result))

        json_result = schema.dumps(result.data)
        print(json_result)
        return json_result


if __name__ == '__main__':
    app.run(debug=True)
