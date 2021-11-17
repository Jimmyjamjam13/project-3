from random import randint


scores = {"computer": 0, "player": 0}


class Board:
    
    """Will create player and computer board based on
    user input. """
    
    def __init__(self, name, size, ship_nums, type):
        self.name = name
        self.size = size
        self.ship_nums = ship_nums
        self.type = type
        self.board = [['|  ' for x in range(size)] for y in range(size)]
        self.ships = []
        self.guesses = []
    
    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def board_guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = 'X'

        if (x, y) in self.ships:
            self.board[x][y] = '| O'
            return f'{self.name}, you hit and sank a battleship!'
        else:
            return f"{self.name}, you've missed this time..."

    def add_ships(self, x, y, type='computer'):
        if len(self.ships) >= self.ship_nums:
            print('Too many ships')

        else:
            self.ships.append((x, y))
            if self.type == 'player':
                self.board[x][y] = '| @'
  

def random_number(size):
    """
    Returns random integer between 0 and the length of the board
    chosen by the player.
    """
    return randint(0, (size) - 1)


def valiidate_coordinates(x, y, board):
    while True:
        for board_guess in board.guess:
            if (x, y) == board_guess:
                print(f'{board.name}, you already guessed {(x, y)}.')
                print('Please try again.')
                return False

        break

    if (x, y) in board.ships:
        board.guesses.append((x, y))
        board.board[x][y] = '| O'
        print('A Battleship has been hit!')
    else:
        board.guesses.append((x, y))
        board.board[x][y] = '| X'
        print('Missile missed target...')


def game_setup(board):
    print(f"{board.name}'s board:\n")

    size = board.size

    while len(board.ships) != board.ship_nums:
        x = random_number(size)
        y = random_number(size)
        board.add_ships(x, y)

    board.print_board()
    print(board.ships)


def make_guesses(board):

    size = board.size

    while True:
        if board.type == 'computer':
            print("Computer's turn to guess")
            row_guess = random_number(board.size)
            col_guess = random_number(board.size)
        else:
            row_guess = input('Enter row num:\n')
            col_guess = input('Enter column num:\n')
            
        row = valiidate_coordinates(str(row_guess), 0, size)
        col = valiidate_coordinates(str(col_guess), 0, size)

        if row and col:
            break

    return [int(row_guess), int(col_guess)]


def play_game(computer_board, player_board):
    while True:
        game_setup(board)
        print('~' * 60)
        game_setup(board)

        player_guess = make_guesses(board)
        p_row = player_guess[0]
        p_col = player_guess[1]
        valiidate_coordinates(board, p_row, p_col)

        comp_guess = make_guesses(_board)
        c_row = comp_guess[0]
        c_col = comp_guess[1]
        valiidate_coordinates(board, c_row, c_col)

        if len(other_board.guesses) == ships:
            break

    print('finished game')


def new_game():

    """Runs new game every time user reloads
    or restarts the game"""

    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print("-" * 35)
    print(print('WELCOME TO BATTLESHIPS'))
    print(f" Board Size: {size}. Number of ships: {num_ships}")
    print("Top left hand corner is row 0, col 0")
    print("-" * 35)
    player_name = input("Please enter your name: \n")
    print("-" * 35)

    computer_board = Board(size, num_of_ships, "computer", type="computer")
    player_board = Board(size, num_of_ships, player_name, type="player")

    for _ in range(num_ships):
        game_setup(computer_board)
        game_setup(player_board)
    
    play_game(player_board, computer_board)


new_game()