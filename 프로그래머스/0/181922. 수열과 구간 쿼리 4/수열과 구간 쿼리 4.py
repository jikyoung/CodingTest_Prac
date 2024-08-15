# def solution(arr, queries):
#     for s, e, k in queries:
#         indices = [i for i in range(s, e+1) if i % k == 0]
#         for i in indices:
#             arr[i] += 1
#     return arr
def solution(arr, queries):
    n = len(arr)
    
    for s, e, k in queries:
        # 예외 처리: 범위와 k의 유효성 검사
        if s < 0 or e >= n or s > e:
            continue  # 잘못된 범위의 경우 쿼리를 무시
        if k <= 0:
            continue  # 잘못된 k 값은 무시
        
        # 첫 번째 유효한 인덱스 계산
        start = s + (k - s % k) if s % k != 0 else s
        
        # start부터 k 간격으로 인덱스 증가
        for i in range(start, e + 1, k):
            arr[i] += 1
    
    return arr