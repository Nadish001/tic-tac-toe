class Game:
    def __init__(self):
        self.player = "X"
        self.position = [str(i) for i in range(9)]

    def board(self):
        print(f"\n {self.position[0]} | {self.position[1]} | {self.position[2]}")
        print("---|---|---")
        print(f" {self.position[3]} | {self.position[4]} | {self.position[5]}")
        print("---|---|---")
        print(f" {self.position[6]} | {self.position[7]} | {self.position[8]}")

    def move(self, pos):
        try:
            if pos < 0 or pos > 8:
                print("Cell position must be between 0 and 8.")
                return False
            if self.position[pos] == "X" or self.position[pos] == "O":
                print(f"cell {pos} is already filled")
                return False
            self.position[pos] = self.player
            return True
        except IndexError:
            print("Cell position must be between 0 and 8.")
            return False

    def check_winner(self):
        winning_lines = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),(0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)]

        for a, b, c in winning_lines:
            if self.position[a] == self.position[b] == self.position[c] and self.position[a] in ("X", "O"):
                return self.position[a]

        return None

    def cell_full(self):
        for cell in self.position:
            if cell != "X" and cell != "O":
                return False
        return True


game = Game()
print(".............Welcome to tic-tac-toe............")
print("let's begin the game..")
while True:
    game.board()


    cell = int(input(f"enter the cell position from 0-8 to place {game.player}:- "))

    if not game.move(cell):
        continue

    winner = game.check_winner()
    if winner:
        game.board()
        print(f"Player {winner} wins!")
        break

    if game.cell_full():
        game.board()
        print("It's a draw!")
        break

    if game.player == "X":
        game.player = "O"
    else:
        game.player = "X"
    print('-'*87)
