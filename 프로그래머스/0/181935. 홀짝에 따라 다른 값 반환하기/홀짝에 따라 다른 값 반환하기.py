def solution(n):
    # 내 풀이
#     odd=0
#     even=0
    
#     if n%2!=0:
#         for i in range(1, n+1):
#             if i%2!=0:
#                 odd+=i
#         return odd
#     else:
#         for i in range(1, n+1):
#             if i%2==0:
#                 even+=i**2
#         return even
    if n%2:
        return sum(range(1,n+1,2))
    return sum(i*i for i in range(2,n+1,2))
                
                
                
        