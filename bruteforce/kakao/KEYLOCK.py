def rotate(key):
    result = []
    M = len(key) - 1
    for i in range(M+1):
        row = []
        for j in range(M, -1, -1):
            row.append(key[j][i])
        result.append(row)
    return result

def checkFull(key, lock, N):
    size = len(key)
    cnt = 0
    for i in range(size):
        for j in range(size):
            if key[i][j] == 1 and lock[i][j] == 1:
                return 0
            elif key[i][j] == 1 and lock[i][j] != 2 and lock[i][j] != 1:
                cnt += 1
    for i in range(size):
        for j in range(size):
            if lock[i][j] == 1:
                cnt += 1
    if cnt == N * N:
        return 1
    else:
        return 0

def moveRight(key, lock, limit, cnt, N):
    if limit == cnt:
        return 0
    elif checkFull(key, lock, N):
        return 1
    else:
        expand_key = []
        for i, v in enumerate(key):
            expand_key.append(list(v))
            expand_key[i].insert(0, 0)
            expand_key[i].pop()
        return moveRight(expand_key, lock, limit, cnt+1, N)

def moveDown(key, map_size):
    key.insert(0, [0 for i in range(map_size)])
    key.pop()
    return key

def solution(key, lock):
    answer = 0
    M = len(key)
    N = len(lock)
    map_size = M + N + 1
    expand_lock = [[2 for i in range(map_size)] for j in range(map_size)]
    for i in range(N):
        for j in range(N):
            expand_lock[i+M-1][j+M-1] = lock[i][j]
    for i in range(4):
        key = rotate(key)
        expand_key = [[0 for i in range(map_size)] for j in range(map_size)]
        for j in range(M):
            for k in range(M):
                expand_key[j][k] = key[j][k]
        for j in range(M+N-1):
            answer = moveRight(expand_key, expand_lock, M+N-1, 0, N)
            if answer == 1:
                break
            expand_key = moveDown(expand_key, map_size)
        if answer == 1:
            break
    if answer == 1:
        return True
    else:
        return False