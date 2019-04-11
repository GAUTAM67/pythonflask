from flask import Flask, jsonify, make_response, render_template
import json

app = Flask(__name__,
            template_folder='templates', static_folder="static")


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/universe")
def universe():
    return "Hello Universe!"


@app.route("/json")
def json1():
    return jsonify({"hello": "hello world"})


@app.route("/json2")
def json2():
    json_string = json.dumps({"hello": "hello world"})
    response = make_response(json_string)
    # response.headers["Content-type"] = "application/json"
    response.headers["Content-type"] = "application/json; charset=utf-8"
    return response


@app.route("/json3")
def json3():
    return render_template('app-html.html', name="manish")


app.run(
    debug=True,
    host="0.0.0.0",
    port=3000, threaded=True
)
