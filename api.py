import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/helloworld', methods=['GET'])
def home():
    return ("hello world", 200)

app.run()