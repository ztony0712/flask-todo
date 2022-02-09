# this is the file for app init

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect



# app init
app = Flask(__name__, template_folder='templates')

# database configuation
app.config.from_object('config')
db = SQLAlchemy(app)

# database migration
Migrate(app, db)

csrf = CSRFProtect()
csrf.init_app(app)

from app import views, model
# export FLASK_APP="__init__"
