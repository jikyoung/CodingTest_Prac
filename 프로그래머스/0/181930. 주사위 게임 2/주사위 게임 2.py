def solution(a, b, c):
    if a != b and a != c and b != c:
        return a + b + c
    elif a == b and b == c: 
        return 3*(a) * 3*(a**2) * 3 * (a**3)
    else:
        return (a + b + c) * (a**2 + b**2 + c**2)