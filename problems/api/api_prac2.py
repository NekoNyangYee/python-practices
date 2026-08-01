import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 3
}

try:
    response = requests.get(
        url,
        params=params,
        timeout=5
    )

    response.raise_for_status()
    data = response.json()

    print(f"게시글 개수: {len(data)}")
    print()

    for post in data:
        print(f"게시글 ID: {post['id']}")
        print(f"제목: {post['title']}")
        print()

except requests.exceptions.Timeout:
    print("요청 시간이 초과되었습니다.")

except requests.exceptions.HTTPError as error:
    print(f"HTTP 오류: {error}")

except requests.exceptions.RequestException as error:
    print(f"요청 오류: {error}")