import requests

url = "https://jsonplaceholder.typicode.com/users/5"

try:
    responses = requests.get(
        url,
        timeout = 5
    )

    responses.raise_for_status()
    data = responses.json()

    print(f"이름: ", data["name"])
    print(f"이메일: ", data["email"])
    print(f"도시: ", data["address"]["city"])
    print(f"회사: ", data["company"]["name"])
except requests.exceptions.Timeout:
    print("타임아웃")
