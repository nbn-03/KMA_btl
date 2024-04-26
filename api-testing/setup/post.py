import requests
import read
def post():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer d76528d3edeb70ab3d775d9f11a4963181b94d9e0ec17d996ed8ddb2d6cb5f22"
    }
    for i in range(1,6):
        res = requests.post("https://gorest.co.in/public/v2/users",json=read.read_file(f"C:\\api-testing\\setup\\c{i}.json"),headers= headers)
        print(res.status_code)
def delete():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer d76528d3edeb70ab3d775d9f11a4963181b94d9e0ec17d996ed8ddb2d6cb5f22"
    }
    res = requests.delete("https://gorest.co.in/public/v2/users/6854750",headers= headers)
    print(res.status_code)

