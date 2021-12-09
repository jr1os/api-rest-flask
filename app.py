from flask import Flask, jsonify

app = Flask(__name__)

develops = [{
    "name":"ali",
    "skills":["python", "flask"],
},
{
    "name":"jonathan",
    "skills":["python", "javascript"],
}]


@app.route('/dev/<int:id>/', methods=["GET"])
def develop(id):
    develop = develops[id]
    print(develop)
    return jsonify(develop)