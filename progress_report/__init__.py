from flask import Flask
app = Flask(__name__)

# config
import os
app.config.from_object(os.environ['APP_SETTINGS'])


from progress_report import views
