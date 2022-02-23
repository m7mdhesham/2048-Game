from tkinter import *
from Game import *
from random import *
from tkinter import messagebox
import tkinter as tk

matlen=4

class Game(Frame):
    def __init__(self):
        Frame.__init__(self)
        #b1=Button(text='UP',fg='black').place(x=50,y=0)
        #b2=Button(text='DOWN',fg='black').place(x=40,y=40)
        #b3=Button(text='LEFT',fg='black').place(x=0,y=0)
        #b4=Button(text='RIGHT',fg='black').place(x=90,y=0)
        self.grid()
        self.master.title('2048 Game')
        self.master.bind("<Key>", self.key_down)
        self.commands={"'w'": up, "'s'": down, "'a'": left, "'d'": right}
        self.box=[]
        self.matGRId()
        self.input_first_mat()
        self.fill_box()
        self.mainloop()

    def matGRId(self):
        background=Frame(self, bg='black', width=400, height=400)
        background.grid()
        for a in range(matlen):
            grid_row=[]
            for b in range(matlen):
                cell=Frame(background, width=(400/matlen), height=(400/matlen))
                cell.grid(row=a, column=b, padx=5, pady=5)
                t=Label(master=cell, text="", bg='black', font=("Arial", 38, "italic"), width=4, height=2)
                t.grid()
                grid_row.append(t)
            self.box.append(grid_row)

    def input_first_mat(self):
        self.matrix=start(matlen)
        self.matrix=random_two(self.matrix)
        self.matrix=random_two(self.matrix)

    def fill_box(self):
        for m in range(matlen):
            for n in range(matlen):
                x=self.matrix[m][n]
                if x==0:
                    self.box[m][n].configure(text="", bg='red')
                else:
                    self.box[m][n].configure(text=str(x), bg='orange', fg='white')
        self.update_idletasks()
        
    def key_down(self, commandfunction):
        k=repr(commandfunction.char)
        if k in self.commands:
            self.matrix,done=self.commands[repr(commandfunction.char)](self.matrix)
            if done:
                self.matrix=random_two(self.matrix)
                self.fill_box()
                done=False
                if wingame(self.matrix)=='win':
                    text='YOU WON!'
                    messagebox.showinfo("2048",text)
STARTGAMEwhenrun=Game()
