# assignment: programming assignment 4
# author: Nathan Tran
# date: 05/29/23
# file: fifteen.py is a program that allows users to swap tiles to put them in order
# input: number that wants to be swapped with empty
# output: table with numbers

import numpy as np
from random import choice

class Fifteen:
    
    def __init__(self, size = 4):
        self.size = size
        self.tiles = np.array([i for i in range(1,size**2)] + [0])
        # indicies of adjecent
        self.adj = [[1,4], [0,2,5], [1,3,6], [2,7], [0,5,8], [1,4,6,9], [2,5,7,10], 
                    [3,6,11], [4,9,12], [5,8,10,13], [6,9,11,14], [7,10,15], 
                    [8,13], [12,9,14], [10,13,15], [11,14]]

    def update(self, move):
        try:
            dup = self.tiles.tolist()
            move_index = dup.index(move)
            zero_index = dup.index(0)
            if self.is_valid_move(move):
                self.tiles[move_index] = 0
                self.tiles[zero_index] = move
        except:
            None

    def shuffle(self, steps=30):
        index = np.where(self.tiles == 0)[0][0]
        for i in range(steps):
            move_index = choice (self.adj[index])
            self.tiles[index],self.tiles[move_index] = self.tiles[move_index],self.tiles[index]
            index = move_index
        
        
    def is_valid_move(self, move):
        dup = self.tiles.tolist()
        index = dup.index(0)
        for i in self.adj[index]:
            if move == self.tiles[i]:
                return True
        return False

    def is_solved(self):
        res = self.tiles == np.array([i for i in range(1, self.size**2)] + [0])
        return False not in res

    def draw(self):
        dup = self.tiles.tolist()
        
        for i in range(len(dup)):
            if int(dup[i]) == 0:
                dup[i] = '  '
        print(' +---+---+---+---+')
        for i in range(0, 15, 4):
            print(f' | {dup[i]}', end = '') if len(str(dup[i])) == 1 else print(f' |{dup[i]}', end = '')
            print(f' | {dup[i+1]}', end = '') if len(str(dup[i+1])) == 1 else print(f' |{dup[i+1]}', end = '')
            print(f' | {dup[i+2]}', end = '') if len(str(dup[i+2])) == 1 else print(f' |{dup[i+2]}', end = '')
            print(f' | {dup[i+3]} |') if len(str(dup[i+3])) == 1 else print(f' |{dup[i+3]} |')
            print(' +---+---+---+---+')
    
    def __str__(self):
        string = ''
        dup = self.tiles.tolist()
        
        for i in range(len(dup)):
            if int(dup[i]) == 0:
                dup[i] = '  '
        
        for i in range(0, 15, 4):
            if len(str(dup[i])) == 1:
                string += f' {dup[i]} ' 
            else: 
                string += f'{str(dup[i])} '
            if len(str(dup[i+1])) == 1:
                string += f' {dup[i+1]} ' 
            else: 
                string += f'{str(dup[i+1])} '
            if len(str(dup[i+2])) == 1:
                string += f' {dup[i+2]} ' 
            else: 
                string += f'{str(dup[i+2])} '
            if len(str(dup[i+3])) == 1:
                string += f' {dup[i+3]} ' 
            else: 
                string += f'{str(dup[i+3])} '
            string += '\n'
        return string
        

if __name__ == '__main__':

    game = Fifteen()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False
    

    # game = Fifteen()
    # game.shuffle()
    # game.draw()
    # while True:
    #     move = input('Enter your move or q to quit: ')
    #     if move == 'q':
    #         break
    #     elif not move.isdigit():
    #         continue
    #     game.update(int(move))
    #     game.draw()
    #     if game.is_solved():
    #         break
    # print('Game over!')