def solution(q, r, code):
    # result = ''
    # for i,j in enumerate(code):
    #     if i%q==r:
    #         result += code[i]
    # return result
    
    result = [code[i] for i in range(len(code)) if i % q == r]
    return ''.join(result)

    # code[r::q]