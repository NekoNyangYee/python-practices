# 문제: 문자열 뒤집는 함수 만들기

# 문자열을 입력받아서 뒤집어서 반환하는 함수를 작성하세요.

# 입력 예시

# hello


# 출력 예시

# olleh

def reverse_string(input_str):
    print(input_str[::-1])

reverse_string("hello")

# ✅ 총평
# 문제 이해	⭐⭐⭐⭐⭐	요구사항 완벽 반영
# 코드 정확성	⭐⭐⭐⭐⭐	완벽
# 파이썬 스타일	⭐⭐⭐⭐⭐	슬라이싱 활용 Good
# 확장성	⭐⭐⭐⭐☆	반환형 활용 시 더 유연