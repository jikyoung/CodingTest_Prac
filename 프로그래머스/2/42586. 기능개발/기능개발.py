# def solution(progress, speed):
#     # pop(0)가 O(n)의 시간이 걸리기 때문에 비효율적임
#     answer = []
#     while progress:
#         cnt = 0
#         while progress and progress[0]>=100:
#             cnt += 1
#             progress.pop(0)
#             speed.pop(0)
            
#         progress = [progress[i]+speed[i] for i in range(len(progress))]
        
#         if cnt:
#             answer.append(cnt)
#     return answer

# 리스트를 순회하면서 pop(0)을 호출하기보단 인덱스를 사용해 접근
def solution(progress, speed):
    from math import ceil

    # 각 작업의 남은 작업일을 계산합니다.
    days_remaining = [ceil((100 - p) / s) for p, s in zip(progress, speed)]
    
    # 결과를 저장할 리스트
    answer = []
    
    # 첫 번째 배포일을 기준으로 설정
    current_max = days_remaining[0]
    count = 0
    
    for day in days_remaining:
        if day <= current_max:
            # 현재 배포일 내에 완료되는 작업 개수 카운트
            count += 1
        else:
            answer.append(count)
            count=1
            current_max=day
    if count:
        answer.append(count)
        
    return answer
