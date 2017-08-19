from flask import Flask

app = Flask(__name__)

@app.route("/")
def function():
	pass

@app.route("/log")
def function():
	if "user" in session:
		return "index.html"
	return "log.html"

if __name__ == '__main__':
	app.run(debug=True)