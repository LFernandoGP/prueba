from flask import Flask

app = Flask(__name__)

@app.route("/")
def function():
	pass

@app.route("/<name>")
def function():
	pass

@app.route("/log")
def function():
	return "log.html"

@app.route("/logout")
def logout():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=False)