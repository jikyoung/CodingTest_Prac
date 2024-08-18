def solution(my_string, indices):
    my_string=list(my_string)
    
    result = [char for i, char in enumerate(my_string) if i not in indices]
    return ''.join(result)