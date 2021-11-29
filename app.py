from flask import Flask
from flask_cors import CORS
from routes.roadsign_bp import roadsign_bp


app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(roadsign_bp, url_prefix='/')
app.register_blueprint(roadsign_bp, url_prefix="/predict")

if __name__ == "__main__":
  "Main method of Flask application"
  app.run()