from collections import Counter

def solution(a, b, c, d):
    # 주사위 수를 저장할 리스트
    dice = [a, b, c, d]
    
    # 주사위 값의 빈도를 계산
    counts = Counter(dice).most_common()
    
    # 조건 1. 네 주사위의 값이 모두 같을 때
    if counts[0][1] == 4:
        return 1111 * counts[0][0]
    
    # 조건 2. 세 주사위의 값이 같고 나머지 하나가 다를 때
    if counts[0][1] == 3:
        return (10 * counts[0][0] + counts[1][0]) ** 2
    
    # 조건 3. 주사위가 두 개씩 같은 값이 나올 때
    if counts[0][1] == 2 and counts[1][1] == 2:
        return (counts[0][0] + counts[1][0]) * abs(counts[0][0] - counts[1][0])
    
    # 조건 4. 어느 두 주사위에서 같은 값이 나오고 나머지 두 주사위가 다른 값을 가질 때
    if counts[0][1] == 2:
        return counts[1][0] * counts[2][0]
    
    # 조건 5. 네 주사위에 적힌 숫자가 모두 다를 때
    return min(dice)