from flask import Flask,request
from flask_restful import Resource, Api
import pickle
import pandas as pd 
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

api = Api(app)

class prediction(Resource):
    def get(self,area):
        print(area)
        area = [int(area)]
        df = pd.DataFrame(area, columns=['area'])
        model = pickle.load(open('model_pickle','rb'))
        prediction = model.predict(df)
        prediction = int(prediction[0])
        return str(prediction)

class getData(Resource):
    def get(self):
        df = pd.read_csv('sample.csv')
        res = df.to_json(orient='records')
        return res

api.add_resource(getData, '/api')

api.add_resource(prediction, '/prediction/<int:area>')

if __name__ == '__main__':
    app.run(host='0.0.0.0')