from flask import Flask
app = Flask(__name__)

# config
import os
app.config.from_object(os.environ['APP_SETTINGS'])

# database
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
db.init_app(app)


import views


if __name__ == '__main__':
    app.run()
