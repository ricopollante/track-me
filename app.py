from flask import Flask, request 
from flask_restful import Resource, Api 
import json
app = Flask(__name__) 
api = Api(app) 

class LocationStore(Resource):
    def post(self): 
        long = request.form['long']
        lat = request.form['lat']
        print(long, lat)
        return {'status': 'ok'} 
api.add_resource(LocationStore, '/') 

if __name__ == '__main__':
    app.run(debug=True)

