from flask import Flask
from flask_mongoalchemy import MongoAlchemy

# To establish connection with database

app = Flask(__name__, template_folder='templates')
app.config['MONGOALCHEMY_DATABASE'] = 'test'
app.config['MONGOALCHEMY_SERVER'] = 'localhost'
app.config['MONGOALCHEMY_PORT'] = '27017'
db = MongoAlchemy(app)
