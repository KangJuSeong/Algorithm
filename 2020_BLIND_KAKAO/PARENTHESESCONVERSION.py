def checkBalance(p):
    cnt = 0
    for i in p:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
    return not(bool(cnt))

def checkCorrect(p):
    cnt = 0
    if not checkBalance(p):
        return False
    for i in p:
        if i == '(':
            cnt += 1
        else: cnt -= 1
        if cnt < 0:
            return False
    return True

def solution(p):
    if checkCorrect(p):
        return p
    
    for i in range(2, len(p)+1, 2):
        if checkBalance(p[:i]):
            u, v = p[:i], p[i:]
            break
    if checkCorrect(u):
        return u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        for i in u[1:-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
        return answer
