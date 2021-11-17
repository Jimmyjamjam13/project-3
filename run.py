from random import randint


scores = {"computer": 0, "player": 0}


class Board:
    
    """Will create player and computer board based on user input."""

    def __init__(self, name, size, ship_nums, type):
        self.name = name
        self.size = size
        self.ship_nums = ship_nums
        self.type = type
        self.board = [["." for x in range(size)] for y in range(size)]
        self.ships = []
        self.guesses = []

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def board_guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = 'X'

        if (x, y) in self.ships:
            self.board[x][y] = 'O'
            return f'{self.name}, you hit and sank a battleship!'
        else:
            return f"{self.name}, you've missed this time..."

    def add_ships(self, x, y, type='computer'):
        if len(self.ships) >= self.ship_nums:
            print('Too many ships')

        else:
            self.ships.append((x, y))
            if self.type == 'player':
                self.board[x][y] = '@'


def random_number(size):
    
    """Returns random integer between 0 and the length of the board
    chosen by the player."""

    return randint(0, (size) - 1)


def valid_coordinates(x, y, board):
    return [['O' for count in range(board)] for count in range(board)]


def populate_board(board):
    
    """Populates game board for each player, one for the user
    and one for the computer."""
    
    print(f"{board.name}'s board:\n")

    size = board.size

    while len(board.ships) != board.ship_nums:
        x = random_number(size)
        y = random_number(size)
        board.add_ships(x, y)

    board.print_board()
    print(board.ships)

