from flask import Flask

app = Flask(__name__)

@app.route('/mattareddy1')
def mattareddy1():
	return 'This is mattareddy app----syamala mattareddy'

if __name__ == "__main__":
	app.run(debug=True)