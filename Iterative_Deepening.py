#Author: Elias Rosenberg
#Date: October 11, 2021
#Purpose: Uses iterative deepening in conjunction with minimax algorithm to suggest next best move in a chess game against an AI. Almost all the code is the same as in MinimaxAI.py. I will add unique comments where parts of this code differ.

import math
import chess
import random
from random import shuffle


class Iterative_DeepeningAI():
    def __init__(self, depth, player):
        self.max_depth = depth  # max depth of the search
        self.currDepth = 0 #current depth of the search
        self.currentPlayer = player  # boolean of which player is moving. White is True, Black is False
        self.calls = 0 #tracking the number of recursive calls to minimax

    def choose_move(self, board):  # iterative deepening changes how we choose the next best move, by only returning the best move at this depth.
        best_score = -math.inf
        best_move = None
        maximizingPlayer = board.turn
        for depth in range(0, self.max_depth + 1):  # for each depth of the search, choose the best move and return it
            moves = list(board.legal_moves)
            # random.shuffle(moves)
            for move in moves:
                board.push(move)
                score = self.minimax(board, move, self.max_depth, not maximizingPlayer)[0]
                print(self.max_depth)
                board.pop()
                if score > best_score:
                    best_score = score
                    best_move = move

        print("best move is: " + str(best_move))
        print("best score is: " + str(best_score))
        return best_move

    def terminal_test(self, board, currDepth):  # game is over if we find the solution or we have reached the max depth
        return board.is_game_over() or currDepth == 0

    def evaluate_move(self, board, maximizingPlayer): #board value. Takes the number of White pieces and subtracts the number of Black ones, multiplied by chess piece weight values.
        maxP, minP = len(board.pieces(chess.PAWN, maximizingPlayer)), len(
            board.pieces(chess.PAWN, not maximizingPlayer))
        maxN, minN = len(board.pieces(chess.KNIGHT, maximizingPlayer)), len(
            board.pieces(chess.KNIGHT, not maximizingPlayer))
        maxB, minB = len(board.pieces(chess.BISHOP, maximizingPlayer)), len(
            board.pieces(chess.BISHOP, not maximizingPlayer))
        maxQ, minQ = len(board.pieces(chess.QUEEN, maximizingPlayer)), len(
            board.pieces(chess.QUEEN, not maximizingPlayer))
        maxR, minR = len(board.pieces(chess.ROOK, maximizingPlayer)), len(
            board.pieces(chess.ROOK, not maximizingPlayer))
        maxK, minK = len(board.pieces(chess.KING, maximizingPlayer)), len(
            board.pieces(chess.KING, not maximizingPlayer))

        val = ((maxP - minP) + (3 * (maxN - minN)) + (3 * (maxB - minB)) + (9 * (maxQ - minQ)) + (5 * (
                maxR - minR)) + (200 * (maxK - minK)))

        return val

    def utility_function(self, board): #returns the utility of end states of the game.
        # 3 scenarios, if it's a checkmate, stalemate or neither
        if board.is_checkmate():
            if self.currentPlayer == chess.WHITE and board.turn:
                return math.inf #since White is maximizing, it returns infinity
            else:
                return -math.inf #Black is minizing, so it returns negative infinity
        elif board.is_stalemate():
            return 0
        else:
            return self.evaluate_move(board, self.currentPlayer)


    def minimax(self, board, move, max_depth, maximizingPlayer):
        if self.terminal_test(board, max_depth):  # if the terminal state is met or the depth limit is reached
            return self.utility_function(board), None

        else:
            if maximizingPlayer == self.currentPlayer:  # if we are on the maximizingPlayer (white)
                maxEval = -math.inf #set the max value to negative infinity so it can be beaten.
                best_move = None
                moves = list(board.legal_moves) #possible moves.
                # random.shuffle(moves)
                for move in moves:
                    board.push(move) #add the move to the board
                    eval = self.minimax(board, move, max_depth - 1, False)[0] #get the  minimax score of this move
                    board.pop() #remove the move rom the board
                    if eval > maxEval: #if the new move is better than the last one
                        best_move = move #make it the best move at this depth
                        maxEval = eval
                return maxEval, best_move

            else:
                minEval = math.inf #all the same, but for the minizing player.
                best_move = None
                moves = list(board.legal_moves)
                # random.shuffle(moves)
                for move in moves:
                    board.push(move)
                    eval = self.minimax(board, move, max_depth - 1, True)[0]
                    board.pop()
                    if eval < minEval:
                        best_move = move
                        minEval = eval
                return minEval, best_move

