def solution(arr1, arr2):
    # 길이를 비교하여 반환
    if len(arr1) < len(arr2):
        return -1
    if len(arr1) > len(arr2):
        return 1

    # 길이가 같은 경우 합계를 비교하여 반환
    if len(arr1) == len(arr2):
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr1) < sum(arr2):
            return -1
        else:
            return 0