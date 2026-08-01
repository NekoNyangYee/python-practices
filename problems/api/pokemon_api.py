import requests

url = "https://pokeapi.co/api/v2/pokemon/ditto"

try:
    response = requests.get(
        url=url,
        timeout=5
    )

    response.raise_for_status()
    data = response.json()

    print(f"이름: {data['name']}")
    print(f"키: {data['height']}")
    print(f"몸무게: {data['weight']}")
    print(f"기본 경험치: {data['base_experience']}")
    print(f"능력 갯수: {len(data['abilities'])}")

except requests.exceptions.Timeout:
    print("요청 시간 초과")

except requests.exceptions.HTTPError as err:
    print(f"HTTP err: {err}")

except requests.exceptions.RequestException as err:
    print(f"Req Err: {err}")