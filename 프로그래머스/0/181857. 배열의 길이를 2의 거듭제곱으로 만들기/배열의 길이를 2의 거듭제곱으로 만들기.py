def solution(arr):
    num = 1
    
    while num<len(arr):
        num*=2
    zero = num-len(arr)
    
    return arr + [0] * zero
        