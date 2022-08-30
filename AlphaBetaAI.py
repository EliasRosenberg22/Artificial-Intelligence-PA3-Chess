#Author: Elias Rosenberg
#Date: October 11, 2021
#Purpose: Uses AlphaBeta pruning in conjuction with minimax algorithm to suggest next best move in a chess game against an AI. Almost all the code is the same as in MinimaxAI.py. I will add unique comments where parts of this code differ.


import math
import random
from random import shuffle
import chess
from math import inf


class AlphaBetaAI():

    def __init__(self, depth, player):
        self.currDepth = 0
        self.currentPlayer = player  # boolean of which player is moving. White is True, Black is False
        self.max_depth = depth
        self.alpha = -math.inf
        self.beta = math.inf
        self.calls = 0

    def choose_move(self, board):  # best possible move out of list of legal states given minimax value (result)
        maximizingPlayer = board.turn  # turn we are on
        score, move = self.alpha_beta(board, self.max_depth, self.alpha, self.beta, maximizingPlayer) #this minimax takes alpha and beta to prune away moves that aren't worth looking at because their scores are either too low or too high
        self.calls += 1
        return move

    def terminal_test(self, board, currDepth):  # game is over if we find the solution or we have reached the max depth
        return board.is_game_over() or currDepth == 0

    def evaluate_move(self, board, maximizingPlayer):
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

    def utility_function(self, board):
        # 3 scenarios, if it's a checkmate, stalemate or neither
        if board.is_checkmate():
            print("number of calls: " + str(self.calls))
            if self.currentPlayer == chess.WHITE:
                return 1
            else:
                return -1
        elif board.is_stalemate():
            return 0
        else:
            # print(self.currentPlayer)
            return self.evaluate_move(board, self.currentPlayer)

    def alpha_beta(self, board, max_depth, alpha, beta, maximizingPlayer):
        if self.terminal_test(board, max_depth):  # if cutoff test is met, evaluate this board and return the value
            return self.utility_function(board), None

        else:
            if maximizingPlayer == self.currentPlayer:  # if we are on the maximizingPlayer (white)
                maxEval = -math.inf
                best_move = None
                moves = list(board.legal_moves)
                #random.shuffle(moves)
                for move in moves:
                    board.push(move)
                    eval = self.alpha_beta(board, max_depth - 1, alpha, beta, False)[0]
                    board.pop()
                    if eval > maxEval:
                        best_move = move
                        maxEval = eval
                    if eval > alpha: #comparing the current best move to alpha, which is the overall best move for maximizing player
                        alpha = eval
                    if beta <= alpha:
                        break
                return maxEval, best_move

            else:
                minEval = math.inf
                best_move = None
                moves = list(board.legal_moves)
                #random.shuffle(moves)
                for move in moves:
                    board.push(move)
                    eval = self.alpha_beta(board, max_depth - 1, alpha, beta, True)[0]
                    board.pop()
                    if eval < minEval:
                        best_move = move
                        minEval = eval

                    if eval < beta: #comparing the current best move to beta, which is the overall best move for minimizing player
                        beta = eval
                    if beta <= alpha:
                        break
                return minEval, best_move
