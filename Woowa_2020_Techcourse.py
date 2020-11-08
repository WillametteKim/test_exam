def solution(grades, weights, threshold):
    answer = -1234567890
    gradeReference = {'A+': 10, 'A0': 9, 'B+': 8, 'B0': 7, 'C+': 6, 'C0': 5, 'D+':4, 'D0': 3, 'F': 0}
    
    myCredit = 0
    for i in range(len(grades)):
        myCredit += gradeReference[grades[i]] * weights[i]

    answer = myCredit - threshold
    return answer
#############################################
def solution(s, op):
    answer = []    
    
    for i in range(len(s)-1):
        s1 = s[:i+1]
        s2 = s[i+1:]
        
        if(op == '+'): answer.append(add(int(s1), int(s2)))
        elif(op == '-'): answer.append(minus(int(s1), int(s2)))
        elif(op == '*'): answer.append(multiply(int(s1), int(s2)))
    
    return answer

def add(n1, n2): 
    return n1 + n2
def minus(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
#############################################
def solution(money, expected, actual):
    answer = -1
    bet = 100
    
    for i in range(len(expected)): 
        if money == 0:                          # no money
            break;
        elif(judge(expected[i], actual[i])):    # he won
            money += bet
            bet = 100
        else:                                   # he lose
            money -= bet
            if money < bet * 2: 
                bet = money
            else:
                bet *= 2
    return money

def judge(expectedVal, actualVal): 
    if expectedVal == actualVal: 
        return True
    return False
#############################################
def solution(n, board):
    answer = 0
    posDict = mapPos(n, board)
    currentPos = [0,0]
    
    for i in range(1, n*n+1):
        answer +=  walker(currentPos, posDict[i], n)
        print(answer)
        currentPos = posDict[i]

    return answer + n*n

def mapPos(n, board):   # check all values' location
    posDict = {}
    for i in range(n):
        for j in range(n): 
            posDict.update({board[i][j]:[i, j]})
    return posDict

def walker(currentPos, targetPos, n):
    x_dist1 = abs(targetPos[0] - currentPos[0])
    x_dist2 = abs(targetPos[0] - (currentPos[0] + n))
    x_dist3 = abs(targetPos[0] - (currentPos[0] - n))
    y_dist1 = abs(targetPos[1] - currentPos[1])
    y_dist2 = abs(targetPos[1] - (currentPos[1] + n))
    y_dist3 = abs(targetPos[1] - (currentPos[1] - n))
    
    return (min(x_dist1, x_dist2, x_dist3) + min(y_dist1, y_dist2, y_dist3))

#############################################
def solution(penter, pexit, pescape, data):
    datalen = len(penter)
    splitData = []
    
    while len(data) != 0: 
        splitData.append(data[:datalen])
        data = data[datalen:]

    answer = ''
    answer += penter 
    for i in range(len(splitData)):
        if splitData[i] == penter or splitData[i] == pexit or splitData[i] == pescape: 
            answer += pescape
            
        answer += splitData[i]
    answer += pexit 
    return answer
#############################################
# 못품 ㅜㅜ 
#############################################

RIGHT = 2
DOWN = 1
DIAGONAL = 0

def solution(n, horizontal):
    map = [[0] * n for _ in range(n)]
    endPos = [n-1, n-1]
    direction = False  # False means heading to 7'o, True means heading to 1'o
    priorMoving = False  # False means moved diagonally, True means moved vertical/horizontally
    currentPos = [0, 0]
    nextPos = [0, 0]
    time = 0

    # 처음 한번 움직인 뒤
    if horizontal:
        currentPos, time, map, priorMoving = moveVertiHorizontally(RIGHT, currentPos, time, map, priorMoving)
        direction = False
    else:
        currentPos, time, map, priorMoving = moveVertiHorizontally(DOWN, currentPos, time, map, priorMoving)
        direction = True

    while(currentPos != endPos):
        nextPos = calcNextPos(currentPos, n, direction)
        print(map)
        print(currentPos, nextPos, direction, priorMoving)
        if priorMoving:
            currentPos, time, map, priorMoving = moveDiagonally(currentPos, nextPos, time, map)
        else:
            retval, direction = checkBoundary(nextPos, n, direction)
            print(direction); print()
            if retval is RIGHT:
                currentPos, time, map, priorMoving = moveVertiHorizontally(RIGHT, currentPos, time, map,
                                                                                      priorMoving)
            elif retval is DOWN:
                currentPos, time, map, priorMoving = moveVertiHorizontally(DOWN, currentPos, time, map, priorMoving)
            else:
                currentPos, time, map, priorMoving = moveDiagonally(currentPos, nextPos, time, map)

    return time

def calcNextPos(currentPos, n, direction):
    if direction:
        nextPos = [currentPos[0]-1, currentPos[1]+1]
    else:
        nextPos = [currentPos[0]+1, currentPos[1]-1]
    return nextPos

def checkBoundary(nextPos, n, direction):
    if nextPos[0] >= n and nextPos[1] < 0:
        direction = not direction
        return RIGHT, direction
    elif nextPos[0] < 0 and nextPos[1] >= n:
        direction = not direction
        return DOWN, direction
    elif nextPos[0] < 0:
        direction = not direction
        return RIGHT, direction
    elif nextPos[1] < 0:
        direction = not direction
        return DOWN, direction
    elif nextPos[0] >= n:
        direction = not direction
        return RIGHT, direction
    elif nextPos[1] >= n:
        direction = not direction
        return DOWN, direction
    else:
        return DIAGONAL, direction

def moveVertiHorizontally(cmd, currentPos, time, map, priorMoving):
    if cmd is RIGHT:
        currentPos[1] += 1
        #direction = False
    else:
        currentPos[0] += 1
        #direction = True

    time += 1
    map[currentPos[0]][currentPos[1]] = time
    priorMoving = True
    return currentPos, time, map, priorMoving

def moveDiagonally(currentPos, nextPos, time, map):
    currentPos = nextPos
    time += 2
    map[currentPos[0]][currentPos[1]] = time
    priorMoving = False
    return currentPos, time, map, priorMoving
