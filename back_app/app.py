from flask import Flask
from flask_restplus import Api
from flask_mongoengine import MongoEngine
from routes.test_routes import test_routes
from routes.data_routes import data_routes
from flask_cors import CORS

config = {'MONGODB_SETTINGS': {
    'db': 'dev',
    'host': 'localhost',
    'port': 27017,
    'username': 'admin',
    'password': 'admin',
    'authentication_source': 'admin'}}


##BASE DE DATOS DE ATLAS
#DEFAULT_CONFIG = {
#    "database": {
#        "user": "admin",
#        "pwd": "admin",
#        "clusterName": "cluster0",
#        "database": "test",
#    }
#}

#ATLAS_URI = "mongodb+srv://{user}:{pwd}@{clusterName}.ytibs.mongodb.net/{database}?retryWrites=true&w=majority"
#DB_URI = ATLAS_URI.format(**DEFAULT_CONFIG["database"])
##############################################################


app = Flask(__name__)
CORS(app)
#app.config["MONGODB_HOST"] = DB_URI #BD ATLAS
app.config.update(config)
db = MongoEngine(app=app)
api = Api(app=app)


test = api.namespace('test', description='Test APIs')
data = api.namespace('data', description='Data APIs')

test_routes(api=test)
data_routes(api=data)
if __name__ == '__main__':
    app.run()
