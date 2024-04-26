import random
def get_header():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer d76528d3edeb70ab3d775d9f11a4963181b94d9e0ec17d996ed8ddb2d6cb5f22"
    }
    return headers

def get_email():
    no = random.randint(1000,9999)
    email = f"test_auto_{no}@gmail.com"
    return email

def get_header_error1():
    headers = {
        "Content-Type": "application/json"
    }
    return headers

def get_header_error2():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 18661386073d8ec7e241a5395233b5ce5457a4a7acca76f0a37f0ff14e057a7b1"
    }
    return headers