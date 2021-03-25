from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

# Initializing application
app = Flask(__name__,instance_relative_config = True)

app.config.from_object(DevConfig)
#app.config.from_pyfile('config.py')

boostrap=Boostrap(app)
from app import views