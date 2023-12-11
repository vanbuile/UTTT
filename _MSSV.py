import numpy as np
import math
from state import UltimateTTT_Move
ai = -1
player = 1
board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

DEPTV1 = 4
DEPTV2 = 5
DEPTV3 = 6
DEPTV4 = 7

def checkWinCondition(map):
    a = 1
    if (map[0] + map[1] + map[2]  == a * 3 or map[3] + map[4] + map[5]  == a * 3 or map[6] + map[7] + map[8]  == a * 3 or map[0] + map[3] + map[6]  == a * 3 or map[1] + map[4] + map[7]  == a * 3 or
        map[2] + map[5] + map[8]  == a * 3 or map[0] + map[4] + map[8]  == a * 3 or map[2] + map[4] + map[6]  == a * 3):
        return a
    a = -1
    if (map[0] + map[1] + map[2]  == a * 3 or map[3] + map[4] + map[5]  == a * 3 or map[6] + map[7] + map[8]  == a * 3 or map[0] + map[3] + map[6]  == a * 3 or map[1] + map[4] + map[7]  == a * 3 or
        map[2] + map[5] + map[8]  == a * 3 or map[0] + map[4] + map[8]  == a * 3 or map[2] + map[4] + map[6]  == a * 3):
        return a
    return 0

def realEvaluateSquare(pos):
    evaluation = 0
    points = [0.2, 0.17, 0.2, 0.17, 0.22, 0.17, 0.2, 0.17, 0.2]
    for bw in range(9):
        evaluation -= pos[bw] * points[bw]
    a = 2
    if pos[0] + pos[1] + pos[2] == a or pos[3] + pos[4] + pos[5] == a or pos[6] + pos[7] + pos[8] == a:
        evaluation -= 6
    if pos[0] + pos[3] + pos[6] == a or pos[1] + pos[4] + pos[7] == a or pos[2] + pos[5] + pos[8] == a:
        evaluation -= 6
    if pos[0] + pos[4] + pos[8] == a or pos[2] + pos[4] + pos[6] == a:
        evaluation -= 7

    a = -1
    if ((pos[0] + pos[1] == 2*a and pos[2] == -a) or (pos[1] + pos[2] == 2*a and pos[0] == -a) or (pos[0] + pos[2] == 2*a and pos[1] == -a)
        or (pos[3] + pos[4] == 2*a and pos[5] == -a) or (pos[3] + pos[5] == 2*a and pos[4] == -a) or (pos[5] + pos[4] == 2*a and pos[3] == -a)
        or (pos[6] + pos[7] == 2*a and pos[8] == -a) or (pos[6] + pos[8] == 2*a and pos[7] == -a) or (pos[7] + pos[8] == 2*a and pos[6] == -a)
        or (pos[0] + pos[3] == 2*a and pos[6] == -a) or (pos[0] + pos[6] == 2*a and pos[3] == -a) or (pos[3] + pos[6] == 2*a and pos[0] == -a)
        or (pos[1] + pos[4] == 2*a and pos[7] == -a) or (pos[1] + pos[7] == 2*a and pos[4] == -a) or (pos[4] + pos[7] == 2*a and pos[1] == -a)
        or (pos[2] + pos[5] == 2*a and pos[8] == -a) or (pos[2] + pos[8] == 2*a and pos[5] == -a) or (pos[5] + pos[8] == 2*a and pos[2] == -a)
        or (pos[0] + pos[4] == 2*a and pos[8] == -a) or (pos[0] + pos[8] == 2*a and pos[4] == -a) or (pos[4] + pos[8] == 2*a and pos[0] == -a)
        or (pos[2] + pos[4] == 2*a and pos[6] == -a) or (pos[2] + pos[6] == 2*a and pos[4] == -a) or (pos[4] + pos[6] == 2*a and pos[2] == -a)):
        evaluation-=9
    a = -2
    if(pos[0] + pos[1] + pos[2] == a or pos[3] + pos[4] + pos[5] == a or pos[6] + pos[7] + pos[8] == a):
        evaluation += 6

    if(pos[0] + pos[3] + pos[6] == a or pos[1] + pos[4] + pos[7] == a or pos[2] + pos[5] + pos[8] == a):
        evaluation += 6

    if(pos[0] + pos[4] + pos[8] == a or pos[2] + pos[4] + pos[6] == a):
        evaluation += 7

    a = 1
    if((pos[0] + pos[1] == 2*a and pos[2] == -a) or (pos[1] + pos[2] == 2*a and pos[0] == -a) or (pos[0] + pos[2] == 2*a and pos[1] == -a)
        or (pos[3] + pos[4] == 2*a and pos[5] == -a) or (pos[3] + pos[5] == 2*a and pos[4] == -a) or (pos[5] + pos[4] == 2*a and pos[3] == -a)
        or (pos[6] + pos[7] == 2*a and pos[8] == -a) or (pos[6] + pos[8] == 2*a and pos[7] == -a) or (pos[7] + pos[8] == 2*a and pos[6] == -a)
        or (pos[0] + pos[3] == 2*a and pos[6] == -a) or (pos[0] + pos[6] == 2*a and pos[3] == -a) or (pos[3] + pos[6] == 2*a and pos[0] == -a)
        or (pos[1] + pos[4] == 2*a and pos[7] == -a) or (pos[1] + pos[7] == 2*a and pos[4] == -a) or (pos[4] + pos[7] == 2*a and pos[1] == -a)
        or (pos[2] + pos[5] == 2*a and pos[8] == -a) or (pos[2] + pos[8] == 2*a and pos[5] == -a) or (pos[5] + pos[8] == 2*a and pos[2] == -a)
        or (pos[0] + pos[4] == 2*a and pos[8] == -a) or (pos[0] + pos[8] == 2*a and pos[4] == -a) or (pos[4] + pos[8] == 2*a and pos[0] == -a)
        or (pos[2] + pos[4] == 2*a and pos[6] == -a) or (pos[2] + pos[6] == 2*a and pos[4] == -a) or (pos[4] + pos[6] == 2*a and pos[2] == -a)):
        evaluation+=9

    evaluation -= checkWinCondition(pos) * 12

    return evaluation

def evaluateGame(position, currentBoard):
    evale = 0
    mainBd = []
    evaluatorMul = [1.4, 1, 1.4, 1, 1.75, 1, 1.4, 1, 1.4]
    for eh in range(9):
        evale += realEvaluateSquare(position[eh])*1.5*evaluatorMul[eh]
        if(eh == currentBoard):
            evale += realEvaluateSquare(position[eh])*evaluatorMul[eh]
        tmpEv = checkWinCondition(position[eh])
        evale -= tmpEv*evaluatorMul[eh]
        mainBd.append(tmpEv)

    evale -= checkWinCondition(mainBd)*5000
    evale += realEvaluateSquare(mainBd)*150
    return evale

def evaluatePos(pos, square):
    evaluation = 0
    pos[square] = ai
    points = [0.2, 0.17, 0.2, 0.17, 0.22, 0.17, 0.2, 0.17, 0.2]
    evaluation += points[square]
    # Prefer creating pairs
    a = -2
    if(pos[0] + pos[1] + pos[2]  == a or pos[3] + pos[4] + pos[5]  == a or pos[6] + pos[7] + pos[8]  == a or pos[0] + pos[3] + pos[6]  == a or pos[1] + pos[4] + pos[7]  == a or
        pos[2] + pos[5] + pos[8]  == a or pos[0] + pos[4] + pos[8]  == a or pos[2] + pos[4] + pos[6]  == a):
        evaluation += 1

    # Take victories
    a = -3
    if(pos[0] + pos[1] + pos[2]  == a or pos[3] + pos[4] + pos[5]  == a or pos[6] + pos[7] + pos[8]  == a or pos[0] + pos[3] + pos[6]  == a or pos[1] + pos[4] + pos[7]  == a or
        pos[2] + pos[5] + pos[8]  == a or pos[0] + pos[4] + pos[8]  == a or pos[2] + pos[4] + pos[6]  == a):
        evaluation += 5


    # Block a players turn if necessary
    pos[square] = player
    a = 3
    # player
    if(pos[0] + pos[1] + pos[2]  == a or pos[3] + pos[4] + pos[5]  == a or pos[6] + pos[7] + pos[8]  == a or pos[0] + pos[3] + pos[6]  == a or pos[1] + pos[4] + pos[7]  == a or
        pos[2] + pos[5] + pos[8]  == a or pos[0] + pos[4] + pos[8]  == a or pos[2] + pos[4] + pos[6]  == a):
        evaluation += 2
    pos[square] = ai
    evaluation -= checkWinCondition(pos)*15
    pos[square] = 0
    return evaluation


def miniMax(position, boardToPlayOn, depth, alpha, beta, maximize):
    # check if curstate is termination
    tmpPlay = -1
    calcEval = evaluateGame(position, boardToPlayOn)
    if(depth <= 0 or abs(calcEval) > 5000):
        return {"mE": calcEval, "tP": tmpPlay}

    #If the board to play on is -1, it means you can play on any board

    #The board to play on is win/lose
    if(boardToPlayOn != -1 and checkWinCondition(position[boardToPlayOn]) != 0):
        boardToPlayOn = -1

    #The board to play on is full(draw)
    if(boardToPlayOn != -1 and position[boardToPlayOn].count(0) == 0):
        boardToPlayOn = -1


    if(maximize): # maximizer turn
        maxEval = -math.inf
        for mm in range(9):
            if boardToPlayOn == -1:
                evalut = -math.inf
                for c in range(9):
                    if checkWinCondition(position[mm]) == 0:
                        if(position[mm][c] == 0):
                            position[mm][c] = ai
                            evalut = miniMax(position, c, depth - 1, alpha, beta, False)["mE"]
                            position[mm][c] = 0
                        if evalut > maxEval:
                            maxEval = evalut
                            tmpPlay = mm
                        alpha = max(alpha, evalut)
                if beta <= alpha:
                    break
            else:
                evalut = {"mE":None, "tP":None}
                if(position[boardToPlayOn][mm] == 0):
                    position[boardToPlayOn][mm] = ai
                    evalut = miniMax(position, mm, depth - 1, alpha, beta, False)
                    position[boardToPlayOn][mm] = 0
                    blop = evalut["mE"]
                    if(blop > maxEval):
                        maxEval = blop
                        tmpPlay = evalut["tP"]
                    alpha = max(alpha, blop)
                if(beta <= alpha):
                    break
        return { "mE": maxEval, "tP": tmpPlay}
    else: # minimizer turn
        minEval = math.inf
        for mm in range(9):
            if boardToPlayOn == -1:
                evalua = math.inf
                for c in range(9):
                    if checkWinCondition(position[mm]) == 0:
                        if (position[mm][c] == 0):
                            position[mm][c] = player
                            evalua = miniMax(position, c, depth - 1, alpha, beta, True)["mE"];
                            position[mm][c] = 0
                        if evalua < minEval:
                            minEval = evalua
                            tmpPlay = mm
                        beta = min(beta, evalua)
                if beta <= alpha:
                    break
            else:
                evalua = {"mE":None, "tP":None}
                if (position[boardToPlayOn][mm] == 0):
                    position[boardToPlayOn][mm] = player
                    evalua = miniMax(position, mm, depth - 1, alpha, beta, True)
                    position[boardToPlayOn][mm] = 0
                    blep = evalua["mE"]
                    if (blep < minEval):
                        minEval = blep
                        tmpPlay = evalua["tP"]
                    beta = min(beta, blep)
                if (beta <= alpha):
                    break
        return {"mE": minEval, "tP": tmpPlay}


def select_move(cur_state, remain_time):

    bestMove = -1
    bonus = [-math.inf, -math.inf, -math.inf, -math.inf, -math.inf, -math.inf, -math.inf, -math.inf, -math.inf]
    if (cur_state.previous_move != None):
        board[cur_state.previous_move.index_local_board][3 * cur_state.previous_move.x + cur_state.previous_move.y] = 1
    count = 0
    depth = 0
    # isMaximize = (cur_state.player_to_move == -1)
    #Count number of empty cells
    for i in range(9):
        if (checkWinCondition(board[i])):
            for c in range(9):
                if(board[i][c] == 0):
                    count+=1

    #Calculate the depth
    if (remain_time > 110):
        depth = min(DEPTV1, count)
    elif (remain_time > 100):
        depth = min(DEPTV2, count)
    else:
        depth = min(DEPTV3, count)


    # Find what board should play when can play any
    valid_moves = cur_state.get_valid_moves

    currentBoard = 0
    if(cur_state.free_move):
        currentBoard = miniMax(board, -1, depth, -math.inf, math.inf, True)["tP"]
    else:
        if cur_state.previous_move == None:
            currentBoard = -1
        else:
            currentBoard = cur_state.previous_move.x*3 + cur_state.previous_move.y

    #Find best move
    if(len(valid_moves) > 0):
        #bonus score by cell index
        for i in range(9):
            if board[currentBoard][i] == 0:
                bestMove = i
                break
        if bestMove != -1:
            for i in range(9):
                if (board[currentBoard][i] == 0):
                    bonus[i] = evaluatePos(board[currentBoard], i) * 45

            if (remain_time > 100):
                depth = min(DEPTV1, count)
            elif (remain_time > 90):
                depth = min(DEPTV2, count)
            else:
                depth = min(DEPTV3, count)


            for b in range(9):
                if(checkWinCondition(board[currentBoard]) == 0):
                    if (board[currentBoard][b] == 0):
                        board[currentBoard][b] = ai
                        savedMm = miniMax(board , b, depth, -math.inf, math.inf, False)
                        score2 = savedMm["mE"]
                        board[currentBoard][b] = 0
                        bonus[b] += score2

            for i in range(9):
                if(bonus[i] > bonus[bestMove]):
                    bestMove = i
        x = bestMove // 3
        y = bestMove % 3
        board[currentBoard][bestMove] = -1
        newMove = UltimateTTT_Move(currentBoard, x, y, cur_state.player_to_move)
    return newMove







