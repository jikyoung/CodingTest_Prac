def solution(arr, k):
    result = []
    for i in arr:
        if i not in result:
            result.append(i)
        if len(result)==k:
            break
    return result + [-1] * (k-len(result))
#     result = []
#     seen = set()
    
#     for i in arr:
#         if i not in seen:
#             seen.add(i)
#             result.append(i)
#         if len(result)==k:
#             return result
    
#     while len(result) < k:
#         result.append(-1)
        
#     return result
        
            
        
            
        