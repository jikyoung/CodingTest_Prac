# def solution(arr):
#     indices = [i for i,x in enumerate(arr) if x == 2]
    
#     if not indices:
#         return [-1]
    
#     start = indices[0]
#     end = indices[-1]
    
#     return arr[start:end+1]

def solution(arr):
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]
