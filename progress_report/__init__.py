from flask import Flask
app = Flask(__name__, static_folder='../app/public', static_url_path="", template_folder='../app/templates')

# config
import os
app.config.from_object(os.environ['APP_SETTINGS'])


from progress_report import views
