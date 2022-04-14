class TicTacToe:
    """ A simple Tic-Tec-Toe game. """

    # define number of rows and columns of the game board
    ROWS = 3
    COLS = 3

    __slots__ = '_board', '_player'

    def __init__(self):
        """ Start a new game board. """
        self._board = [[' '] * self.COLS for _ in range(self.ROWS)]
        self._player = 'X'


    def mark(self, i, j):
        """ Put an X or O mark at position (i, j) for next player's turn. """
        if not (0 <= i < self.ROWS and 0 <= j < self.COLS):
            raise ValueError('Invalid board position')
        if self._board[i][j] != ' ':
            raise ValueError('Board position occupied')
        if self.winner() is not None:
            raise ValueError('Game is already completed')
        self._board[i][j] = self._player
        if self._player == 'X':
            self._player = 'O'
        else:
            self._player = 'X'

    
    def _is_win(self, mark):
        """ Check whether the board configuration is a win for the given player. """
        board = self._board
        return (
            # row 1
            mark == board[0][0] == board[0][1] == board[0][2] or
            # row 2
            mark == board[1][0] == board[1][1] == board[1][2] or
            # row 3
            mark == board[2][0] == board[2][1] == board[2][2] or
            # column 1
            mark == board[0][0] == board[1][0] == board[2][0] or
            # column 2
            mark == board[0][1] == board[1][1] == board[2][1] or
            # column 3
            mark == board[0][2] == board[1][2] == board[2][2] or
            # diagonal
            mark == board[0][0] == board[1][1] == board[2][2] or
            # reversed diagonal
            mark == board[0][2] == board[1][1] == board[2][0]
        )

    def winner(self):
        """ Return the mark of winning player, or None to indicate a tie. """
        for mark in 'XO':
            if self._is_win(mark):
                return mark
        return None

    
    def __str__(self):
        """ Return string representation of current game board. """
        rows = ['|'.join(self._board[r]) for r in range(3)]
        return '\n-----\n'.join(rows)

if __name__ == '__main__':
    # start game
    game = TicTacToe()
    # X moves           # Y moves
    game.mark(2, 2);    game.mark(0, 2)
    game.mark(1, 1);    game.mark(0, 0)
    game.mark(0, 1);    game.mark(2, 1)
    game.mark(1, 2);    game.mark(1, 0)
    game.mark(2, 0)
    # board configuration
    print(game)
    # who is winning player?
    winner = game.winner()
    if winner is None:
        print('Tie')
    else:
        print(winner, 'wins')
