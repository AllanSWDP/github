from flask import flask

app = flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

# app.run(port=5008,debug=True)