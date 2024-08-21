def solution(arr, intervals):
    result = list()
    for i in intervals:
        a, b = i
        # result.extend(arr[a:b+1])
        result += arr[a:b+1]
    return result
        