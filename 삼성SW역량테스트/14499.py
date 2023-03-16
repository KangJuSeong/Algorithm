import sys
input = sys.stdin.readline



# 동쪽=1, 서쪽=2, 북쪽=3, 남쪽=4
N, M , y, x, K = map(int, input().split())
dy, dx = (0, 0, 0, -1, 1), (0, 1, -1, 0, 0)
board = list()
dice = {'up': 0, 'down': 0, 'left': 0, 'right': 0, 'top': 0, 'bottom': 0} 
for _ in range(N):
    board.append(list(map(int, input().split())))
commands = list(map(int, input().split()))

def out_of_range(dy, dx):
    if y+dy < 0 or y+dy == N or x+dx < 0 or x+dx == M:
        return True
    return False

def move(dy, dx):
    if board[y+dy][x+dx] == 0:
        board[y+dy][x+dx] = dice['bottom']
    elif board[y+dy][x+dx] != 0:
        dice['bottom'] = board[y+dy][x+dx]
        board[y+dy][x+dx] = 0
    print(dice['top'])
    return y+dy, x+dx
    
def roll(arrow):
    if arrow == 1:
        left, right, top, bottom = dice['left'], dice['right'], dice['top'], dice['bottom']
        dice['left'] = bottom
        dice['right'] = top
        dice['top'] = left
        dice['bottom'] = right
    elif arrow == 2:
        left, right, top, bottom = dice['left'], dice['right'], dice['top'], dice['bottom']
        dice['left'] = top
        dice['right'] = bottom
        dice['top'] = right
        dice['bottom'] = left
    elif arrow == 3:
        up, down, top, bottom = dice['up'], dice['down'], dice['top'], dice['bottom']
        dice['up'] = top
        dice['top'] = down
        dice['down'] = bottom
        dice['bottom'] = up
    else:
        up, down, top, bottom = dice['up'], dice['down'], dice['top'], dice['bottom']
        dice['up'] = bottom
        dice['top'] = up
        dice['down'] = top
        dice['bottom'] = down
        
for c in commands:
    if out_of_range(dy[c], dx[c]):
        continue
    roll(c)
    y, x = move(dy[c], dx[c])