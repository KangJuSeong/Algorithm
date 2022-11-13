board = [
    [0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]
        ]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
        

def solution(board, moves):
    answer = 0
    picked = []
    picked_pos = []
    for pick in moves:
        y = pick - 1
        for x, v in enumerate(board):
            if (x, y) in picked_pos:
                continue
            if v[y] != 0:
                picked_pos.append((x, y))
                if len(picked) != 0 and picked[-1] == v[y]:
                    picked.pop()
                    answer += 1
                    break
                else:
                    picked.append(v[y])
    return answer

if '__main__' == __name__:
    print(solution(board, moves))
