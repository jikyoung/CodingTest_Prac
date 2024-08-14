def solution(number, n, m):
    # 내가 한 풀이
    # if number%n==0:
    #     if number%m==0:
    #         return 1
    #     else:
    #         return 0
    # else:
    #     return 0
    # 다른 사람 풀이
    return 1 if number%n==0 and number%m==0 else 0