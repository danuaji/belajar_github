import json

file_json = open("tesjson.json")

data = json.loads(file_json.read())

print(data(users.get['firstName']))