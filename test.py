# Tic Tac Toe game with GUI
# using tkinter

# importing all necessary libraries
from lib2to3.pgen2.token import RARROW
import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy
import time
import tkinter.messagebox

import tkinter
from tkinter import *

#new

# sign variable to decide the turn of which player
sign = 0

#root = Tk()

# Creates an empty board
global board
board = [[" " for x in range(3)] for y in range(3)]



# Check l(O/X) won the match or not
# according to the rules of the game
def winner(b, l):
	return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
			(b[1][0] == l and b[1][1] == l and b[1][2] == l) or
			(b[2][0] == l and b[2][1] == l and b[2][2] == l) or
			(b[0][0] == l and b[1][0] == l and b[2][0] == l) or
			(b[0][1] == l and b[1][1] == l and b[2][1] == l) or
			(b[0][2] == l and b[1][2] == l and b[2][2] == l) or
			(b[0][0] == l and b[1][1] == l and b[2][2] == l) or
			(b[0][2] == l and b[1][1] == l and b[2][0] == l))


# Check if the player can push the button or not
def isfree(i, j):
	return board[i][j] == " "

# Check the board is full or not
def isfull():
	flag = True
	for i in board:
		if(i.count(' ') > 0):
			flag = False
	return flag



# Decide the next move of system
def pc():
	possiblemove = []
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == ' ':
				possiblemove.append([i, j])
	move = []
	if possiblemove == []:
		return
	else:
		for let in ['O', 'X']:
			for i in possiblemove:
				boardcopy = deepcopy(board)
				boardcopy[i[0]][i[1]] = let
				if winner(boardcopy, let):
					return i
		corner = []
		for i in possiblemove:
			if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
				corner.append(i)
		if len(corner) > 0:
			move = random.randint(0, len(corner)-1)
			return corner[move]
		edge = []
		for i in possiblemove:
			if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
				edge.append(i)
		if len(edge) > 0:
			move = random.randint(0, len(edge)-1)
			return edge[move]

"""def backtomenu(game_board):
	bean.title("Menu")
	nex.pack_forget
	B1 = Button(game_board, text = "Tic Tac Toes", 
				activeforeground = 'gray',
				activebackground = "yellow", bg = "dark gray",
				fg = "black", width = 50, font = 'blue', bd = 5)
	if count > 0:
		B1.configure(state = DISABLED)
	B3 = Button(game_board, text = "Exit", command = game_board.quit,
				activeforeground = 'green',
				activebackground = "yellow", bg = "dark green",
				fg = "white", width = 50, font = 'blue', bd = 5)
	C1 = Button(game_board, text = "Cooking", command = lambda:cpc(game_board),
				activeforeground = 'green',
				activebackground = "yellow", bg = "dark red",
				fg = "white", width = 50, font = 'blue', bd = 5)
	B1.pack(side = 'top')
	C1.pack(side = 'top')
	B3.pack(side = 'top')"""

# Configure text on button while playing with system
def get_text_pc(i, j, gb, l1, l2):
	global sign
	if board[i][j] == ' ':
		if sign % 2 == 0:
			l1.config(state=DISABLED)
			l2.config(state=ACTIVE)
			board[i][j] = "X"
		else:
			button[i][j].config(state=ACTIVE)
			l2.config(state=DISABLED)
			l1.config(state=ACTIVE)
			board[i][j] = "O"
		sign += 1
		button[i][j].config(text=board[i][j])
	x = True
	if winner(board, "X"):
		#gb.destroy()
		
		x = False
		box = messagebox.showinfo("Winner", "Player won the match")
		l1.grid_forget()
		l2.grid_forget()
		resetboard()
		clearboard()
		levels = 1
		gb.geometry("250x250")
		sd = Label(gb, text = "sfgvsf")
		#sd.pack()
		#backtomenu(bean)
		backtomenu(gb)
	elif winner(board, "O"):
		#gb.destroy()
		x = False
		box = messagebox.showinfo("Winner", "Computer won the match--try again")
		sign = 0
		resetboard()
		clearboard()
		gameboard_pc(gb, l1, l2)
	elif(isfull()):
		#gb.destroy()
		x = False
		box = messagebox.showinfo("Tie", "The match is a tie--try again")
		sign = 0
		resetboard()
		clearboard()
		gameboard_pc(gb, l1, l2)

		#l1.grid_forget()
		#l2.grid_forget()
		#restart.grid(row=1, column=1)
		#play()


        
	if(x):
		if sign % 2 != 0:
			move = pc()
			button[move[0]][move[1]].config(state=DISABLED)
			get_text_pc(move[0], move[1], gb, l1, l2)

# Create the GUI of game board for play along with system
def gameboard_pc(game_board, l1, l2):
	global button
	button = []
	for i in range(3):
		m = 3+i
		button.append(i)
		button[i] = []
		for j in range(3):
			n = j
			button[i].append(j)
			get_t = partial(get_text_pc, i, j, game_board, l1, l2)
			button[i][j] = Button(
				game_board, bd=5, command=get_t, height=4, width=8)
			button[i][j].grid(row=m, column=n)
	game_board.mainloop()

# Initialize the game board to play with system
def withpc(game_board):
	game_board.destroy()
	game_board = Tk()
	game_board.title("Tic Tac Toe")
	l1 = Button(game_board, text="Player : X", width=10)
	l1.grid(row=1, column=1)
	l2 = Button(game_board, text = "Computer : O",
				width = 10, state = DISABLED)
	
	l2.grid(row = 2, column = 1)
	gameboard_pc(game_board, l1, l2)

def resetboard():
	for i in range(len(board)):
		for j in range(len(board[i])):
			board[i][j] = ' '
	

def clearboard():
	for i in range(len(button)):
		for j in range(len(button[i])):
			button[i][j].grid_forget()

""""def backtomenu(game_board):
	bean.title("Menu")
	nex.pack_forget
	B1 = Button(game_board, text = "Tic Tac Toes", 
				activeforeground = 'gray',
				activebackground = "yellow", bg = "dark gray",
				fg = "black", width = 50, font = 'blue', bd = 5)
	if count > 0:
		B1.configure(state = DISABLED)
	B3 = Button(game_board, text = "Exit", command = game_board.quit,
				activeforeground = 'green',
				activebackground = "yellow", bg = "dark green",
				fg = "white", width = 50, font = 'blue', bd = 5)
	C1 = Button(game_board, text = "Cooking", command = lambda:cpc(game_board),
				activeforeground = 'green',
				activebackground = "yellow", bg = "dark red",
				fg = "white", width = 50, font = 'blue', bd = 5)
	B1.pack(side = 'top')
	C1.pack(side = 'top')
	B3.pack(side = 'top')"""



def cpc(game_board):
	game_board.destroy()
	Cooking = Tk()
	Cooking.geometry("250x250")
	Cooking.title("Cooking")
	#tkinter.messagebox.showinfo("Instructions", "Press the DONE button when the color bar is green for the max food points.")
	done = FALSE
	global ra
	ra = [0, 0, 0, 0, 0, 0]
	global ca
	ca = [0, 0, 0, 0, 0, 0]
	pots1 = Label(Cooking, bg = "dark red", width = 15)
	pots2 = Label(Cooking, bg = "dark red", width = 15)
	pots3 = Label(Cooking, bg = "dark red", width = 15)
	pots4 = Label(Cooking, bg = "dark red", width = 15)
	pots5 = Label(Cooking, bg = "dark red", width = 15)
	pots6 = Label(Cooking, bg = "dark red", width = 15)
	global recipe1, recipe2, recipe3, recipe4, recipe5, recipe6
	recipe1 = Label(Cooking, bg = "dark red", width = 15)
	recipe2 = Label(Cooking, bg = "dark red", width = 15)
	recipe3 = Label(Cooking, bg = "dark red", width = 15)
	recipe4 = Label(Cooking, bg = "dark red", width = 15)
	recipe5 = Label(Cooking, bg = "dark red", width = 15)
	recipe6 = Label(Cooking, bg = "dark red", width = 15)
	global chicken 
	chicken = Label(Cooking, bg = "dark red", width = 35)
	l1 = Button(Cooking, text="cook", command = newrecipe, width=10)
	DONE = Button(Cooking, text="DONE", command = done, width=10)
	arrow1 = Button(Cooking, text="=>", command = lambda:cooking(pots1, 0), width=5, height=1)
	arrow2 = Button(Cooking, text="=>", command = lambda:cooking(pots2, 1), width=5, height=1)
	arrow3 = Button(Cooking, text="=>", command = lambda:cooking(pots3, 2), width=5, height=1)
	arrow4 = Button(Cooking, text="=>", command = lambda:cooking(pots4, 3), width=5, height=1)
	arrow5 = Button(Cooking, text="=>", command = lambda:cooking(pots5, 4), width=5, height=1)
	arrow6 = Button(Cooking, text="=>", command = lambda:cooking(pots6, 5), width=5, height=1)
	global numdone
	numdone = 0 
	rec = Label(Cooking, text = str(numdone) + "/3")
	#chicken.grid(row = 0, column = 0)
	l1.grid(sticky = "w", padx = 10, row = 1, column = 0)
	pots1.grid(sticky = "w", row = 2, column = 0)
	pots2.grid(sticky = "w", row = 3, column = 0)
	pots3.grid(sticky = "w", row = 4, column = 0)
	pots4.grid(sticky = "w", row = 5, column = 0)
	pots5.grid(sticky = "w", row = 6, column = 0)
	pots6.grid(sticky = "w", row = 7, column = 0)
	arrow1.grid(row = 2, column = 1)
	arrow2.grid(row = 3, column = 1)
	arrow3.grid(row = 4, column = 1)
	arrow4.grid(row = 5, column = 1)
	arrow5.grid(row = 6, column = 1)
	arrow6.grid(row = 7, column = 1)
	rec.grid(row = 8, column = 1)
	recipe1.grid(sticky = "w", row = 2, column = 2)
	recipe2.grid(sticky = "w", row = 3, column = 2)
	recipe3.grid(sticky = "w", row = 4, column = 2)
	recipe4.grid(sticky = "w", row = 5, column = 2)
	recipe5.grid(sticky = "w", row = 6, column = 2)
	recipe6.grid(sticky = "w", row = 7, column = 2)


global cc
cc = [0, 0, 0, 0, 0, 0] 

global r
r = [0, 0, 0, 0, 0, 0] 

global numrep
numrep = 0

global isdone
isdone = FALSE

def done():
	isdone = TRUE


def newrecipe():
	if numrep == 0:
		recipe1.configure(bg = "tan")
		recipe2.configure(bg = "yellow")
		recipe3.configure(bg = "dark green")
		recipe4.configure(bg = "red")
		recipe5.configure(bg = "brown")
		recipe6.configure(bg = "tan")

def cooking(buttt, num):
	ca[num]
	if cc[num] == 0:
		buttt.configure(bg = "tan")
		ca[num] = 0
	if cc[num] == 1:
		buttt.configure(bg = "yellow")
		ca[num] = 1
	if cc[num] == 2:
		buttt.configure(bg = "dark green")
		ca[num] = 2
	if cc[num] == 3:
		buttt.configure(bg = "red")
		ca[num] = 3
	if cc[num] == 4:
		buttt.configure(bg = "brown")
		ca[num] = 4
	if cc[num] == 5:
		buttt.configure(bg = "tan")
	cc[num] = cc[num] + 1



# main function
def play():
	menu = Tk()
	menu.geometry("250x250")
	menu.title("Menu")
	wpc = partial(withpc, menu)
	
	
	B1 = Button(menu, text = "Tic Tac Toes", command = wpc,
				activeforeground = 'gray',
				activebackground = "yellow", bg = "dark gray",
				fg = "black", width = 500, font = 'blue', bd = 5)

	
	B3 = Button(menu, text = "Exit", command = menu.quit,
				activeforeground = 'green',
				activebackground = "yellow", bg = "dark green",
				fg = "white", width = 500, font = 'blue', bd = 5)
    
	C1 = Button(menu, text = "Cooking", command = lambda:cpc(menu),
				activeforeground = 'green',
				activebackground = "yellow", bg = "dark red",
				fg = "white", width = 500, font = 'blue', bd = 5)
	nex.grid_forget()
	dialogue.grid_forget()
	B1.pack(side = 'top')
	C1.pack(side = 'top')
	B3.pack(side = 'top')
	menu.mainloop()

global levels
levels = 0

#hannah dsifcvnioh
global bean
bean = Tk()
bean.title("A Simple Love Story <3")
bean.geometry("600x400")

#script array
firstscript = ["Welcome to the love story.", "It begins on a hill with two lovers, Alex and Sam.", "The summer air is warm.", "They are wrapped in each others arms.", "All is right in their world.", "Suddenly, the ground begins to shake.", "A ferocious dragon races up the hill.", "It takes Alex within its claws and soars into the setting sky.", "Player, you will continue this story as Sam.", "You must travel to the dragon's den, find Alex, and rescue your lover.", "Do not be afraid of the challenges along the way.", "With them, you will grow."]
count=0

global dialogue
dialogue = Label(bean, text = "Hello there, player.")

global nex
nex= Button(bean, text="NEXT", command = lambda:button_click(firstscript, dialogue))

#displays first script
def introscript():
    dialogue.pack()
    nex.pack()
    
def backtomenu(game_board):
	bean.title("Menu")
	nex.pack_forget()
	dialogue.pack_forget()
	wpc = partial(withpc, bean)
	B1 = Button(game_board, text = "Tic Tac Toes", command = wpc,
				activeforeground = 'gray',
				activebackground = "yellow", bg = "dark gray",
				fg = "black", width = 50, font = 'blue', bd = 5)
	if levels > 0:
		B1.configure(state = DISABLED)
	B3 = Button(game_board, text = "Exit", command = game_board.quit,
				activeforeground = 'green',
				activebackground = "yellow", bg = "dark green",
				fg = "white", width = 50, font = 'blue', bd = 5)
	C1 = Button(game_board, text = "Cooking", command = lambda:cpc(game_board),
				activeforeground = 'green',
				activebackground = "yellow", bg = "dark red",
				fg = "white", width = 50, font = 'blue', bd = 5)
	B1.pack(side = 'top')
	C1.pack(side = 'top')
	B3.pack(side = 'top')

#loops through array when button is clicked to change dialogue
def button_click(array, label):
    global count
    if count < len(array):
        label.configure(text = array[count])
        count+=1
    else:
        count = 0
        nex.configure(command = lambda:backtomenu(bean))



introscript()
bean.mainloop()
# hannah inkj

#Call main function
#if __name__ == '__main__':
#	play()

