def solution(my_string, alp):
    new_my_string = ''.join(char.upper() if char == alp else char for char in my_string)
    return new_my_string