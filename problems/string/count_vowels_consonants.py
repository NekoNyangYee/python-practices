# 🧩 문제: 모음과 자음 개수 세기

# 문자열을 입력받아,
# 그 안에 포함된 영문 모음(vowel) 과 자음(consonant) 의 개수를 각각 출력하세요.

# 입력 예시 1
# Hello World

# 출력 예시 1
# Vowels: 3
# Consonants: 7

# 입력 예시 2
# Python Programming

# 출력 예시 2
# Vowels: 4
# Consonants: 13

def count_vowels_consonants(input_str):
    vowels = 0
    consonants = 0
    
    for str in input_str.lower():
        if str.isalpha():
            if str in "aeiou":
                vowels += 1
            else:
                consonants += 1
            
    print(f"vowels: {vowels}")
    print(f"consonant: {consonants}")

count_vowels_consonants("Python Programming")