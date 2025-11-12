# 🧩 문제: 최고 점수 학생 찾기 (Find the Top Student)

# 학생 이름과 점수가 들어 있는 딕셔너리를 입력받아,
# 가장 높은 점수를 받은 학생의 이름과 점수를 출력하세요.

# 입력 예시 1
# {"Alice": 82, "Bob": 91, "Charlie": 88}

# 출력 예시 1
# Bob 91

# 입력 예시 2
# {"Minho": 75, "Yuna": 92, "Jisoo": 85, "Taeyang": 92}

# 출력 예시 2
# Yuna 92


# 최고 점수가 여러 명이라면 사전 순으로 이름이 앞선 학생을 출력합니다.
# (예: "Yuna" vs "Taeyang" → "Taeyang"이 아니라 "Yuna" 출력)

def highest_score_student(input):
    # user_li = []
    # user_dict = list(input.keys())
    # max_score = max(input.values())

    # for user in user_dict:
    #     if (input[user] == max_score):
    #         user_li.append(user)

    # print(f"{user_li[0]} {input[user_li[0]]}")

    max_score = max(input.values())

    top_students = [name for name, score in input.items() if score == max_score]

    top_name = sorted(top_students)[0]

    print(f"{top_name} {input[top_name]}")


highest_score_student({"Alice": 82, "Bob": 91, "Charlie": 88})
