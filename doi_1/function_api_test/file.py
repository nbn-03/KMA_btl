import json
def read_file_c():
    with open("C:\\project-api\\config\\CREATE_USER.json","r") as json_file:
        properties = json.load(json_file)
        return properties
    
def read_file_u():
    with open("C:\\project-api\\config\\UPDATE_USER.json","r") as json_file:
        properties = json.load(json_file)
        return properties
    
def update_file_c(data):
    with open("C:\\project-api\\config\\CREATE_USER.json","w") as json_file:
        json_file.truncate(0)
        json_file.seek(0) 
        json.dump(data, json_file, indent=4)
