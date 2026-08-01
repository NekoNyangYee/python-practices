import requests

url = "https://jsonplaceholder.typicode.com/posts/10"

try:
    payload = {
        "title": "PATCH 요청 연습 완료"
    }

    response = requests.patch(
        url=url,
        json=payload,
        timeout=5
    )

    response.raise_for_status()
    data = response.json()

    print(f"ID: {data['id']}")
    print(f"title: {data['title']}")
    print(f"body: {data['body']}")
    print(f"userId: {data['userId']}")

except requests.exceptions.Timeout:
    print("요청 시간 초과")

except requests.exceptions.HTTPError as err:
    print(f"HTTP error: {err}")

except requests.exceptions.RequestException as err:
    print(f"Req Error: {err}")