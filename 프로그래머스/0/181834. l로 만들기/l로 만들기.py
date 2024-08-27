def solution(myString):
    result = [ 'l' if S < 'l' else S for S in myString ]

    return ''.join(result)