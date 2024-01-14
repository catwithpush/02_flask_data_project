from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
import os




app = Flask(__name__)
csrf = CSRFProtect(app)

# Configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expsenseDB.db'


# Load the environment variables
load_dotenv()

# Access the SECRET_KEY using the environment variable
#secret_key = os.getenv("API_KEY")

app.config['SECRET_KEY'] =os.urandom(32)

db = SQLAlchemy(app)

from application import routes
