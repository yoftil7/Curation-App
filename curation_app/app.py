from flask import Flask
from flask_pymongo import PyMongo
from flask_restx import Api


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://curating_user:curating_password@127.0.0.1:27017/curating_db"
mongo = PyMongo(app)
api = Api(app, version='1.0', title='Curating API', description='Curating API')

from routes.items import api as items_namespace
api.add_namespace(items_namespace)

if __name__ == "__main__":
    app.run(debug=True)



