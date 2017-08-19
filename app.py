from flask import Flask

app = Flask(__name__)

@app.route("/")
def function():
	return "index.html"

@app.route("/login")
def function():
	return "login.html"

@app.route("/logout")
def function():
	return "logout.html"

if __name__ == '__main__':
	app.run(debug=True)