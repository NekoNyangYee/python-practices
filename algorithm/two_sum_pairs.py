# 🧩 문제 설명

# 정수로 이루어진 정렬되지 않은 리스트 nums 와
# 정수 target 이 주어졌을 때,

# 리스트 안에서 합이 target이 되는 서로 다른 두 수의 쌍(pair) 을
# 중복 없이 모두 찾아 리스트로 반환하세요.

# 쌍은 작은 수가 앞에 오도록 하고,
# 전체 결과는 사전순(lexicographical order) 으로 정렬해서 출력합니다.

# 🔍 입력 예시 1
# nums = [2, 7, 11, -2, 4, 5, 15]
# target = 9

# 📤 출력 예시 1
# [[-2, 11], [2, 7], [4, 5]]

def two_sum_pairs(nums, target):
    result = []
    start = 0
    end = 1
    duplicate_num = list(set(nums))

    for i in range(start, len(duplicate_num)):
        for j in range(end, len(duplicate_num)):
            if duplicate_num[i] + duplicate_num[j] == target:
                result.append([duplicate_num[i], duplicate_num[j]])
                end += 1

    duplicate_set = set(tuple(sorted(x)) for x in result)
    duplicate_list = [list(x) for x in duplicate_set]
    duplicate_list.sort(key=lambda x:x[0])
    print(duplicate_list)

two_sum_pairs(nums = [2, 7, 11, -2, 4, 5, 15], target = 9)

# 📘 요약 평가
# 항목	점수	이유
# 로직 / 정답 여부	⭐⭐⭐⭐⭐	정답 잘 도출함
# 효율성	⭐⭐⭐	set 활용 OK, but end 증가 구조 비효율적
# 안정성	⭐⭐⭐	set 순서 비보장 + end 구조 문제
# 가독성	⭐⭐⭐	돌아는 가지만 구조적으로 복잡함
# 알고리즘 사고력	⭐⭐⭐⭐	dedupe, sorting, tuple-set 변환 등 좋은 감각 있음