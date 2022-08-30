# PA3: Chess
#Elias Rosenberg
#CS76
#21F
#Professor Quattrini Li
#October 11, 2021

# Introduction: 
In this lab we were tasked with implementing the minimax algortithm to reccomend the next best chess move against an AI player, and to implement variations on the algorithm: AlphaBeta pruning, and Icrement Depth search. Minimax is an algorithm built to deal with two players in a fully visible game space. Chess is good for this, as all the pieces are known to both players, so every piece left on the board can be taken into account when deciding a next move. Chess is a 'zero-sum' game, meaning that when you add the scores of each player up (-1 for the minimizing player, and 1 for the maximizing player) you should get zero. My program uses positive and negative infinity, but the values are arbitrary as long as they are consistent. 

# Description: 
Minimax is a recursive algortihm that takes into account the best possible actions of two players called the Maximizing Player and the Minimizing Player. The Maximizing Player is trying to get the highest score it can, and the Minimizing Player is trying to get the lowest. The trick is that in the search tree, the Minimizing Player often gets to choose the lowest value first, meaning the maximizing player is stuck picking the highest of the lowest values presented. It can also go the other way around, depending on how the search tree is initially setup. Each leaf node is given a utility value, which are the values each player is trying to get the highest, or lowest of. Minimax also makes use of a terminal_state() method that returns the game space when a player has won the game, or the search depth limit has been reached and we hit a stalemate before finding a solution.  

In this implementation for chess, we have a list of legal moves given from all the pieces that remain on the board. We can run minimax on each move to get its utility value (calculated by considering all the White pieces minus the Black pieces, and multilpying those values by the value weights of each chess piece). The maximizing player will chose the move with the highest utility, and the minimizing player the lowest. In this context the Maximizing player is White, and the Minimizing player is Black, but again these attributions are arbitrary and can be changed for any search problem using Minimax. 

The other two algorithms, Alpha-Beta Pruning (ABP) and Iterative Depth Search (IDS) were slight variations on minimax. ABP allows the algorithm to cut away nearly half of any given search tree by storing the best overall moves of any branch for the Max and Min players in the alpha and beta values respectively. If a better move wont be found on a given branch, then that branch can be pruned away without having to look at every one of its leaf nodes. This basically halved the runtime of my Minimax algorithm, which is really cool. IDS is concerned with returning the best move at a given depth instead of returning a winning board for one player. It is similar to ABP, in that it stores the overall best move at every depth. The difference here is that IDS rebuilds the tree and explores to a depth + 1 of the previous depth to see if there is an even better move. For 'i' in the range between depth 0 and the given max_depth, run minimax to get the best move at that depth. If the move at that depth is better than at the previous depth, replace it. Return the best move once all depths have been explored. 

I didn't have to make that many design choices with my code. The chess module for python is really robust, and already had most of the helper methods needed to get this algortihm to run on a game of chess. This video on the minimax algorithm https://www.youtube.com/watch?v=l-hh51ncgDI&t=541s was amazingly helpful, and gave a side explanation in python syntax how minimax broadly functions. I attribute the structure of most of my code to this video, and I'm sure many others in the class have done the same. Between this general structure, and the pseudocode in the textbook, there weren't many design choices for me to make. I guess calculating the utility values of any board state took some thinking. I was getting the weirdest values from just subtracting the pieces away, and then remembered that different chess pieces have different values!

I made the IDS algorithm its own class, which was entirely unecessary, but was nice for ease of use in test_chess.py. I tried adding IDS as a method to my minimax class, but there was something about the way I structured my parameters where I just couldn't get it to run properly when called from the player object in test_chess.py. Most of the code is just variations on the MinimaxAI class. 

## Evaluation

The algorithms do actually work. Minimax consistently gets to a solution at approximately 80 calls, and hovers around that number–give or take 20 turns–when the list of moves is randomized to add some variety. As expected, ABP runs in half the time, taking between 40-60 moves. IDS just returns the best move at a given depth, so it doesn't take that long to process. 

# Discussion Questions
 1)  Every time the depth is increased on minimax, another approximately 10-15 calls are added, and this number increases exponentially at every new depth. At depth 1, there are 37 calls. At depths 2 there were 51, at depth 3 there were 75. As each new depth adds more nodes to be explored, it makes complete sense that the number of calls on minimax is also increasing to get the scores of each of those nodes. 

2) The evaluation function, for me, was the hardest part of the lab to figure out. Once I really read the module description carefully, however, it wasn't that bad. Each state of the board is given a value based on the pieces of either side remaining. To get a value of a board, you must go through all the White pieces remaining and then subtract them from the Black pieces remaining. You then multiply those values by the weights of each value of a piece. Pawns are worth 1, Knights and Bishops 3, Rooks are 5, the Queen is 9, and the King is worth 200. The value returned does not change with the depth of the search, because the last move is always just the state of the board in checkmate, which is the same at every depth. Typically the Minimax algortihm crushses the RandomAI on every depth, so the score returned is always around 35 (the king isn't captured in checkmate).

3) Works as well as I hoped it would, cutting the runtimes in half. If Minimax at depth 2 takes 80 calls, alphabeta only requires 40. The moves between both algorithms in the early game are pretty much the same. Once the RandomAI is down to a few pieces is where alphabeta really shines, because it doesn't have to explore every single option to win, but just the best ones. IDS gets really wonky after a depth of 4, and the pieces of the board swithc to mostly white for some reason, skewing the values, which basically breaks the algorithm. I wish I had more time to debug it. 

4) At depth 1 the best_move returned has these results:
best move is: f8g7
best score is: 17

At depth 2 we get these results: 
best move is: e2f1b
best score is: 65

There score is much higher, which means the move to get there is better. After this depth the checkmate is usually reached, so the score is in the 200s, which is as good as it can get. 
