from flask import Flask 


app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    #run other code here
    return "Hello World, this is Flask"

@app.route("/abc", methods=['GET'])
def abc():
    #run other code here
    return "ABC"

