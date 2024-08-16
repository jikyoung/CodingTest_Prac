# def solution(arr):
#     stk = []
#     i = 0
#     while i<len(arr):
#         if not stk:
#             stk.append(arr[i])
#             i+=1
#         elif stk[-1]<arr[i]:
#             stk.append(arr[i])
#             i+=1
#         else:
#             stk.pop()
#     return stk
def solution(arr):
    stk = []
    for num in arr:
        while stk and stk[-1] >= num:
            stk.pop()
        stk.append(num)
    return stk
    