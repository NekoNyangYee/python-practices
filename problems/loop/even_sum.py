# 문제: 1부터 N까지의 합 중 짝수만 더하기

# 정수 N을 입력받아 1부터 N까지 중 짝수만 합한 값을 출력하세요.

# 입력 예시

# 10


# 출력 예시

# 30


# 설명: 2+4+6+8+10 = 30

def even_sum(input_stirng):
    num = int(input_stirng)
    total = 0

    for i in range(1, num+1):
        if (i % 2 == 0):
            total += i
    
    print(total)
    
even_sum("10")

# ✅ 총평
# 문제 이해	⭐⭐⭐⭐⭐	조건 정확히 반영
# 코드 정확성	⭐⭐⭐⭐⭐	출력 값 정확
# 가독성	⭐⭐⭐⭐☆	변수명만 조정하면 완벽
# 오류 처리 능력	⭐⭐⭐⭐☆	에러 원인 파악하면 더 좋음
