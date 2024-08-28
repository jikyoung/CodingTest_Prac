from collections import deque

def solution(numbers, k):
    
    dq = deque(numbers)
    for _ in range(k - 1):
        dq.append(dq.popleft())
        dq.append(dq.popleft())
    
    return dq[0]
        
    