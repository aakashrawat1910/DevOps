from flask import Flask, request, jsonify

appname = Flask(__name__)
B=2
@appname.route("/")
#this is master change
#this is change in bigfix
#Master 2


def hello():
    return "hello world"

#if __name__ == '__main__':



appname.run(debug=True)

