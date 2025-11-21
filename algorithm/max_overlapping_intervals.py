# 🧩 문제: 가장 많이 겹치는 구간 개수 구하기 (Maximum Overlapping Intervals)

# 여러 개의 시간 구간(intervals)이 리스트로 주어진다.
# 각 구간은 [start, end] 형태이며, start ≤ end 를 만족한다.

# 이때,
# 어떤 시점에서든 동시에 가장 많이 겹치는 구간의 개수를 구하라.

# ✨ 입력 예시 1
# intervals = [
#     [1, 4],
#     [2, 5],
#     [9, 12],
#     [5, 9],
#     [5, 12]
# ]

# ✔️ 출력 예시 1
# 2

# 📌 설명

# 시간 흐름에서 구간 겹침 수를 보면:

# 1~2: 1개

# 2~4: 2개

# 4~5: 2개

# 5~9: 2개

# 9~12: 2개

# 최대 겹침 개수 = 2

# ✨ 입력 예시 2
# intervals = [
#     [1, 3],
#     [2, 4],
#     [3, 5],
#     [7, 9]
# ]

# ✔️ 출력 예시 2
# 3

# 📌 설명

# 시간 3에서 [1,3], [2,4], [3,5] 구간이 3개 겹침


def max_overlapping_intervals(intervals):
    events = []

    # 시작점은 +1, 끝점은 -1 이벤트로 저장
    for start, end in intervals:
        events.append((start, 1))   # 시작
        events.append((end, -1))    # 끝

    # 시간 기준 정렬
    # 시간이 같다면 끝(-1)이 먼저 와야 겹침 계산이 맞음
    events.sort(key=lambda x: (x[0], x[1]))

    current = 0
    max_overlap = 0

    for time, change in events:
        current += change
        max_overlap = max(max_overlap, current)

    return max_overlap


# 실행 예시
print(max_overlapping_intervals([[1, 3], [2, 4], [3, 5], [7, 9]]))


