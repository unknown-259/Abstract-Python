# assignment: programming assignment 5
# author: Nathan Tran
# date: 06/09/23
# file: skyland.py is a program where the user can play a game
# input: keys from the keyboard
# output: movement in the game

'''
You are trying to take your daily protein intake to build muscle. You must collect the egg and bring it back to your house to
get 6g of protein. Once you bring back the egg, the chicken will lay another egg. If you run into the dumbbell,
you will start doing bicep curls and get a bit bigger, but at a cost of losing 10g of protein. When you have reached your 
required protein intake for the day, you will have to bring the chicken back to get an additional 38g of protein.

Controls:
    arrows = move
    alt+L = restart
    space = pause
'''

from tkinter import *
import tkinter.font as font

WIDTH, HEIGHT = 600, 400
CLOCK_RATE = 15
START_X, START_Y = 20, 350
END_X, END_Y = 400, 350

class Skyland:
    # def __init__(self, canvas, weight):
    def __init__(self, canvas):
        self.canvas = canvas
        self.canvas.bind_all('<KeyPress-space>', self.pause)
        self.canvas.bind_all('<KeyPress-Alt_L>', self.restart)
        
        # self.reqProtein = round(weight * 0.8)
        self.reqProtein = 30
        self.protein = 0

        self.pause_bool = True
        self.land = Land(canvas)
        self.trophy = Trophy(canvas)
        self.avatar = Avatar(canvas)
        self.ai = Ai(canvas)
        self.chickenText = canvas.create_text(300, 245, text='', font=font.Font(family='Helveca', size='15', weight='bold'))
        self.text = canvas.create_text(280, 370, text=f'Required Daily Protein: {self.reqProtein}g   |   Your Protein: {self.protein} ', font=font.Font(family='Helveca', size='15', weight='bold'))
        self.dumbbell_bool = False
        self.chicken_bool = False
        self.update()

    def restart(self, event=None):
        self.reqProtein = 30
        self.protein = 0
        self.avatar.replace()
        self.canvas.delete(self.chickenText)
        self.canvas.itemconfig(self.text, text=f'Required Daily Protein: {self.reqProtein}g   |   Your Protein: {self.protein} ')
        self.dumbbell_bool = False
        self.chicken_bool = False
        self.canvas.delete(self.trophy.egg)
        self.trophy.egg = self.canvas.create_oval(552, START_Y-10, 558, START_Y, fill='white')
        for i in self.ai.chicken:
            self.canvas.delete(i)
        self.ai.chicken = self.ai.make_chicken()
        self.canvas.delete(self.land.leftWing)
        self.canvas.delete(self.land.rightWing)
        self.land.birdRight = 65
        self.land.birdLeft = 10
        self.land.leftWing = self.canvas.create_arc(self.land.birdLeft, 80, 40, 150, start=30, extent=120, style='arc', width=3)
        self.land.rightWing = self.canvas.create_arc(35, 80, self.land.birdRight, 150, start=30, extent=120, style='arc', width=3)
        
    def pause(self, event=None):
        if self.pause_bool == True:
            self.avatar.leftKey = self.canvas.unbind_all('<KeyPress-Left>')
            self.avatar.rightKey = self.canvas.unbind_all('<KeyPress-Right>')
            self.avatar.upKey = self.canvas.unbind_all('<KeyPress-Up>')
            self.avatar.downKey = self.canvas.unbind_all('<KeyPress-Down>')
            self.avatar.x = 0
            self.avatar.y = 0
            self.land.moveBird = self.land.update(bool = False)
            self.pause_bool = False
        else:
            self.avatar.leftKey = self.canvas.bind_all('<KeyPress-Left>', self.avatar.move)
            self.avatar.rightKey = self.canvas.bind_all('<KeyPress-Right>', self.avatar.move)
            self.avatar.upKey = self.canvas.bind_all('<KeyPress-Up>', self.avatar.move)
            self.avatar.downKey = self.canvas.bind_all('<KeyPress-Down>', self.avatar.move)
            self.land.moveBird = self.land.update(bool = True)
            self.pause_bool = True

    def update(self):
        for i in self.land.coop:
            self.avatar.hit_object(i)

        if self.avatar.hit_object(self.trophy.egg):
            self.trophy.egg_bool = True
            self.trophy.get_trophy()
        if self.avatar.hit_object(self.land.house) and self.trophy.egg_bool == True:
            self.trophy.egg_bool = False
            self.protein += 6
            self.canvas.itemconfig(self.text, text=f'Required Daily Protein: {self.reqProtein}g   |   Your Protein: {self.protein} ')
            self.trophy.replace()
        else:
            self.avatar.hit_object(self.land.house)

        for i in self.ai.dumbbell:
            dumbbell_bool = self.avatar.hit_object(i)
            if dumbbell_bool == True:
                self.avatar.leftKey = self.canvas.unbind_all('<KeyPress-Left>')
                self.avatar.rightKey = self.canvas.unbind_all('<KeyPress-Right>')
                self.avatar.upKey = self.canvas.unbind_all('<KeyPress-Up>')
                self.avatar.downKey = self.canvas.unbind_all('<KeyPress-Down>')
                if 365 < self.canvas.coords(self.avatar.torso)[2] < 385:
                    self.canvas.moveto(self.avatar.torso, 350, START_Y)
                    self.canvas.moveto(self.avatar.head, 350, START_Y-10)
                elif 370 <= self.canvas.coords(self.avatar.torso)[0] < 420:
                    self.canvas.moveto(self.avatar.torso, 430, START_Y)
                    self.canvas.moveto(self.avatar.head, 430, START_Y-10)
                if self.protein >= 5:
                    self.protein -= 5
                else:
                    self.protein = 0
                self.canvas.itemconfig(self.text, text=f'Required Daily Protein: {self.reqProtein}g   |   Your Protein: {self.protein} ')
                self.ai.update()
                h1, h2, h3, h4 = self.canvas.coords(self.avatar.head)[0], self.canvas.coords(self.avatar.head)[1], self.canvas.coords(self.avatar.head)[2], self.canvas.coords(self.avatar.head)[3]
                t1, t2, t3, t4 = self.canvas.coords(self.avatar.torso)[0], self.canvas.coords(self.avatar.torso)[1], self.canvas.coords(self.avatar.torso)[2], self.canvas.coords(self.avatar.torso)[3]
                self.canvas.delete(self.avatar.head)
                self.canvas.delete(self.avatar.torso)
                self.avatar.head = self.canvas.create_oval(h1-1, h2, h3+1, h4, fill='sandybrown')
                self.avatar.torso = self.canvas.create_rectangle(t1-1, t2, t3+1, t4, fill='lime')
                self.dumbbell_bool = False
            if self.ai.finish == True:
                self.avatar.leftKey = self.canvas.bind_all('<KeyPress-Left>', self.avatar.move)
                self.avatar.rightKey = self.canvas.bind_all('<KeyPress-Right>', self.avatar.move)
                self.avatar.upKey = self.canvas.bind_all('<KeyPress-Up>', self.avatar.move)
                self.avatar.downKey = self.canvas.bind_all('<KeyPress-Down>', self.avatar.move)
        self.avatar.update()
        self.check_win()
        self.canvas.after(CLOCK_RATE, self.update)

    def check_win(self):
        if self.protein >= self.reqProtein:
            self.trophy.get_trophy()
            self.canvas.itemconfig(self.chickenText, text='You must bring the chicken back for more protein!!!')
            if self.avatar.hit_object(self.ai.chicken[2]):
                self.chicken_bool = True
                for i in self.ai.chicken:
                    self.canvas.delete(i)
            if self.avatar.hit_object(self.land.house) and self.chicken_bool == True:
                self.protein += 38
                self.avatar.leftKey = self.canvas.unbind_all('<KeyPress-Left>')
                self.avatar.rightKey = self.canvas.unbind_all('<KeyPress-Right>')
                self.avatar.upKey = self.canvas.unbind_all('<KeyPress-Up>')
                self.avatar.downKey = self.canvas.unbind_all('<KeyPress-Down>')
    
class Ai:
    def __init__(self, canvas):

        self.canvas = canvas
        self.finish = False
        self.count = 0
        self.chicken = self.make_chicken()
        self.dumbbell = self.make_dumbbell()  

    def make_chicken(self):
        a = self.canvas.create_oval(575, START_Y-25, 585, START_Y-15, fill='white') # head
        b = self.canvas.create_polygon(585,START_Y-22, 585,START_Y-18, 590,START_Y-20, fill='orange', outline='black') # beak
        c = self.canvas.create_oval(565, START_Y-15, 585, START_Y-5, fill='white') # body
        d = self.canvas.create_rectangle(570, START_Y-5, 572, START_Y, fill='red') # left leg
        e = self.canvas.create_rectangle(575, START_Y-5, 577, START_Y, fill='red') # right leg
        return [a, b, c, d, e]

    def make_dumbbell(self):
        a = self.canvas.create_rectangle(370, START_Y-5, 375, START_Y-10, fill='grey')
        b = self.canvas.create_rectangle(375, START_Y-2, 380, START_Y-13, fill='grey')
        c = self.canvas.create_rectangle(380, START_Y, 385, START_Y-15, fill='grey')
        d = self.canvas.create_rectangle(385, START_Y-5, 400, START_Y-10, fill='grey') # bar
        e = self.canvas.create_rectangle(400, START_Y, 405, START_Y-15, fill='grey')
        f = self.canvas.create_rectangle(405, START_Y-2, 410, START_Y-13, fill='grey')
        g = self.canvas.create_rectangle(410, START_Y-5, 415, START_Y-10, fill='grey')
        return [a, b, c, d, e, f, g]
    
    def update(self):
        self.finish = False
        for i in self.dumbbell:
            self.canvas.delete(i)
        a = self.canvas.create_oval(383, START_Y, 403, START_Y-20, fill='grey')
        b = self.canvas.create_oval(388, START_Y-5, 398, START_Y-15, fill='grey')
        c = self.canvas.create_oval(392, START_Y-9, 394, START_Y-11, fill='grey')
        side = [a, b, c]
        self.up_down(side, True)

    def up_down(self, obj, bool):
        if self.count == 5:
            self.dumbbell = self.make_dumbbell()
            self.count = 0
            for i in obj:
                self.canvas.delete(i)
            self.finish = True
        else:
            self.count += 1
            if bool == True:
                for i in obj:
                    self.canvas.move(i, 0, -10)
            else:
                for i in obj:
                    self.canvas.move(i, 0, 10)
            self.canvas.after(1000, self.up_down, obj, False if bool == True else True)
        
class Trophy:
    def __init__(self, canvas):

        self.canvas = canvas
        self.egg = self.canvas.create_oval(552, START_Y-10, 558, START_Y, fill='white')
        self.egg_bool = False
        
    def get_trophy(self):
        self.canvas.delete(self.egg)

    def replace(self):
        self.egg = self.canvas.create_oval(552, START_Y-10, 558, START_Y, fill='white')

class Land:
    def __init__(self, canvas):

        self.canvas = canvas

        self.canvas.create_rectangle( 0, 0, WIDTH, START_Y-100, fill='lightblue') # sky
        self.canvas.create_rectangle( 0, START_Y-120, WIDTH, START_Y, fill='limegreen') # valley
        
        self.make_hill(10, 230, 200, 230, height=100)
        self.make_hill(300, 230, 600, 230, height=100)

        self.birdRight = 65
        self.birdLeft = 10
        self.leftWing = self.canvas.create_arc(self.birdLeft, 80, 40, 150, start=30, extent=120, style='arc', width=3)
        self.rightWing = self.canvas.create_arc(35, 80, self.birdRight, 150, start=30, extent=120, style='arc', width=3)
        self.moveBird = self.update(bool = True)

        self.coop = self.make_coop()
        self.house = self.make_house()


    def make_hill(self, x1, y1, x2, y2, height):
        self.canvas.create_polygon(x1, y1, x2, y2, (x1+x2)/2, y2-height, fill='brown', outline='black') 

    def make_house(self):
        body = self.canvas.create_rectangle(0, START_Y-80, 50, START_Y, fill='tan')
        self.canvas.create_rectangle(5, START_Y-60, 20, START_Y-40, fill='white')
        self.canvas.create_rectangle(30, START_Y-60, 45, START_Y-40, fill='white')
        self.canvas.create_rectangle(20, START_Y-25, 40, START_Y, fill='brown')
        self.canvas.create_oval(22,335, 27, 340, fill='yellow')
        return body 

    def make_coop(self):
        a = self.canvas.create_rectangle(590, START_Y-50, WIDTH, START_Y, fill='maroon')
        b = self.canvas.create_rectangle(565, START_Y-60, WIDTH, START_Y-50, fill='maroon') # roof
        return [a, b]

    def get_obstacles(self):
        return [self.house, self.coop]
    
    def update(self, bool):
        if self.birdRight < 600 and bool == True:
            self.birdRight += 1
            self.canvas.move(self.leftWing, 1, 0)
            self.canvas.move(self.rightWing, 1, 0)
        else:
            bool = False
        if self.birdRight > 55 and bool == False:
            self.birdRight -= 1
            self.canvas.move(self.leftWing, -1, 0)
            self.canvas.move(self.rightWing, -1, 0)
        else:
            bool = True
        self.canvas.after(CLOCK_RATE, self.update, bool)

class Avatar:
    def __init__(self, canvas):

        color1 = 'lime'
        color2 = 'sandybrown'
        self.canvas = canvas
        self.head = self.canvas.create_oval(50, 0, 60, 10, fill=color2)
        self.torso = self.canvas.create_rectangle(50, 10, 60, 20, fill=color1)
        self.canvas.move(self.head, START_X, START_Y-20)
        self.canvas.move(self.torso, START_X, START_Y-20)
        self.leftKey = self.canvas.bind_all('<KeyPress-Left>', self.move)
        self.rightKey = self.canvas.bind_all('<KeyPress-Right>', self.move)
        self.upKey = self.canvas.bind_all('<KeyPress-Up>', self.move)
        self.downKey = self.canvas.bind_all('<KeyPress-Down>', self.move)
        self.count = 0

        self.x = .5
        self.y = 0

    def update(self):
        if 350 >= self.canvas.coords(self.torso)[3]: # check bottom
            self.canvas.move(self.head, self.x, self.y)
            self.canvas.move(self.torso, self.x, self.y)
        else:
            self.y = 0
            self.canvas.move(self.head, 0, -1)
            self.canvas.move(self.torso, 0, -1)

        if START_X-20 <= self.canvas.coords(self.torso)[0]: # check left wall
            self.canvas.move(self.head, self.x, self.y)
            self.canvas.move(self.torso, self.x, self.y)
        else:
            self.x = .5

        if WIDTH >= self.canvas.coords(self.torso)[2]: # check right wall
            self.canvas.move(self.head, self.x, self.y)
            self.canvas.move(self.torso, self.x, self.y)
        else:
            self.x = -.5

        if 2 <= self.canvas.coords(self.head)[1]: # check top
            self.canvas.move(self.head, self.x, self.y)
            self.canvas.move(self.torso, self.x, self.y)
        else:
            self.y = .1

    def move(self, event=None):
        if event.keysym == 'Left':
            self.x = -.5
            self.y = 0
        elif event.keysym == 'Right':
            self.x = .5
            self.y = 0
        elif event.keysym == 'Up': # jumping
            self.upKey = self.canvas.unbind_all('<KeyPress-Up>')
            self.jump(True)
        elif event.keysym == 'Down':
            self.y = .5
            self.x = 0
    
    def jump(self, bool):
        if self.count < 2:
            self.count += 1
            if bool == True:
                self.y = -.5
            else:
                self.y = .5
            self.canvas.after(500, self.jump, False if bool == True else True)
        else:
            self.count = 0
            self.y = 1
            self.upKey = self.canvas.bind_all('<KeyPress-Up>', self.move)
   
    def hit_object(self, obj):
        try:
            if self.canvas.coords(self.torso)[2] >= self.canvas.coords(obj)[0] >= self.canvas.coords(self.torso)[0] and self.canvas.coords(self.torso)[3] >= self.canvas.coords(obj)[1] <= self.canvas.coords(self.torso)[1]:
                self.canvas.move(self.head, -5, 0)
                self.canvas.move(self.torso, -5, 0)
                self.x = 0
                self.y = 0
                return True
            if self.canvas.coords(self.torso)[2] >= self.canvas.coords(obj)[2] >= self.canvas.coords(self.torso)[0] and self.canvas.coords(self.torso)[3] >= self.canvas.coords(obj)[1] <= self.canvas.coords(self.torso)[1]:
                self.canvas.move(self.head, 5, 0)
                self.canvas.move(self.torso, 5, 0)
                self.x = 0
                self.y = 0
                return True
        except:
            None

    def replace(self):
        self.canvas.delete(self.head)
        self.canvas.delete(self.torso)
        self.head = self.canvas.create_oval(60, START_Y-20, 70, START_Y-10, fill='sandybrown')
        self.torso = self.canvas.create_rectangle(60, START_Y-10, 70, START_Y, fill='lime')
        self.x = .5
        self.y = 0

def get_weight(entry, window):
    global weight 
    try:
        weight = float(entry.get())
        window.destroy()
    except:
        None

import tkinter as tk 
from functools import partial
if __name__ == '__main__':

    # weight = 0
    # tkWindow = Tk()  
    # tkWindow.geometry('250x50')  
    # tkWindow.title('Weight Input')

    # usernameLabel = Label(tkWindow, text="Enter a weight in lbs: ")
    # entry = Entry(tkWindow)

    # detail = partial(get_weight, entry, tkWindow)

    # submitButton = Button(tkWindow, text="Submit", command = detail)

    # usernameLabel.grid(row=0, column=0)
    # entry.grid(row=0, column=1) 
    # submitButton.grid(row=1, column=1) 

    # tkWindow.mainloop()
   
    tk = Tk()
    tk.title('Gainz')
    canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
    canvas.pack()
    # game = Skyland(canvas, weight)
    game = Skyland(canvas)
    mainloop()