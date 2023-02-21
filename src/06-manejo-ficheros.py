## ficheros ##
import json

files = open("src/file.txt", "r+") ## leer y escribir

print(files.read())
# print(files.write("cada dia aprendo algo nuevo y no vot a dejar de aprender"))


with open("data.json") as f:
    result = json.load(f)
    print(result)

json_string = '{"name": "ryan", "age": "20", "address": {"mnz": "sass"}}'
data = json.loads(json_string)

with open('data.json', 'w') as read:
    json.dump(data, read)

json_string = json.dumps(data, indent=4)    