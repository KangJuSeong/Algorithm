def top(stack):
    if not len(stack):
        return ''
    else:
        return stack[-1]

def checkCorrect(p):
    _p = list(p)
    stack = []
    stack.append(_p.pop())
    while len(_p):
        tmp = _p.pop()
        if top(stack) == tmp:
            stack.pop()
        else:
            stack.append(tmp)
    if not len(stack):
        return p
    else:
        return 0
    
def checkBalance(p):
    left_cnt = 0
    right_cnt = 0
    for i in p:
        if i == '(': left_cnt +=1
        else: right_cnt += 1
    if left_cnt == right_cnt:
        return 1
    else:
        return 0

def splitUV(p):
    for i in range(len(p)):
        if checkBalance(p[:i+1]):
            u = p[:i+1]
            v = p[i+1:]
            return u, v

def mixUV(u, v):
    if checkCorrect(u):
        _u, _v = splitUV(v)
        return u + mixUV(_u, _v)
    else:
        _u, _v = splitUV(u)
        return mixUV(_u, _v) + v

def solution(p):
    answer = ''
    # if p != '':
    #     answer = checkCorrect(p)
    #     if answer == 0:
    u, v = splitUV(p)
    print(mixUV(u, v))
    return answer