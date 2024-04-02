import random
def get_header():
    header = { "Content-Type" : "application/json",
               "Authorization" : "Bearer 18661386073d8ec7e241a5395233b5ce5457a4a7acca76f0a37f0ff14e057a7b"}
    return header

def get_email():
    no = random.randint(1000,9999)
    email = f"test_auto_{no}@gmail.com"
    return email