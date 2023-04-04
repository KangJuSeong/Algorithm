import sys
input = sys.stdin.readline


#  u = 흰색, d = 노란색, f = 빨간색, b = 오렌지색, l = 초록색, r = 파란색
# + = 시계 방향, - = 반시계 방향
def print_cube(cube):
    for k, v in cube.items():
        print(f'{k}:')
        for i in range(3):
            for j in range(3):
                print(f'{v[i][j]} ', end='')
            print()
        print()


def print_ans(cube):
    for i in range(3):
        for j in range(3):
            print(f'{cube["U"][i][j]}', end='')
        print()


def turn(cube, face, arrow):
    new_arr = [[0] * 3 for _ in range(3)]
    if arrow == '+':
        for i in range(3):		# 기존 행렬의 행 이동
            for j in range(3):	# 기존 행렬의 열 이동
                new_arr[j][2-i] = cube[face][i][j]
    else:
        for i in range(3):
            for j in range(3):
                new_arr[2-j][i] = cube[face][i][j]
    return new_arr


def rotation(cube, face, arrow):
    if face == 'U':
        if arrow == '+': # F->L, L->B, B->R, R->F
            cube['L'].insert(1, cube['F'].pop(0))
            cube['B'].insert(1, cube['L'].pop(0))
            cube['R'].insert(1, cube['B'].pop(0))
            cube['F'].insert(0, cube['R'].pop(0))
        else:  # F->R, R->B, B->L, L->F
            cube['R'].insert(1, cube['F'].pop(0))
            cube['B'].insert(1, cube['R'].pop(0))
            cube['L'].insert(1, cube['B'].pop(0))
            cube['F'].insert(0, cube['L'].pop(0))
    elif face == 'D':
        if arrow == '+': # B->L, L->F, F->R, R->B
            cube['L'].insert(2, cube['B'].pop(2))
            cube['F'].insert(2, cube['L'].pop(3))
            cube['R'].insert(2, cube['F'].pop(3))
            cube['B'].insert(2, cube['R'].pop(3))
        else:  # B->R, R->F, F->L, L->B
            cube['R'].insert(2, cube['B'].pop(2))
            cube['F'].insert(2, cube['R'].pop(3))
            cube['L'].insert(2, cube['F'].pop(3))
            cube['B'].insert(2, cube['L'].pop(3))
    elif face == 'F':
        if arrow == '+':
            tmp = cube['U'].pop(2)
            _tmp = list()
            for i in range(3):
                _tmp.append(cube['R'][i][0])
                cube['R'][i][0] = tmp[i]
            tmp = cube['D'].pop(2)
            cube['D'].append(_tmp)
            _tmp = list()
            for i in range(3):
                _tmp.append(cube['L'][2-i][2])
                cube['L'][2-i][2] = tmp[i]
            cube['U'].append(_tmp)
        else: 
            for _ in range(3):
                tmp = cube['U'].pop(2)
                _tmp = list()
                for i in range(3):
                    _tmp.append(cube['R'][i][0])
                    cube['R'][i][0] = tmp[i]
                tmp = cube['D'].pop(2)
                cube['D'].append(_tmp)
                _tmp = list()
                for i in range(3):
                    _tmp.append(cube['L'][2-i][2])
                    cube['L'][2-i][2] = tmp[i]
                cube['U'].append(_tmp)
    elif face == 'B':
        if arrow == '+':
            tmp = cube['U'].pop(0)
            _tmp = list()
            for i in range(3):
                _tmp.append(cube['L'][2-i][0])
                cube['L'][2-i][0] = tmp[i]
            tmp = cube['D'].pop(0)
            cube['D'].insert(0, _tmp)
            _tmp = list()
            for i in range(3):
                _tmp.append(cube['R'][i][2])
                cube['R'][i][2] = tmp[i]
            cube['U'].insert(0, _tmp)
        else:
            for k in range(3):
                tmp = cube['U'].pop(0)
                _tmp = list()
                for i in range(3):
                    _tmp.append(cube['L'][2-i][0])
                    cube['L'][2-i][0] = tmp[i]
                tmp = cube['D'].pop(0)
                cube['D'].insert(0, _tmp)
                _tmp = list()
                for i in range(3):
                    _tmp.append(cube['R'][i][2])
                    cube['R'][i][2] = tmp[i]
                cube['U'].insert(0, _tmp)
    elif face == 'L':
        if arrow == '+':
            for i in range(3):
                cube['F'][i].insert(1, cube['U'][i].pop(0))
            for i in range(3):
                cube['D'][2-i].insert(2, cube['F'][i].pop(0))
            for i in range(3):
                cube['B'][i].insert(2, cube['D'][i].pop(-1))
            for i in range(3):
                cube['U'][2-i].insert(0, cube['B'][i].pop(-1))
        else:
            for k in range(3):
                for i in range(3):
                    cube['F'][i].insert(1, cube['U'][i].pop(0))
                for i in range(3):
                    cube['D'][2-i].insert(2, cube['F'][i].pop(0))
                for i in range(3):
                    cube['B'][i].insert(2, cube['D'][i].pop(-1))
                for i in range(3):
                    cube['U'][2-i].insert(0, cube['B'][i].pop(-1))
    else:
        if arrow == '+':
            for i in range(3):
                cube['B'][2-i].insert(1, cube['U'][i].pop(-1))
            for i in range(3):
                cube['D'][i].insert(1, cube['B'][i].pop(0))
            for i in range(3):
                cube['F'][2-i].insert(2, cube['D'][i].pop(0))
            for i in range(3):
                cube['U'][i].insert(2, cube['F'][i].pop(-1))
        else:
            for k in range(3):
                for i in range(3):
                    cube['B'][2-i].insert(1, cube['U'][i].pop(-1))
                for i in range(3):
                    cube['D'][i].insert(1, cube['B'][i].pop(0))
                for i in range(3):
                    cube['F'][2-i].insert(2, cube['D'][i].pop(0))
                for i in range(3):
                    cube['U'][i].insert(2, cube['F'][i].pop(-1))
    cube[face] = turn(cube, face, arrow)
    return cube


N = int(input())
for i in range(N):
    cube = {'U': [['w', 'w', 'w'],
                  ['w', 'w', 'w'],
                  ['w', 'w', 'w']],
            'D': [['y', 'y', 'y'],
                  ['y', 'y', 'y'],
                  ['y', 'y', 'y']],
            'F': [['r', 'r', 'r'],
                  ['r', 'r', 'r'],
                  ['r', 'r', 'r']],
            'B': [['o', 'o', 'o'],
                  ['o', 'o', 'o'],
                  ['o', 'o', 'o']],
            'L': [['g', 'g', 'g'],
                  ['g', 'g', 'g'],
                  ['g', 'g', 'g']],
            'R': [['b', 'b', 'b'],
                  ['b', 'b', 'b'],
                  ['b', 'b', 'b']],
            }
    case = int(input()[:-1])
    cmd = list(map(str, input().split()))
    for c in cmd:
        cube = rotation(cube, c[0], c[1])
    print_ans(cube)
