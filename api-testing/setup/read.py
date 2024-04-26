import json
def read_file(path):
    with open(path,"r") as json_file:
        properties = json.load(json_file)
        return properties