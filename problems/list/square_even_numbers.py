# 🧩 문제: 짝수 제곱 리스트 만들기

# 정수 리스트가 주어졌을 때,
# 그 안에서 짝수인 숫자만 골라,
# 그 숫자들의 제곱 값을 담은 리스트를 만들어 출력하세요.

# 입력 예시 1
# [1, 2, 3, 4, 5, 6]

# 출력 예시 1
# [4, 16, 36]

# 입력 예시 2
# [10, 15, 22, 33, 40]

# 출력 예시 2
# [100, 484, 1600]

def square_even_numbers(input_str):
    arr = [num ** 2 for num in input_str if num % 2 == 0]
    print(arr)

square_even_numbers([1, 2, 3, 4, 5, 6])
