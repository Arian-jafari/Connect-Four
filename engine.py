from utils import evaluate_board
from game import ConnectFourGame, PLAYER, AI
ROW_COUNT, COLUMN_COUNT = 6,6
import numpy as np
from copy import copy


def minimax(game: ConnectFourGame, depth, maximizing_player):
    is_terminal = game.winning_move(PLAYER) or game.winning_move(AI) or len(game.get_valid_locations()) == 0
    if depth == 0 or is_terminal:
        if is_terminal:
            if game.winning_move(AI):
                return (None, 100000000000000)
            elif game.winning_move(PLAYER):
                return (None, -100000000000000)
            else:  
                return (None, 0)
        else: 
            return (None, evaluate_board(game, AI))
    
    board = game.board.copy()
    if maximizing_player:
        v = -float('inf')
        col = 0
        for c in game.get_valid_locations():
            game.board = board.copy()
            row = game.get_next_open_row(c)
            game.board[row, c] = AI
            _, v2 = minimax(game, depth-1, maximizing_player=False)
            if v2 > v:
                v = v2
                col = c
        game.board = board.copy()
        return col, v
    
    else:
        v = float('inf')
        col = 0
        for c in game.get_valid_locations():
            game.board = board.copy()
            row = game.get_next_open_row(c)
            game.board[row, c] = PLAYER
            _, v2 = minimax(game, depth-1, maximizing_player=True)
            if v2 < v:
                v = v2
                col = c
        game.board = board.copy()
        return col, v
            
        
def alpha_beta_pruning(game, depth, alpha, beta, maximizing_player):
    is_terminal = game.winning_move(PLAYER) or game.winning_move(AI) or len(game.get_valid_locations()) == 0
    if depth == 0 or is_terminal:
        if is_terminal:
            if game.winning_move(AI):
                return (None, 100000000000000)
            elif game.winning_move(PLAYER):
                return (None, -100000000000000)
            else:  
                return (None, 0)
        else: 
            return (None, evaluate_board(game, AI))
    
    board = game.board.copy()
    if maximizing_player:
        v = -float('inf')
        col = 0
        for c in game.get_valid_locations():
            game.board = board.copy()
            row = game.get_next_open_row(c)
            game.board[row, c] = AI
            _, v2 = alpha_beta_pruning(game, depth-1, alpha, beta, False)
            if v2 > v:
                v = v2
                col = c
                alpha = max(alpha, v)
            if v >= beta:
                game.board = board.copy()
                return col, v
                
        game.board = board.copy()
        return col, v
    
    else:
        v = float('inf')
        col = 0
        for c in game.get_valid_locations():
            game.board = board.copy()
            row = game.get_next_open_row(c)
            game.board[row, c] = PLAYER
            _, v2 = alpha_beta_pruning(game, depth-1, alpha, beta, True)
            if v2 < v:
                v = v2
                col = c
                beta = min(beta, v)
            if v <= alpha:
                game.board = board.copy()
                return col, v
                
        game.board = board.copy()
        return col, v


def expectimax(game, depth, maximizing_player):
    is_terminal = game.winning_move(PLAYER) or game.winning_move(AI) or len(game.get_valid_locations()) == 0
    if depth == 0 or is_terminal:
        if is_terminal:
            if game.winning_move(AI):
                return (None, 100000000000000)  
            elif game.winning_move(PLAYER):
                return (None, -100000000000000)  
            else:
                return (None, 0)  
        else:
            return (None, evaluate_board(game, AI))  
    
    
    board = game.board.copy()
    
    if maximizing_player:
        
        v = -float('inf')
        best_col = None
        for c in game.get_valid_locations():
            game.board = board.copy()
            row = game.get_next_open_row(c)
            game.board[row, c] = AI
            _, v2 = expectimax(game, depth - 1, False)
            if v2 > v:
                v = v2
                best_col = c
        game.board = board.copy()  
        return best_col, v
    
    else:
        
        v = 0
        valid_locations = game.get_valid_locations()
        num_valid_moves = len(valid_locations)
        for c in valid_locations:
            game.board = board.copy()
            row = game.get_next_open_row(c)
            game.board[row, c] = PLAYER
            _, v2 = expectimax(game, depth - 1, True)
            v += v2 / num_valid_moves  
        game.board = board.copy() 
        return None, v  