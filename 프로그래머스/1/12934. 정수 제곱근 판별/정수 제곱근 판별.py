import math

def is_perfect_square(n):
    sqrt_n = math.sqrt(n)  # 부동소수점 제곱근 계산
    return sqrt_n.is_integer()  # 제곱근이 정수인지 확인

def solution(n):
    if is_perfect_square(n):
        sqrt_n = int(math.sqrt(n))  # 정수 제곱근 계산
        return (sqrt_n + 1) ** 2
    else:
        return -1