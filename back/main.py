from flask import Flask, request, Response
from flask_cors import CORS
import pandas as pd
from pymongo import MongoClient
import json
from bson import json_util
import time
from waitress import serve

general_data = []

rooms = {
    "home": [],
    "petitBac": [],
    "patateChaude": []
}

lobby = {}

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

""" print(Prenoms.head()["name"])
print(PrenomsGars.head()["name"])
print(PrenomsFilles.head()["name"])
print(Celebrities.head()["name"])
print(FruitsLegumes.head()["name"])
print(Metiers.head()["name"])
print(Pays.head()["name"])
print(Villes.head()["name"]) """

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
    print(user)
    if users.find_one(user):
        users.update_one(user, {"$set": {"online": True}})
        return user
    else:
        return "False"

@app.route('/users/logOff/<login>', methods=['GET'])
def logOff(login):
    user = {"login": login}
    oldRoom = users.find_one(user)["currentRoom"]
    if oldRoom != "None":
        rooms[oldRoom].remove(user["login"])
    infoRooms()
    if users.find_one(user):
        users.update_one(user, {"$set": {"online": False, "currentRoom": "None"}})
        return "OK"
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

@app.route('/sendMessage', methods = ['POST'])
def sendMessage():
    messageSplitted = request.get_json()["message"][:-1].split(",")
    general_data.append("(message;" + messageSplitted[0] + ";" + messageSplitted[1] + ";" + messageSplitted[2] + ")")
    return "Message has been registered"

@app.route('/updateRoom/<name>/<room>', methods = ['GET'])
def updateRoom(name, room):
    oldRoom = users.find_one({"login": name})["currentRoom"]
    print(f"{name} changes from {oldRoom} to {room}")
    if oldRoom != "None":
        rooms[oldRoom].remove(name)
    rooms[room].append(name)    
    users.update_one({"login": name}, {"$set": {"currentRoom": room}})
    infoRooms()
    
    return "Player " + name + " is now in " + room

@app.route('/streamingData')
def generate_data():
    def generate():
        while True:
            time.sleep(2)
            if general_data != []: 
                print(general_data)
            yield "data: "+ str(general_data)[1:-1].replace("'", "").replace(" ", "") + "\n\n"
    return app.response_class(generate(), mimetype='text/event-stream')

@app.route('/getAllOnlinePlayer', methods=['GET'])
def getAllOnlinePlayer():
    onlinePlayer = []
    for player in users.find():
        if player["online"]:
            onlinePlayer.append(player)
    print(onlinePlayer)
    return json.loads(json_util.dumps(onlinePlayer))


def infoRooms():
    print("current rooms:")
    [print(f"{room} : {players}") for room, players in rooms.items()]

def updateRooms():
    for user in users.find():
        if user['currentRoom'] != "None":
                rooms[user['currentRoom']].append(user['login'])

if __name__ == "__main__":
    client = MongoClient("mongodb+srv://admin:Dragon-49@cluster0.thgjuyb.mongodb.net/?retryWrites=true&w=majority")
    db = client.Games
    users = db.users
    
    updateRooms()
    infoRooms()

    serve(app, host="0.0.0.0", port=5000, threads=34)