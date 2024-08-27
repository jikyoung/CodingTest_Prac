def solution(myString):
    result = ''
    for S in myString:
        if ord(S) < ord('l'):
            result += 'l'
        else:
            result += S
    return result