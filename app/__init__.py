from flask import Flask

def create_app():
	app = Flask(__name__)

	@app.get("/")
	def index():
		return "Hello World!"

	return app
