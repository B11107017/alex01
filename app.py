from flask import Flask, request, render_template
import json
import request

app = Flask(__name__)
@app.route('/<name>')
def hello(name):
    return "Hello, " + name + ", How are you!"
if __name__=="__main__"
    app.run()