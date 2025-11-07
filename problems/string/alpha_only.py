# 문제: 알파벳만 남기기

# 사용자에게 문자열을 입력받아서, 그 중에서 알파벳 문자만 남기고 출력하세요.
# 대소문자는 그대로 유지합니다.

# 입력 예시

# a1b2c3D4!@


# 출력 예시

# abcD

import re

def only_alphabets(input_string):
    reg = r"[a-zA-Z]+"
    p = re.findall(reg, input_string)
    print(''.join(p))

only_alphabets("a1b2c3D4!@")

# 문제 통과 
# ✅ 총평
# 문제 이해	⭐⭐⭐⭐⭐	요구사항을 정확히 반영
# 코드 가독성	⭐⭐⭐⭐☆	명료함. 정규식은 약간 난이도 있지만 잘 사용함
# 효율성	⭐⭐⭐⭐☆	문자열 길이에 비례, 충분히 효율적
# 확장성	⭐⭐⭐⭐☆	다른 입력에도 문제 없음