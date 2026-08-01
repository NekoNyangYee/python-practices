import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "파이썬 API 연습",
    "body": "POST 요청을 테스트합니다.",
    "userId": 4
}

try:
    response = requests.post(
        url,
        json=payload,
        timeout=5
    )

    response.raise_for_status()
    data = response.json()

    print(f"상태 코드: {response.status_code}")
    print(f"게시글 ID: {data['id']}")
    print(f"제목: {data['title']}")
    print(f"내용: {data['body']}")
    print(f"사용자 ID: {data['userId']}")

except requests.exceptions.Timeout:
    print("요청 시간이 초과되었습니다.")

except requests.exceptions.HTTPError as err:
    print(f"HTTP 오류: {err}")

except requests.exceptions.RequestException as err:
    print(f"요청 오류: {err}")