from flask import Flask, request, jsonify

appname = Flask(__name__)

@appname.route("/")


def hello():
    return "hello world"

if __name__ == '__main__':



appname.run(debug=True)

