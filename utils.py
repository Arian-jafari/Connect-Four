from game import PLAYER, AI

def evaluate_board(game, piece):
    
    total = 0
    rival = PLAYER if piece == AI else AI
    x = game.board.shape[0]
    y = game.board.shape[1]
    
    for r in range(x):
        for c in range(y - 2):
            temp = 0
            if game.board[r, c] == piece:
                temp += 1
            if game.board[r, c] == rival:
                temp -= 1
                
            if game.board[r, c+1] == piece:
                temp += 1    
            if game.board[r, c+1] == rival:
                temp -= 1
                
            if game.board[r, c+2] == piece:
                temp += 1
            if game.board[r, c+2] == rival:
                temp -= 1
            
            total += temp ** 3
                
                
    for r in range(x - 2):
        for c in range(y):
            temp = 0
            if game.board[r, c] == piece:
                temp += 1
            if game.board[r, c] == rival:
                temp -= 1
                
            if game.board[r+1, c] == piece:
                temp += 1    
            if game.board[r+1, c] == rival:
                temp -= 1
                
            if game.board[r+2, c] == piece:
                temp += 1
            if game.board[r+2, c] == rival:
                temp -= 1
                
            total += temp ** 3
    
    for r in range(x - 2):
        for c in range(y - 2):
            temp = 0
            if game.board[r, c] == piece:
                temp += 1
            if game.board[r, c] == rival:
                temp -= 1
                
            if game.board[r+1, c+1] == piece:
                temp += 1    
            if game.board[r+1, c+1] == rival:
                temp -= 1
                
            if game.board[r+2, c+2] == piece:
                temp += 1
            if game.board[r+2, c+2] == rival:
                temp -= 1
                
            total += temp ** 3
            
    for r in range(x - 2):
        for c in range(2, y):
            temp = 0
            if game.board[r, c] == piece:
                temp += 1
            if game.board[r, c] == rival:
                temp -= 1
                
            if game.board[r+1, c-1] == piece:
                temp += 1    
            if game.board[r+1, c-1] == rival:
                temp -= 1
                
            if game.board[r+2, c-2] == piece:
                temp += 1
            if game.board[r+2, c-2] == rival:
                temp -= 1
                
            total += temp ** 3
        
    return total
