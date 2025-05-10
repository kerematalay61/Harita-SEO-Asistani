import random

proxy_list = [
    "http://proxy1.example.com:8000",
    "http://proxy2.example.com:8000",
    "http://proxy3.example.com:8000"
]

def get_random_proxy():
    return random.choice(proxy_list)
