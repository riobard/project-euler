def sudoku(board):
    def available_options(pos, board):
        x,y = divmod(pos, 9)
        row = board[x*9:(x+1)*9]
        col = board[y::9]
        start   = x//3*3*9 + y//3*3
        box     = board[start:start+3] + board[start+9:start+9+3] + board[start+2*9:start+2*9+3]
        return set('123456789') - set(row) - set(col) - set(box)

    for pos in range(0, 9*9):
        if board[pos]=='0': # empty slot to fill
            for option in available_options(pos, board):
                new_board   = board[:pos] + option + board[pos+1:]
                #print 'pos %2d, new board = %s' % (pos, new_board)
                rs  = sudoku(new_board)
                if rs != 'failure': return rs
            return 'failure'    # no available options. previous steps must be wrong
    return board    # no empty slot left and no failure. we are gold. 



# usage:
#b1  = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
#s1  = '483921657967345821251876493548132976729564138136798245372689514814253769695417382'
#t1  = sudoku(b1)
#assert(t1 == s1)


lines   = [line.strip() for line in open('sudoku.txt')]
rs  = 0
for i in range(0, 50):
    board   = ''.join(lines[i*10+1:i*10+10])
    solution= sudoku(board)
    #print 'Board #%2d, solution = %s' % (i+1, solution)
    rs  += int(solution[:3])
print rs
