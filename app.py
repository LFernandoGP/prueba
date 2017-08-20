from flask import Flask

app = Flask(__name__)

@app.route("/")
def function():
	pass

@app.route("/log")
def function():
	return "log.html"

if __name__ == '__main__':
	app.run(debug=False)