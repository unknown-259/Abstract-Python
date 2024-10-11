class Board:
      def __init__(self):
            # board is a list of cells that are represented 
            # by strings (" ", "O", and "X")
            # initially it is made of empty cells represented 
            # by " " strings
            self.sign = " "
            self.size = 3
            self.board = list(self.sign * self.size**2)
            # the winner's sign O or X
            self.winner = ""

      def get_size(self): 
             # optional, return the board size (an instance size)
             return self.size

      def get_winner(self):
            # return the winner's sign O or X (an instance winner)   
            return self.winner 

      def set(self, cell, sign):
            # mark the cell on the board with the sign X or O
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            index = valid_choices.index(cell)
            self.board[index] = sign
            
      def isempty(self, cell):
            # return True if the cell is empty (not marked with X or O)
            valid_choices = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
            index = valid_choices.index(cell)
            return self.board[index] == self.sign
                  
      def isdone(self):
            done = False
            # check all game terminating conditions, if one of them is present, assign the var done to True
            # depending on conditions assign the instance var winner to O or X
            if ' ' not in self.board:
                  done = True
                  self.winner = ''
            
            for i in range(0, 8, 3):
                  if self.board[i] == self.board[i+1] == self.board[i+2] != ' ':
                        done = True
                        self.winner = self.board[i]

            for i in range(3):
                  if self.board[i] == self.board[i+3] == self.board[i+6] != ' ':
                        done = True
                        self.winner = self.board[i]

            if self.board[0] == self.board[4] == self.board[8] != ' ':
                  done = True
                  self.winner = self.board[0]
            
            if self.board[2] == self.board[4] == self.board[6] != ' ':
                  done = True
                  self.winner = self.board[2]

            return done

      def show(self):
            # draw the board
            print('   A   B   C')
            print(' +---+---+---+')
            for i in range(0, 8, 3):
                  print(f'{i//3 + 1}| {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} |')
                  print(' +---+---+---+')