def solution(numbers):
    # 숫자를 문자열로 변환
    str_numbers = list(map(str, numbers))
    
    # 정렬 기준을 설정하여 내림차순 정렬
    sorted_numbers = sorted(str_numbers, key=lambda x: x * 10, reverse=True)
        
    # 정렬된 문자열을 합쳐서 최종 결과를 생성
    result = ''.join(sorted_numbers)
    
    # 결과가 '0'으로만 구성된 경우, '0' 반환
    return '0' if result[0] == '0' else result