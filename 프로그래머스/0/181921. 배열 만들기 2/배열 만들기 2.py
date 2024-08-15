# def is_valid_number(num):
#     """Check if a number is composed only of '0' and '5'."""
#     return all(c in '05' for c in str(num))

# def solution(l, r):
#     result = []
    
#     # Iterate through all numbers in the range
#     for num in range(l, r + 1):
#         if is_valid_number(num):
#             result.append(num)
    
#     # Return sorted result or -1 if no valid number found
#     if result:
#         return sorted(result)
#     else:
#         return [-1]
from collections import deque

def generate_valid_numbers(l, r):
    """Generate all numbers composed of '0' and '5' within the range [l, r]."""
    valid_numbers = set()
    queue = deque(['5'])  # Start with the smallest valid number
    
    # While there are numbers to process
    while queue:
        current = queue.popleft()
        num = int(current)
        
        # Check if the number is within the range
        if l <= num <= r:
            valid_numbers.add(num)
        
        # Generate new numbers by appending '0' and '5'
        if num <= r:
            queue.append(current + '0')
            queue.append(current + '5')
    
    return sorted(valid_numbers)

def solution(l, r):
    # Generate valid numbers in the range and return them
    valid_numbers = generate_valid_numbers(l, r)
    if valid_numbers:
        return valid_numbers
    else:
        return [-1]
