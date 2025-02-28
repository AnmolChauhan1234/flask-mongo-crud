from flask import Flask
from flask_bcrypt import Bcrypt
from flask_restful import Api
from dotenv import load_dotenv
import os
from app.routes import initialize_routes
from app.config import MONGO_URI


load_dotenv()

app = Flask(__name__)
bcrypt = Bcrypt(app)

api = Api(app)


initialize_routes(api)
