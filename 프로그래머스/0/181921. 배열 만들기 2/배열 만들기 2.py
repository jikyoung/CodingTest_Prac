def is_valid_number(num):
    """Check if a number is composed only of '0' and '5'."""
    return all(c in '05' for c in str(num))

def solution(l, r):
    result = []
    
    # Iterate through all numbers in the range
    for num in range(l, r + 1):
        if is_valid_number(num):
            result.append(num)
    
    # Return sorted result or -1 if no valid number found
    if result:
        return sorted(result)
    else:
        return [-1]
