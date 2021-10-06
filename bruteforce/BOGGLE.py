import sys


input = sys.stdin.readline
SIDE = [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]


def hasWord(y, x, word, game_map):
       if y < 0 or y > 4 or x < 0 or x > 4:
           return False

       boolean = (word[0]==game_map[y][x])
       word = word[1:]

       if boolean:
           if not len(word):
               return True
           else:
               for case in SIDE:
                   if hasWord(y + case[0], x + case[1], word, game_map):
                       return True
       else:
           return False


test = int(input())
boggle = []
for k in range(test):
    for i in range(5):
        boggle.append(list(input()))
        boggle[i].pop()
    _test = int(input())
    for _ in range(_test):
        target = list(input())
        target.pop()
        first = target[0]
        init = []
        for y in range(5):
            for x in range(5):
                if first == boggle[y][x]:
                    init.append([y, x])
        flag = False
        for pos in init:
            result = hasWord(pos[0], pos[1], target, boggle)
            if result: 
                flag = True
                break
        for t in target:
            print(t, end='')
        if flag: print(' YES')
        else: print(' NO')        
    