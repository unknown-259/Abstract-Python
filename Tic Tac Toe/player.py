import math
class Player:
      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X

      def get_sign(self):
            # return an instance sign
            return self.sign
      
      def get_name(self):
            # return an instance name
            return self.name
      
      def choose(self, board):
            # prompt the user to choose a cell
            # if the user enters a valid string and the cell on the board is empty, update the board
            # otherwise print a message that the input is wrong and rewrite the prompt
            # use the methods board.isempty(cell), and board.set(cell, sign)
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            cell = input(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:\n').upper()
            while True: 
                  try:
                        if board.isempty(cell) == True:
                              board.set(cell, self.sign)
                              break
                        else:
                              print('You did not choose correctly.')
                              cell = input(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:\n').upper()
                  except:
                        print('You did not choose correctly.')
                        cell = input(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:\n').upper()
                              
from random import choice
class AI(Player):
      def __init__(self, name, sign, board):
            super().__init__(name, sign)
            self.cells = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            self.board = board

      def get_sign(self):
            # return an instance sign
            return self.sign

      def get_name(self):
            # return an instance name
            return self.name
        
      def choose(self, board):
            cell = choice([x for x in self.cells if board.isempty(x)])
            board.set(cell, self.sign)
            print(f'{self.name}, X: Enter a cell [A-C][1-3]:')
            print(cell)

class MiniMax(AI):
      def __init__(self, name, sign, board):
            super().__init__(name, sign, board)
            self.cells = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            self.board = board

      def get_sign(self):
            # return an instance sign
            return self.sign

      def get_name(self):
            # return an instance name
            return self.name
      
      def choose(self, board):
            print(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:')
            cell = MiniMax.minimax(self, board, True, True)
            print(cell)
            board.set(cell, self.sign)

      def minimax(self, board, self_player, start):
            min = math.inf
            max = -math.inf

            # check the base conditions
            if board.isdone():
                  # self is a winner
                  if board.get_winner() == self.sign:
                        return 1
                  # is a tie
                  elif board.get_winner() == "":
                        return 0
                  # self is a looser (opponent is a winner)
                  else:
                        return -1
                        
            # make a move (choose a cell) recursively
            for cell in self.cells:
                  if board.isempty(cell):
                        if self_player:
                              board.set(cell, self.sign)
                              score = MiniMax.minimax(self, board, False, False) + 1
                              board.set(cell, ' ')
                              if score > max:
                                    max = score
                                    move = cell
                        else:
                              board.set(cell, 'X' if self.sign == 'O' else 'O')
                              score = MiniMax.minimax(self, board, True, False) + 1
                              board.set(cell, ' ')
                              if score < min:
                                    min = score
                                    move = cell  
         
            if start:
                  return move
            elif self_player:
                  return max
            else:
                  return min

# from random import choice  
class SmartAI(AI):
      def __init__(self, name, sign, board):
            super().__init__(name, sign, board)
            self.cells = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            self.board = board

      def get_sign(self):
            # return an instance sign
            return self.sign

      def get_name(self):
            # return an instance name
            return self.name

      def choose(self, board):
            print(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:')

            # chooses a cell randomly first
            cell = choice([x for x in self.cells if board.isempty(x)])
                  
            # winning move horizontally
            for i in range(0, 8, 3):
                  if board.board[i] == board.board[i+1] == 'O' and board.board[i+2] == ' ':
                        cell = self.cells[i+2]
                  elif board.board[i] == board.board[i+2] == 'O'and board.board[i+1] == ' ':
                        cell = self.cells[i+1]
                  elif board.board[i+1] == board.board[i+2] == 'O' and board.board[i] == ' ':
                        cell = self.cells[i]
            
            # winning move vertically
            for i in range(3):
                  if board.board[i] == board.board[i+3] == 'O' and board.board[i+6] == ' ':
                        cell = self.cells[i+6]
                  elif board.board[i] == board.board[i+6] == 'O' and board.board[i+3] == ' ':
                        cell = self.cells[i+3]
                  elif board.board[i+3] == board.board[i+6] == 'O' and board.board[i] == ' ':
                        cell = self.cells[i]

            # winning move diagonally
            if board.board[0] == board.board[4] == 'O' and board.board[8] == ' ':
                  cell = self.cells[8]
            elif board.board[0] == board.board[8] == 'O' and board.board[4] == ' ':
                  cell = self.cells[4]
            elif board.board[4] == board.board[8] == 'O' and board.board[0] == ' ':
                  cell = self.cells[0]
                  
            # winning move diagonally
            if board.board[2] == board.board[4] == 'O' and board.board[6] == ' ':
                  cell = self.cells[6]
            elif board.board[2] == board.board[6] == 'O' and board.board[4] == ' ':
                  cell = self.cells[4]
            if board.board[4] == board.board[6] == 'O' and board.board[2] == ' ':
                  cell = self.cells[2]

            # block possible wins horizontally
            for i in range(0, 8, 3):
                  if board.board[i] == board.board[i+1] == 'X' and board.board[i+2] == ' ':
                        cell = self.cells[i+2]
                  elif board.board[i] == board.board[i+2] == 'X' and board.board[i+1] == ' ':
                        cell = self.cells[i+1]
                  elif board.board[i+1] == board.board[i+2] == 'X' and board.board[i] == ' ':
                        cell = self.cells[i]
            
            # block possible wins vertically
            for i in range(3):
                  if board.board[i] == board.board[i+3] == 'X' and board.board[i+6] == ' ':
                        cell = self.cells[i+6]
                  elif board.board[i] == board.board[i+6] == 'X' and board.board[i+3] == ' ':
                        cell = self.cells[i+3]
                  elif board.board[i+3] == board.board[i+6] == 'X' and board.board[i] == ' ':
                        cell = self.cells[i]

            # block possible wins diagonally
            if board.board[0] == board.board[4] == 'X' and board.board[8] == ' ':
                  cell = self.cells[8]
            elif board.board[0] == board.board[8] == 'X' and board.board[4] == ' ':
                  cell = self.cells[4]
            elif board.board[4] == board.board[8] == 'X' and board.board[0] == ' ':
                  cell = self.cells[0]
                  
            # block possible wins diagonally
            if board.board[2] == board.board[4] == 'X' and board.board[6] == ' ':
                  cell = self.cells[6]
            elif board.board[2] == board.board[6] == 'X' and board.board[4] == ' ':
                  cell = self.cells[4]
            elif board.board[4] == board.board[6] == 'X' and board.board[2] == ' ':
                  cell = self.cells[2]

            print(cell)
            board.set(cell, self.sign)
