# 🧩 문제: 4글자 이상 단어만 대문자로 변환하기

# 문자열 리스트가 주어졌을 때,
# 그 중에서 길이가 4글자 이상인 단어만 골라,
# 그 단어들을 모두 대문자로 변환한 새로운 리스트를 만들어 출력하세요.

# 입력 예시 1
# ["apple", "dog", "banana", "cat", "grape"]

# 출력 예시 1
# ["APPLE", "BANANA", "GRAPE"]

# 입력 예시 2
# ["hi", "hello", "sun", "world", "python"]

# 출력 예시 2
# ["HELLO", "WORLD", "PYTHON"]

def filter_and_transform_words(input_str):
    arr = [word.upper() for word in input_str if len(word) >= 4]
    print(arr)

filter_and_transform_words(["hi", "hello", "sun", "world", "python"])

# 항목	평가	코멘트
# 리스트 컴프리헨션	⭐⭐⭐⭐⭐	완벽하게 사용함
# 조건문 활용	⭐⭐⭐⭐⭐	길이 조건 정확
# 함수 구조	⭐⭐⭐⭐☆	return 사용해도 좋음
# 변수명	⭐⭐⭐⭐☆	string → word가 더 자연스러움