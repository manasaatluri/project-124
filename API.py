from crypt import methods
from numpy import append
from flask import Flask, jsonify, request



app = Flask(__name__)

m=[
    {
        "name":"vidhushi",
        "age":"13",
        "grade":"9th",
        "height":"149cm"    
    },
    {
        "name":"harsha",
        "age":"14",
        "grade":"9th",
        "height":"172cm"
    }
]



#basic route
@app.route("/")
def hi():
    return "this is the data in my first api link"



@app.route("/data")
def hello():
    return jsonify({
         "name":"navya",
        "age":"15",
        "grade":"9th",
        "height":"169cm"
    })


@app.route("/vmh")
def hola():
    return jsonify({
        "data": m,
        "status":"bff"
    })


@app.route("/bts")
def bonjour():
    h={
        "name":"manasa",
        "age":"14",
        "grade":"9th",
        "height":"162cm"
    }
    m.append(h)
    return jsonify({
        "data2": m,
        "status":"bff"
    })


@app.route("/fl",methods=["POST"])
def annyeong():
    h={
        "name":request.json.get('name', ""),
        "age":request.json.get('age', ""),
        "grade":request.json.get('grade', ""),
        "height":request.json.get('height', "")
    }
    m.append(h)
    return jsonify({
        "data2": m,
        "status":"bff"
    })





if __name__ == "__main__":
    app.run()


