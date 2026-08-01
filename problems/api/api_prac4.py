import requests

url = "https://jsonplaceholder.typicode.com/users/8"

try:
    headers = {
        "Accept": "application/json",
        "User-Agent": "Python-API-Practice"
    }

    response = requests.get(
        headers=headers,
        url=url
        timeout=5
    )

    response.raise_for_status()
    data = response.json()

    print(f"User-Agent: {response.request.headers['User-Agent']}")
    print(f"이름: {data['name']}")
    print(f"이메일: {data['email']}")
    print(f"웹사이트: {data['website']}")
except requests.exceptions.Timeout:
    print("요청 시간 초과")

except requests.exceptions.HTTPError as err:
    print(f"HTTP 에러: {err}")

except requests.exceptions.RequestException as err:
    print(f"Req 에러: {err}")