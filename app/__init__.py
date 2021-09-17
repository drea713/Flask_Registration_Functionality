from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

# setup database connection
db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)

login_manager = LoginManager(app)

from app import routes, models