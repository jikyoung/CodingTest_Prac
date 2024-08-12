def solution(num):
    # 내 풀이
#     if num[-1] > num[-2]:
#         num.append(num[-1] - num[-2])
#     else:
#         num.append(num[-1] * 2)
    
#     return num
    # 효율적인 풀이
    num.append(num[-1]-num[-2] if num[-1]>num[-2] else num[-1]*2)
    return num