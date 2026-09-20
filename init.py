from flask import Flask
import config


app = Flask(__name__)
app.secret_key = config.secret_key
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024


