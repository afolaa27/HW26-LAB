from flask import Flask, jsonify, g

DEBUG=True
PORT=8000
app = Flask(__name__)




@app.route('/')
def index():
	return "Server Now runs"

if __name__ == '__main__':

	app.run(debug=DEBUG, port=PORT)
