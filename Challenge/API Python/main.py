from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home() :
    return "Hello Anas"



if __name__ == "__main__" :
    app.run(debug=True)

#? Methods can use
# GET => To SELECT
# POST => To INSERT
# PUT => To UPDATE
# DELETE => To DELETE