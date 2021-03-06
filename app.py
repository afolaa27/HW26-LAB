from flask import Flask, jsonify, g
from resources.shoes import shoes


import models


DEBUG=True
PORT=8000
app = Flask(__name__)

app.register_blueprint(shoes, url_prefix='/api/v1/shoes')


@app.route('/')
def index():
	return "Server Now runs"

if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)
