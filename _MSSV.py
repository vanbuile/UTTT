import numpy as np
import math
ai = -1
player = 1

def checkWinCondition(block):
    map = np.asarray(block).ravel()
    a = 1
    if (map[0] + map[1] + map[2]  == a * 3 or map[3] + map[4] + map[5]  == a * 3 or map[6] + map[7] + map[8]  == a * 3 or map[0] + map[3] + map[6]  == a * 3 or map[1] + map[4] + map[7]  == a * 3 or
        map[2] + map[5] + map[8]  == a * 3 or map[0] + map[4] + map[8]  == a * 3 or map[2] + map[4] + map[6]  == a * 3):
        return a
    a = -1
    if (map[0] + map[1] + map[2]  == a * 3 or map[3] + map[4] + map[5]  == a * 3 or map[6] + map[7] + map[8]  == a * 3 or map[0] + map[3] + map[6]  == a * 3 or map[1] + map[4] + map[7]  == a * 3 or
        map[2] + map[5] + map[8]  == a * 3 or map[0] + map[4] + map[8]  == a * 3 or map[2] + map[4] + map[6]  == a * 3):
        return a
    return 0

def realEvaluateSquare(block):
    pos =  np.asarray(block).ravel()
    evaluation = 0
    points = [0.2, 0.17, 0.2, 0.17, 0.22, 0.17, 0.2, 0.17, 0.2]
    for bw in pos:
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
    a = -2;
    if(pos[0] + pos[1] + pos[2] == a or pos[3] + pos[4] + pos[5] == a or pos[6] + pos[7] + pos[8] == a):
        evaluation += 6

    if(pos[0] + pos[3] + pos[6] == a or pos[1] + pos[4] + pos[7] == a or pos[2] + pos[5] + pos[8] == a):
        evaluation += 6

    if(pos[0] + pos[4] + pos[8] == a or pos[2] + pos[4] + pos[6] == a):
        evaluation += 7

    a = 1;
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

def evaluateGame(cur_state):
    eval = 0
    mainBd = []
    evaluatorMul = [1.4, 1, 1.4, 1, 1.75, 1, 1.4, 1, 1.4]
    index_local_board = cur_state.previous_move.x * 3 + cur_state.previous_move.y
    for eh in range(9):
        eval += realEvaluateSquare(cur_state.blocks[eh])*1.5*evaluatorMul[eh];
        if(eh == index_local_board):
            eval += realEvaluateSquare(cur_state.blocks[eh])*evaluatorMul[eh];
        tmpEv = checkWinCondition(cur_state.blocks[eh])
        eval -= tmpEv * evaluatorMul[eh]
        mainBd.append(tmpEv)

    eval -= checkWinCondition(mainBd)*5000
    eval += realEvaluateSquare(mainBd)*150
    return eval

def evaluatePos(block, r, c, player_to_move):

    pos = np.asarray(block).ravel() # convert to array
    evaluation = 0

    square = 3*r+c

    pos[square] = player_to_move
    points = [0.2, 0.17, 0.2, 0.17, 0.22, 0.17, 0.2, 0.17, 0.2];

    evaluation+=points[square]

    # Prefer creating pairs
    a = 2 * player_to_move
    if(pos[0] + pos[1] + pos[2]  == a or pos[3] + pos[4] + pos[5]  == a or pos[6] + pos[7] + pos[8]  == a or pos[0] + pos[3] + pos[6]  == a or pos[1] + pos[4] + pos[7]  == a or
        pos[2] + pos[5] + pos[8]  == a or pos[0] + pos[4] + pos[8]  == a or pos[2] + pos[4] + pos[6]  == a):
        evaluation += 1

    # Take victories
    a = 3 * player_to_move
    if(pos[0] + pos[1] + pos[2]  == a or pos[3] + pos[4] + pos[5]  == a or pos[6] + pos[7] + pos[8]  == a or pos[0] + pos[3] + pos[6]  == a or pos[1] + pos[4] + pos[7]  == a or
        pos[2] + pos[5] + pos[8]  == a or pos[0] + pos[4] + pos[8]  == a or pos[2] + pos[4] + pos[6]  == a):
        evaluation += 5


    # Block a players turn if necessary
    a = -3 * player_to_move
    pos[square] = -player_to_move  # player
    if(pos[0] + pos[1] + pos[2]  == a or pos[3] + pos[4] + pos[5]  == a or pos[6] + pos[7] + pos[8]  == a or pos[0] + pos[3] + pos[6]  == a or pos[1] + pos[4] + pos[7]  == a or
        pos[2] + pos[5] + pos[8]  == a or pos[0] + pos[4] + pos[8]  == a or pos[2] + pos[4] + pos[6]  == a):
        evaluation += 2
    pos[square] = player_to_move
    evaluation += player_to_move * checkWinCondition(pos)*15
    return evaluation


def miniMax(cur_state,boardToPlayOn, depth, alpha, beta, maximize):
    # check if curstate is termination
    tmpPlay = -1
    calcEval = evaluateGame(cur_state)
    if(depth <= 0 or abs(calcEval) > 5000):
        return {"mE": calcEval, "tP": tmpPlay}

    #If the board to play on is -1, it means you can play on any board

    #The board to play on is win/lose
    # if(boardToPlayOn != -1 and checkWinCondition(cur_state.blocks[boardToPlayOn]) != 0):
    #     boardToPlayOn = -1

    #The board to play on is full(draw)
    if(boardToPlayOn != -1 ):
        local_board = cur_state.blocks[boardToPlayOn]
        indices = np.where(local_board == 0)
        if(len(indices[0]) == 0):
            boardToPlayOn = -1


    if(maximize): # maximizer turn
        maxEval = -math.inf
        if boardToPlayOn == -1:
            for mm in range(9):
                evalut = -math.inf
                for r in range(3):
                    for c in range(3):
                        if checkWinCondition(cur_state.blocks[mm]) == 0:
                            if(cur_state.blocks[mm][r][c] == 0):
                                cur_state.blocks[mm][r][c] = -1
                                evalut = miniMax(cur_state, 3*r + c, depth - 1, alpha, beta, False)["mE"];
                                cur_state.blocks[mm][r][c] = 0
                            if evalut > maxEval:
                                maxEval = evalut
                                tmpPlay = mm
                            alpha = max(alpha, evalut)
                if beta <= alpha:
                    return {"mE": maxEval, "tP": tmpPlay}
        else:
            for r in range(3):
                for c in range(3):
                    if(cur_state.blocks[boardToPlayOn][r][c] == 0):
                        cur_state.blocks[boardToPlayOn][r][c] = -1
                        evalut = miniMax(cur_state, 3*r + c, depth - 1, alpha, beta, False)
                        cur_state.blocks[boardToPlayOn][r][c] = 0
                    blop = evalut["mE"]
                    if(blop > maxEval):
                        maxEval = blop
                        tmpPlay = evalut["tP"]
                    alpha = max(alpha, blop)
                    if(beta <= alpha):
                        return { "mE": maxEval, "tP": tmpPlay}
    else: # minimizer turn
        minEval = math.inf
        if boardToPlayOn == -1:
            for mm in range(9):
                evalua = math.inf
                for r in range(3):
                    for c in range(3):
                        if checkWinCondition(cur_state.blocks[mm]) == 0:
                            if (cur_state.blocks[mm][r][c] == 0):
                                cur_state.blocks[mm][r][c] = 1
                                evalua = miniMax(cur_state, 3 * r + c, depth - 1, alpha, beta, True)["mE"];
                                cur_state.blocks[mm][r][c] = 0
                            if evalua < minEval:
                                minEval = evalua
                                tmpPlay = mm
                            beta = min(beta, evalua)
                if beta <= alpha:
                    return {"mE": minEval, "tP": tmpPlay}
        else:
            for r in range(3):
                for c in range(3):
                    if (cur_state.blocks[boardToPlayOn][r][c] == 0):
                        cur_state.blocks[boardToPlayOn][r][c] = 11
                        evalua = miniMax(cur_state, 3 * r + c, depth - 1, alpha, beta, True)
                        cur_state.blocks[boardToPlayOn][r][c] = 0
                    blep = evalua["mE"]
                    if (blep < minEval):
                        minEval = blep
                        tmpPlay = evalua["tP"]
                    beta = min(beta, blep)
                    if (beta <= alpha):
                        return {"mE": minEval, "tP": tmpPlay}


def select_move(cur_state, remain_time):
    # count empty cell that block have not win
    count = 0
    alpha = -math.inf
    beta = math.inf
    depth = 0
    isMaximize = (cur_state.player_to_move == 1)


    #Count number of empty cells
    for i in range(9):
        for r in range(3):
            for c in range(3):
                if(cur_state.blocks[i][r, c] == 0):
                    count+=1

    #Calculate the depth
    if (remain_time > 110):
        depth = min(4, count)
    elif (remain_time > 100):
        depth = min(5, count)
    else:
        depth = min(6, count)


    # Find what board should play when can play any
    valid_moves = cur_state.get_valid_moves()

    currentBoard = 0
    if(cur_state.free_move):
        currentBoard = miniMax(cur_state, -1, depth, alpha, beta, isMaximize)["tP"]
    else:
        currentBoard = cur_state.previous_move.x*3 + cur_state.previous_move.y

    #Find best move
    bestMove = None
    bonus = [-math.inf, -math.inf, -math.inf, -math.inf, -math.inf, -math.inf, -math.inf, -math.inf, -math.inf]
    if(valid_moves.length > 0):
        #bonus score by cell index
        if(cur_state.global_cells[currentBoard] != 0):
            for a in range(9):
                bonus[a] = 0
        else:
            for r in range(3):
                for c in range(3):
                    if (cur_state.blocks[currentBoard][r, c] == 0):
                        score = evaluatePos(cur_state.blocks[currentBoard], r, c, cur_state.player_to_move) * 45
                        bonus[3*r + c] = score

        if (remain_time > 100):
            depth = min(5, count)
        elif (remain_time > 90):
            depth = min(6, count)
        else:
            depth = min(7, count)

        bestScore = -math.inf
        for move in valid_moves:
            if move.index_local_board == currentBoard:
                cur_state.blocks[currentBoard][move.x, move.y] = move.value
                score = miniMax(cur_state, currentBoard, depth, alpha, beta, isMaximize)
                cur_state.blocks[currentBoard][move.x, move.y] = move.value
                if score + bonus[move.x*3 + move.y] > bestScore:
                    bestScore = score + bonus[move.x*3 + move.y]
                    bestMove = move

    return bestMove







