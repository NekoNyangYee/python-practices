import requests

story_ids_url = "https://hacker-news.firebaseio.com/v0/topstories.json"

try:
    response = requests.get(
        url=story_ids_url,
        timeout=5
    )

    response.raise_for_status()
    story_ids = response.json()
    top_five = story_ids[:5]

    for num, story_id in enumerate(top_five, start=1):
        story_detail_url = (
            f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        )

        response_detail = requests.get(
            url=story_detail_url,
            timeout=5
        )

        response_detail.raise_for_status()
        story_detail = response_detail.json()

        print(f"[{num}]")
        print(f"제목: {story_detail['title']}")
        print(f"작성자: {story_detail['by']}")
        print(f"점수: {story_detail['score']}")
        print(f"댓글 개수: {story_detail.get('descendants', 0)}")
        print(f"URL: {story_detail.get('url', 'URL 없음')}")
        print()

except requests.exceptions.Timeout:
    print("요청 시간 초과")

except requests.exceptions.HTTPError as err:
    print(f"HTTP err: {err}")

except requests.exceptions.RequestException as err:
    print(f"Req err: {err}")