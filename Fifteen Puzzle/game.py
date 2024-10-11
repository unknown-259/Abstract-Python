# assignment: programming assignment 4
# author: Nathan Tran
# date: 05/29/23
# file: game.py is a program that allows users to click on desired tile to swap and put them in order
# input: clicks on interface
# output: swap tiles

from tkinter import *
import tkinter.font as font
from fifteen import Fifteen
from random import choice
          

def clickButton(board, row, col):
    global empty  
    
    # Get the clicked button's position and value
    pos = (row*4)+(col)
    value = labels[int(pos)].get()

    # Check if the clicked button is adjacent to the empty tile
    if board.is_valid_move(int(value)):
        board.update(int(value))
        labels[empty].set(value)
        labels[int(pos)].set('')

        empty = int(pos)

        # Change the background color of the clicked button to white
        gui.nametowidget(pos).configure(bg='white')

        if board.is_solved():
            print("Congratulations! Puzzle solved.")
    else:
        labels[empty].set('')

def shuffle(count, number):
    global empty

    if count < number:
        valid_moves = Fifteen.adj[empty]
        random_move = choice(valid_moves)
        
        # Swap the empty tile with the randomly chosen tile
        labels[empty].set(labels[random_move].get())
        labels[random_move].set(0)
        
        empty = random_move
        
        # Change the background color of the moved tile to white
        gui.nametowidget(empty).configure(bg='white')
        gui.after(300, lambda: shuffle(count+1, number))
    

def addButton(board, gui, value, pos):
    x = Button(gui, textvariable=value, name=str(pos), bg='red', fg='black',
font=font, height=2, width=5)
    x.configure(command = lambda btn=x: your_event_handler(board, btn, value, pos))
    return x

def your_event_handler(board, x, value, pos):
    labels[empty].set(value)
    gui.nametowidget(pos).configure(bg='white') 
    x = x.grid_info()
    clickButton(board, x['row'], x['column'])
    
if __name__ == '__main__':    

    # make tiles
    board = Fifteen()
    board.shuffle(50)
    empty = board.tiles.tolist().index(0)

    # make a window
    gui = Tk()
    gui.title("Fifteen")

    font = font.Font(family='Helveca', size='25', weight='bold')
    labels = []
    buttons = []

    dup = board.tiles.tolist()  
    for i in range(len(dup)):
        if int(dup[i]) == 0:
            dup[i] = ''

    for i in range(16):
        labels.append(StringVar())
        labels[i].set(dup[i])
        buttons.append(addButton(board, gui, labels[i], i))

    for i in range(4):
        for j in range(4):
            buttons[i*4+j].grid(row=i, column=j)

    # update the window
    gui.mainloop()
