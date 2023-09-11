from flask import Flask, request
from flask_cors import CORS
import pandas as pd
from pymongo import MongoClient
import json
from bson import json_util

client = MongoClient()
client = MongoClient("mongodb+srv://admin:Dragon-49@cluster0.thgjuyb.mongodb.net/?retryWrites=true&w=majority")
db = client.Games
users = db.users


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

Prenoms = pd.read_csv("./data/Prenoms.csv", encoding="latin1", delimiter=",")
PrenomsGars = Prenoms[(Prenoms.genre == "m") | (Prenoms.genre == "m,f")]
PrenomsFilles = Prenoms[(Prenoms.genre == "f") | (Prenoms.genre == "m,f")]
Celebrities = pd.read_csv("./data/Celebrities.csv", encoding="latin1", delimiter=",")
FruitsLegumes = pd.read_csv("./data/FruitsLégumes.csv", encoding="latin1", delimiter=";")
Metiers = pd.read_csv("./data/Métiers.csv", encoding="latin1", delimiter=",")
Pays = pd.read_csv("./data/Pays.csv", encoding="latin1", delimiter=",")
Villes = pd.read_csv("./data/Villes.csv", encoding="latin1", delimiter=",")

print(Prenoms.head()["name"])
print(PrenomsGars.head()["name"])
print(PrenomsFilles.head()["name"])
print(Celebrities.head()["name"])
print(FruitsLegumes.head()["name"])
print(Metiers.head()["name"])
print(Pays.head()["name"])
print(Villes.head()["name"])

categories = {
    "Garcon": PrenomsGars,
    "Fille": PrenomsFilles,
    "Celebrities": Celebrities,
    "FruitsLegumes": FruitsLegumes,
    "Pays": Pays,
    "Villes": Villes,
    "Metiers": Metiers,
}

@app.route('/registration', methods=['POST'])
def registration():
    user = request.get_json()
    user["online"] = True
    users.insert_one(user)
    return 'OK'

@app.route('/login', methods=['POST'])
def login():
    user = request.get_json()
    if users.find_one(user):
        return "True"
    else:
        return "False"

@app.route('/sendAnswer', methods=['POST'])
def sendAnswer():
    checkAnswer = {}
    answer = request.get_json()
    print(answer)
    for cat in answer:
        if cat != "PaysVilles":
            print(cat)
            print(answer[cat])
            checkAnswer[cat] = answer[cat] in categories[cat]["name"].values
        else:
            checkAnswer[cat] = (answer[cat] in categories["Pays"]["name"].values) or (answer[cat] in categories["Villes"]["name"].values)    
    print(checkAnswer)
    return checkAnswer

@app.route('/getAllOnlinePlayer', methods=['GET'])
def getAllOnlinePlayer():
    onlinePlayer = []
    for player in users.find():
        if player["online"]:
            onlinePlayer.append(player)
    print(onlinePlayer)
    return json.loads(json_util.dumps(onlinePlayer))


if __name__ == '__main__':
    app.run(host="0.0.0.0")
