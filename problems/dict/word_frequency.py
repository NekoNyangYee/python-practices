# 🧩 문제: 단어 빈도 세기 (Word Frequency Counter)
# 문자열을 입력받아,
# 문자열 안에 있는 각 단어가 몇 번 등장했는지 세어
# 딕셔너리 형태로 출력하세요.

# 입력 예시 1
# nginx
# 코드 복사
# apple banana apple grape banana apple
# 출력 예시 1
# bash
# 코드 복사
# {'apple': 3, 'banana': 2, 'grape': 1}
# 입력 예시 2
# bash
# 코드 복사
# Dog cat dog dog bird cat
# 출력 예시 2
# bash
# 코드 복사
# {'dog': 3, 'cat': 2, 'bird': 1}


def word_frequency(input):
    lower_input = input.lower()
    split_input = lower_input.split(' ')
    result = {}

    for fruit in split_input:
        if fruit in result:
            result[fruit] += 1
        else:
            result[fruit] = 1
    
    print(result)

word_frequency("apple banana apple grape banana apple")