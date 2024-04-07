import json
def get_base_end_point():
    with open("C:\\api-testing\\config\\endpoint.json","r") as json_file:
        properties = json.load(json_file)
        env = properties["environment"]["env"]
        return properties[env]["base_url"]
    
    