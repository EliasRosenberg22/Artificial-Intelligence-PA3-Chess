# pip3 install python-chess

#Author: Elias Rosenberg
#Date: October 11, 2021
#Purpose: Run test cases on the three different AI algorithms written to play the optimal moves for chess. The three AI are
#MinimaxAI, AlphaBetaAI, and Iterative_DeepeningAI (aswell as the RandomAI that comes with the give code)

import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from Iterative_Deepening import Iterative_DeepeningAI
from ChessGame import ChessGame


import sys


#player1 = MinimaxAI(2, True)
#player2 = RandomAI()

#player1 = AlphaBetaAI(4, True)
#player2 = RandomAI()

player1 = Iterative_DeepeningAI(0, True)
player2 = RandomAI()

game = ChessGame(player1, player2)


while not game.is_game_over():
    print(game)
    game.make_move()

print(hash(str(game.board)))



