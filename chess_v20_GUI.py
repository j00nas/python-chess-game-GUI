from tkinter import *
import tkinter.messagebox



###------------------------------------------------------------ GUI ------------------------------------------------------------###


tk = Tk()
tk.title('Chess 2.0')
tk.configure(background='white')
game_started = False
tkstart = ()
tkend = ()
startbutton = ''
endbutton = ''
endbutton_color = ''
startbutton_color = ''
error = -1
last_movement = ()


def restart_game():
	main()
	undo_coloring(restartgame = True)

	history_gui.configure(state='normal')
	history_gui.delete('1.0' ,END)
	history_gui.configure(state='disabled')

	labelZahl1['text'] = "White's turn"

	black_fig = [BR, BN, BB, BQ, BK, BB, BN, BR, BP, BP, BP, BP, BP, BP, BP, BP]
	white_fig = [WP, WP, WP, WP, WP, WP, WP, WP, WR, WN, WB, WQ, WK, WB, WN, WR]
	board_fig = black_fig + ['' for i in range(32)] + white_fig

	for count, i in enumerate(fields_dic):
		fields_dic[i]['text'] = board_fig[count]


def undo_coloring(restartgame = False):
	positions = [i for i in fields_dic]
	white = [0,2,4,6,9,11,13,15,16,18,20,22,25,27,29,31,32,34,36,38,41,43,45,47,48,50,52,54,57,59,61,63]
	black = [i for i in range(63) if i not in white]

	for i in white:
		fields_dic[positions[i]]['bg'] = 'white'
	for i in black:
		fields_dic[positions[i]]['bg'] = 'grey'

	if last_movement and not restartgame:
		fields_dic[last_movement[0]]['bg'] = '#ccffcc' 
		fields_dic[last_movement[1]]['bg'] = '#ccffcc'

	for i in fields_dic:
		if fields_dic[i]['fg'] == 'lightblue':
			fields_dic[i]['fg'] = 'black'
		if fields_dic[i]['text'] == '\u0E4F':
			fields_dic[i]['text'] = ''
		if 'check' in fields_dic[i]['text']:
			if not history: 
				fields_dic[i]['text'] = fields_dic[i]['text'][:1]
			elif not history[-1][-1] and not check_mate:
				fields_dic[i]['text'] = fields_dic[i]['text'][:1]


def display_moves(coord):
	global fields_dic

	if Chess_Board.Fig_Pos[coord]._color == current_color:
		for fields in Chess_Board.Fig_Pos[coord].poss_moves:
			if fields_dic[fields]['text'] == '':
				fields_dic[fields]['fg'] = 'lightblue'
				fields_dic[fields]['text'] = '\u0E4F'
			else:
				fields_dic[fields]['fg'] = 'lightblue'


def enemy_king_position(current_color):
	enemy_king_pos = ()
	for find_king_pos in Chess_Board.Fig_Pos:
		if Chess_Board.Fig_Pos[find_king_pos]._color == current_color and Chess_Board.Fig_Pos[find_king_pos]._figure == 'King':
			enemy_king_pos = Chess_Board.Fig_Pos[find_king_pos].position
			break
	return enemy_king_pos

def btnClick(id):
	global game_started, tkstart, tkend, error, fields_dic, startbutton_color, endbutton_color, is_check, check_mate, playing, last_movement

	fields_dic =   {(0,0):a8, (0,1):b8, (0,2):c8, (0,3):d8, (0,4):e8, (0,5):f8, (0,6):g8, (0,7):h8, 
					(1,0):a7, (1,1):b7, (1,2):c7, (1,3):d7, (1,4):e7, (1,5):f7, (1,6):g7, (1,7):h7, 
					(2,0):a6, (2,1):b6, (2,2):c6, (2,3):d6, (2,4):e6, (2,5):f6, (2,6):g6, (2,7):h6,
					(3,0):a5, (3,1):b5, (3,2):c5, (3,3):d5, (3,4):e5, (3,5):f5, (3,6):g5, (3,7):h5, 
					(4,0):a4, (4,1):b4, (4,2):c4, (4,3):d4, (4,4):e4, (4,5):f4, (4,6):g4, (4,7):h4, 
					(5,0):a3, (5,1):b3, (5,2):c3, (5,3):d3, (5,4):e3, (5,5):f3, (5,6):g3, (5,7):h3, 
					(6,0):a2, (6,1):b2, (6,2):c2, (6,3):d2, (6,4):e2, (6,5):f2, (6,6):g2, (6,7):h2, 
					(7,0):a1, (7,1):b1, (7,2):c1, (7,3):d1, (7,4):e1, (7,5):f1, (7,6):g1, (7,7):h1}
	
	if not game_started:
		main()
		game_started = True

	if id == tkstart:
		undo_coloring()
		startbutton_color = ''
		endbutton_color = ''
		tkstart = ()
		tkend = ()

	elif tkstart != ():
		tkend = id
		if tkend in Chess_Board.Fig_Pos and Chess_Board.Fig_Pos[tkend]._color == current_color:
			con = True
			if tkstart in Chess_Board.Fig_Pos: #Rochade 
				if (Chess_Board.Fig_Pos[tkstart]._figure == 'King' and Chess_Board.Fig_Pos[tkend]._figure == 'Rook') or (Chess_Board.Fig_Pos[tkstart]._figure == 'Rook' and Chess_Board.Fig_Pos[tkend]._figure == 'King'):
					con = False
			if con: 
				fields_dic[tkstart]['bg'] = startbutton_color
				undo_coloring()
				tkstart = tkend
				startbutton_color = fields_dic[tkstart]['bg']
				fields_dic[tkstart]['bg'] = 'lightblue'
				display_moves(tkstart)	
				tkend = ()	
		if tkstart not in Chess_Board.Fig_Pos and tkend not in Chess_Board.Fig_Pos:
			tkstart = ()
			tkend = ()

	else:
		tkstart = id
		startbutton_color = fields_dic[tkstart]['bg']
		if tkstart in Chess_Board.Fig_Pos and Chess_Board.Fig_Pos[tkstart]._color == current_color:		
			fields_dic[tkstart]['bg'] = 'lightblue'
		if fields_dic[tkstart]['text'] != '':
			display_moves(tkstart)



	if tkstart != () and tkend != ():
		endbutton_color = fields_dic[tkend]['bg'] 

		if not check_mate:
			play_game()	
			if error == 0:
				undo_coloring()
				figure = fields_dic[tkstart]['text']
				figure2 = fields_dic[tkend]['text'] 
				if figure2 != '': 
					if tkstart in Chess_Board.Fig_Pos: #Can be true if Rochade
						if (Chess_Board.Fig_Pos[tkstart]._figure == 'King' and Chess_Board.Fig_Pos[tkend]._figure == 'Rook') or (Chess_Board.Fig_Pos[tkstart]._figure == 'Rook' and Chess_Board.Fig_Pos[tkend]._figure == 'King'):
							fields_dic[tkstart]['text'], fields_dic[tkend]['text'] = figure2, figure
					elif is_check:
						enemy_king_pos = enemy_king_position(current_color)
						fields_dic[enemy_king_pos]['text'] = fields_dic[enemy_king_pos]['text'] + '\ncheck!'
						fields_dic[tkstart]['text'], fields_dic[tkend]['text'] = '', figure	
					else: 
						fields_dic[tkstart]['text'], fields_dic[tkend]['text'] = '', figure
				else:
					enemy_king_pos = enemy_king_position(current_color)		
					if is_check:
						fields_dic[enemy_king_pos]['text'] = fields_dic[enemy_king_pos]['text'] + '\ncheck!'
						fields_dic[tkstart]['text'], fields_dic[tkend]['text'] = '', figure
					elif check_mate:
						fields_dic[tkstart]['text'], fields_dic[tkend]['text'] = '', figure
						fields_dic[enemy_king_pos]['text'] = fields_dic[enemy_king_pos]['text'] + '\ncheck \nmate!'
						playing = False
					else:
						fields_dic[tkstart]['text'], fields_dic[tkend]['text'] = '', figure

				last_movement = (tkstart, tkend)
				undo_coloring()
				fields_dic[tkstart]['bg'] = '#ccffcc' 
				fields_dic[tkend]['bg'] = '#ccffcc'
				tkstart = ()
				tkend = ()
				startbutton_color = ''
				endbutton_color = ''
				error = -1
				display_player_color = "White's turn" if current_color == 1 else "Black's turn"
				labelZahl1['text'] = display_player_color

			else:
				undo_coloring()
				startbutton_color = ''
				endbutton_color = ''			
				tkstart = ()
				tkend = ()

		

BR = '\u265C'
BN = '\u265E'
BB = '\u265D'
BQ = '\u265B'
BK = '\u265A'
BP = '\u265F'

WR = '\u2656'
WN = '\u2658'
WP = '\u2659'
WQ = '\u2655'
WK = '\u2654'
WB = '\u2657'

a8 = Button(tk, text=BR, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((0,0))])
a8.grid(row=1, column=1, padx=(40,0), pady=(40,0))
b8 = Button(tk, text=BN, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((0,1))])
b8.grid(row=1, column=2, padx=(0,0), pady=(40,0))
c8 = Button(tk, text=BB, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((0,2))])
c8.grid(row=1, column=3, padx=(0,0), pady=(40,0))
d8 = Button(tk, text=BQ, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((0,3))])
d8.grid(row=1, column=4, padx=(0,0), pady=(40,0))
e8 = Button(tk, text=BK, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((0,4))])
e8.grid(row=1, column=5, padx=(0,0), pady=(40,0))
f8 = Button(tk, text=BB, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((0,5))])
f8.grid(row=1, column=6, padx=(0,0), pady=(40,0))
g8 = Button(tk, text=BN, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((0,6))])
g8.grid(row=1, column=7, padx=(0,0), pady=(40,0))
h8 = Button(tk, text=BR, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((0,7))])
h8.grid(row=1, column=8, padx=(0,40), pady=(40,0))
a7 = Button(tk, text=BP, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((1,0))])
a7.grid(row=2, column=1, padx=(40,0), pady=(0,0))
b7 = Button(tk, text=BP, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((1,1))])
b7.grid(row=2, column=2)
c7 = Button(tk, text=BP, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((1,2))])
c7.grid(row=2, column=3)
d7 = Button(tk, text=BP, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((1,3))])
d7.grid(row=2, column=4)
e7 = Button(tk, text=BP, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((1,4))])
e7.grid(row=2, column=5)
f7 = Button(tk, text=BP, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((1,5))])
f7.grid(row=2, column=6)
g7 = Button(tk, text=BP, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((1,6))])
g7.grid(row=2, column=7)
h7 = Button(tk, text=BP, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((1,7))])
h7.grid(row=2, column=8, padx=(0,40), pady=(0,0))
a6 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((2,0))])
a6.grid(row=3, column=1, padx=(40,0), pady=(0,0))
b6 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((2,1))])
b6.grid(row=3, column=2)
c6 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((2,2))])
c6.grid(row=3, column=3)
d6 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((2,3))])
d6.grid(row=3, column=4)
e6 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((2,4))])
e6.grid(row=3, column=5)
f6 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((2,5))])
f6.grid(row=3, column=6)
g6 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((2,6))])
g6.grid(row=3, column=7)
h6 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((2,7))])
h6.grid(row=3, column=8, padx=(0,40), pady=(0,0))
a5 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((3,0))])
a5.grid(row=4, column=1, padx=(40,0), pady=(0,0))
b5 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((3,1))])
b5.grid(row=4, column=2)
c5 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((3,2))])
c5.grid(row=4, column=3)
d5 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((3,3))])
d5.grid(row=4, column=4)
e5 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((3,4))])
e5.grid(row=4, column=5)
f5 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((3,5))])
f5.grid(row=4, column=6)
g5 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((3,6))])
g5.grid(row=4, column=7)
h5 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((3,7))])
h5.grid(row=4, column=8, padx=(0,40), pady=(0,0))
a4 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((4,0))])
a4.grid(row=5, column=1, padx=(40,0), pady=(0,0))
b4 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((4,1))])
b4.grid(row=5, column=2)
c4 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((4,2))])
c4.grid(row=5, column=3)
d4 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((4,3))])
d4.grid(row=5, column=4)
e4 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((4,4))])
e4.grid(row=5, column=5)
f4 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((4,5))])
f4.grid(row=5, column=6)
g4 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((4,6))])
g4.grid(row=5, column=7)
h4 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((4,7))])
h4.grid(row=5, column=8, padx=(0,40), pady=(0,0))
a3 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((5,0))])
a3.grid(row=6, column=1, padx=(40,0), pady=(0,0))
b3 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((5,1))])
b3.grid(row=6, column=2)
c3 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((5,2))])
c3.grid(row=6, column=3)
d3 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((5,3))])
d3.grid(row=6, column=4)
e3 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((5,4))])
e3.grid(row=6, column=5)
f3 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((5,5))])
f3.grid(row=6, column=6)
g3 = Button(tk, text='', font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((5,6))])
g3.grid(row=6, column=7)
h3 = Button(tk, text='', font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((5,7))])
h3.grid(row=6, column=8, padx=(0,40), pady=(0,0))
a2 = Button(tk, text=WP, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((6,0))])
a2.grid(row=7, column=1, padx=(40,0), pady=(0,0))
b2 = Button(tk, text=WP, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((6,1))])
b2.grid(row=7, column=2)
c2 = Button(tk, text=WP, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((6,2))])
c2.grid(row=7, column=3)
d2 = Button(tk, text=WP, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((6,3))])
d2.grid(row=7, column=4)
e2 = Button(tk, text=WP, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((6,4))])
e2.grid(row=7, column=5)
f2 = Button(tk, text=WP, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((6,5))])
f2.grid(row=7, column=6)
g2 = Button(tk, text=WP, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((6,6))])
g2.grid(row=7, column=7)
h2 = Button(tk, text=WP, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((6,7))])
h2.grid(row=7, column=8, padx=(0,40), pady=(0,0))
a1 = Button(tk, text=WR, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((7,0))])
a1.grid(row=8, column=1, padx=(40,0), pady=(0,40))
b1 = Button(tk, text=WN, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((7,1))]) 
b1.grid(row=8, column=2, padx=(0,0), pady=(0,40))
c1 = Button(tk, text=WB, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((7,2))])  
c1.grid(row=8, column=3, padx=(0,0), pady=(0,40))
d1 = Button(tk, text=WQ, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((7,3))]) 
d1.grid(row=8, column=4, padx=(0,0), pady=(0,40))
e1 = Button(tk, text=WK, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((7,4))])
e1.grid(row=8, column=5, padx=(0,0), pady=(0,40))
f1 = Button(tk, text=WB, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((7,5))])
f1.grid(row=8, column=6, padx=(0,0), pady=(0,40))
g1 = Button(tk, text=WN, font='Times 20 bold', bg='grey', height=2, width=5, command=lambda: [btnClick((7,6))])
g1.grid(row=8, column=7, padx=(0,0), pady=(0,40))
h1 = Button(tk, text=WR, font='Times 20 bold', bg='white', height=2, width=5, command=lambda: [btnClick((7,7))])
h1.grid(row=8, column=8, padx=(0,40), pady=(0,40))

labelZahl1 = Label(tk, text="White's turn", bg = 'white', width = 30)
labelZahl1.config(font=(10))
labelZahl1.grid(row=1, column=9, sticky='w')
labelZahl2 = Label(tk, text='Game History', bg = 'white', width = 30)
labelZahl2.config(font=(10))
labelZahl2.grid(row=3, column=9, sticky='w')

history_gui = Text(tk, height=10, width=30, wrap = 'none', pady = 5, padx = 5)
scroll = Scrollbar(tk, command=history_gui.yview)
history_gui.configure(yscrollcommand=scroll.set, state='disabled')
history_gui.grid(row = 4, column = 9, rowspan = 2)

restartgame_button = Button(tk, text='Restart Game', bg='white', height=1, width=10, command=lambda: [restart_game()])
restartgame_button.config(font=(10))
restartgame_button.grid(row=8, column=9)






###------------------------------------------------------------ ENGINE ------------------------------------------------------------###


class Board(object):
	def __init__(self):
		self.Fig_Pos = {
						(0,0) : Rook(0, (0,0), []),
						(0,1) : Knight(0, (0,1), []),
						(0,2) : Bishop(0, (0,2), []),
						(0,3) : Queen(0, (0,3), []),
						(0,4) : King(0, (0,4), []),
						(0,5) : Bishop(0, (0,5), []),
						(0,6) : Knight(0, (0,6), []),
						(0,7) : Rook(0, (0,7), []),	
						(1,0) : Pawn(0, (1,0), []),
						(1,1) : Pawn(0, (1,1), []),
						(1,2) : Pawn(0, (1,2), []),
						(1,3) : Pawn(0, (1,3), []),
						(1,4) : Pawn(0, (1,4), []),
						(1,5) : Pawn(0, (1,5), []),
						(1,6) : Pawn(0, (1,6), []),
						(1,7) : Pawn(0, (1,7), []),
						(7,0) : Rook(1, (7,0), []),
						(7,1) : Knight(1, (7,1), []),
						(7,2) : Bishop(1, (7,2), []),
						(7,3) : Queen(1, (7,3), []),
						(7,4) : King(1, (7,4), []),
						(7,5) : Bishop(1, (7,5), []),
						(7,6) : Knight(1, (7,6), []),
						(7,7) : Rook(1, (7,7), []),	
						(6,0) : Pawn(1, (6,0), []),
						(6,1) : Pawn(1, (6,1), []),
						(6,2) : Pawn(1, (6,2), []),
						(6,3) : Pawn(1, (6,3), []),
						(6,4) : Pawn(1, (6,4), []),
						(6,5) : Pawn(1, (6,5), []),
						(6,6) : Pawn(1, (6,6), []),
						(6,7) : Pawn(1, (6,7), [])
						}

	def draw_Board(self):
		board_side = [' 8 \u2502',' 7 \u2502',' 6 \u2502',' 5 \u2502',' 4 \u2502',' 3 \u2502',' 2 \u2502',' 1 \u2502']
		print('\n\n        a   b   c   d   e   f   g   h' + '\n    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n   \u2502                                    \u2502')
		k = 8
		for i in range(8):
			print(board_side[i], end = '   ')
			for j in range(8):
				if (i,j) in self.Fig_Pos:
					if self.Fig_Pos[(i,j)]._figure == 'Knight':
						print('N' + str(self.Fig_Pos[(i,j)]._color), end = '  ')
					else:
						print(self.Fig_Pos[(i,j)]._figure[0] + str(self.Fig_Pos[(i,j)]._color), end = '  ')
				else: 
					print(' \u2022 ', end = ' ')
			print(' \u2502 ' + str(k) + '\n   \u2502                                    \u2502')
			k -= 1
		print('    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n        a   b   c   d   e   f   g   h' + '\n')

	def get_positions(self):
		return self.Fig_Pos

	def update_positions(self, old_position, new_position):
		self.Fig_Pos[new_position] = self.Fig_Pos[old_position]
		del self.Fig_Pos[old_position]

	def update_position_rochade(self, old_position, new_position):
		p1 = self.Fig_Pos[old_position]
		p2 = self.Fig_Pos[new_position]

		self.Fig_Pos[old_position] = p2
		self.Fig_Pos[new_position] = p1



class Figure(object):
	def __init__(self, color, position, poss_moves):
		self._color = color
		self.position = position
		self.poss_moves = poss_moves

	def get_poss_moves(self):
		return self.poss_moves

	def get_position(self):
		return self.position

	def get_color(self):
		return self._color


class King(Figure):	
	def __init__(self, color, position, poss_moves, figure = 'King'):
		Figure.__init__(self, color, position, poss_moves)
		self._figure = figure
		self.already_moved = False

	def get_sourrounding(self):
		i,j = self.position[0], self.position[1]
		sur = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
		sur = [(i[0], i[1]) for i in sur if -1 < i[0] < 8 and -1 < i[1] < 8]
		return sur 

	def check_move(self, end_position):
		if not self.poss_moves:
			return False

		cur_position = self.get_position()
		cur_Board = Chess_Board.get_positions()
		sur = self.get_sourrounding()

		if end_position not in sur:
			return False

		if end_position not in cur_Board:
			return True

		if end_position in cur_Board and cur_Board[end_position]._color != self._color:
			return True

		return False

	def update_current_pos(self, new_position):
		self.position = new_position

	def update_poss_moves(self):
		sur = self.get_sourrounding()
		cur_Board = Chess_Board.get_positions()
		self.poss_moves = [(i[0], i[1]) for i in sur if i not in cur_Board or Chess_Board.Fig_Pos[(i[0], i[1])]._color != self._color]


class Queen(Figure):
	def __init__(self, color, position, poss_moves, figure = 'Queen'):
		Figure.__init__(self, color, position, poss_moves)
		self._figure = figure

	def get_sourrounding(self):
		cur_Board = Chess_Board.get_positions()
		i,j = self.position[0], self.position[1]
		sur = []
		for count, m in enumerate([(i+1, 8, 1), (i-1, -1, -1), (j+1, 8, 1), (j-1, -1, -1)]):
			for k in range(m[0], m[1], m[2]):
				udrl = (k,j) if count < 2 else (i,k)
				if udrl not in cur_Board: 
					sur.append(udrl)
				elif udrl in cur_Board and Chess_Board.Fig_Pos[udrl]._color != self._color:
					sur.append(udrl)
					break
				else:
					break

		for pos in ([1, 1], [1, -1], [-1, 1], [-1, -1]):
			i_m = pos[0]
			j_m = pos[1]
			while -1 < i+i_m < 8 and -1 < j+j_m < 8:
				if (i+i_m, j+j_m) in cur_Board and Chess_Board.Fig_Pos[(i+i_m, j+j_m)]._color != self._color:
					sur.append((i+i_m, j+j_m))
					break
				elif (i+i_m, j+j_m) in cur_Board and Chess_Board.Fig_Pos[(i+i_m, j+j_m)]._color == self._color:
					break
				else:
					sur.append((i+i_m, j+j_m))
					i_m += pos[0]
					j_m += pos[1]
		return sur

	def update_poss_moves(self):
		self.poss_moves = self.get_sourrounding()


class Bishop(Figure):
	def __init__(self, color, position, poss_moves, figure = 'Bishop'):
		Figure.__init__(self, color, position, poss_moves)
		self._figure = figure

	def get_sourrounding(self):
		cur_Board = Chess_Board.get_positions()
		i,j = self.position[0], self.position[1]
		sur = []
		for pos in ([1, 1], [1, -1], [-1, 1], [-1, -1]):
			i_m = pos[0]
			j_m = pos[1]
			while -1 < i+i_m < 8 and -1 < j+j_m < 8:
				if (i+i_m, j+j_m) in cur_Board and Chess_Board.Fig_Pos[(i+i_m, j+j_m)]._color != self._color:
					sur.append((i+i_m, j+j_m))
					break
				elif (i+i_m, j+j_m) in cur_Board and Chess_Board.Fig_Pos[(i+i_m, j+j_m)]._color == self._color:
					break
				else:
					sur.append((i+i_m, j+j_m))
					i_m += pos[0]
					j_m += pos[1]
		return sur		

	def update_poss_moves(self):
		self.poss_moves = self.get_sourrounding()


class Rook(Figure):
	def __init__(self, color, position, poss_moves, figure = 'Rook'):
		Figure.__init__(self, color, position, poss_moves)
		self._figure = figure
		self.already_moved = False

	def get_sourrounding(self):
		cur_Board = Chess_Board.get_positions()
		i,j = self.position[0], self.position[1]
		sur = []
		for count, m in enumerate([(i+1, 8, 1), (i-1, -1, -1), (j+1, 8, 1), (j-1, -1, -1)]):
			for k in range(m[0], m[1], m[2]):
				udrl = (k,j) if count < 2 else (i,k)
				if udrl not in cur_Board: 
					sur.append(udrl)
				elif udrl in cur_Board and Chess_Board.Fig_Pos[udrl]._color != self._color:
					sur.append(udrl)
					break
				else:
					break
		return sur

	def update_poss_moves(self):
		self.poss_moves = self.get_sourrounding()


class Knight(Figure):
	def __init__(self, color, position, poss_moves, figure = 'Knight'):
		Figure.__init__(self, color, position, poss_moves)
		self._figure = figure

	def get_sourrounding(self):
		sur = []
		cur_Board = Chess_Board.get_positions()
		i = self.position[0]
		j = self.position[1]

		for posspos in [(i-2, j-1), (i-2, j+1), (i-1, j-2), (i-1, j+2), (i+2, j-1), (i+2, j+1), (i+1, j-2), (i+1, j+2)]:
			i_k = posspos[0]
			j_k = posspos[1]
			if 0 <= i_k < 8 and 0 <= j_k < 8 and (i_k, j_k) not in cur_Board:
				sur.append((i_k, j_k))
			if 0 <= i_k < 8 and 0 <= j_k < 8 and (i_k, j_k) in cur_Board and Chess_Board.Fig_Pos[(i_k, j_k)]._color != self._color:
				sur.append((i_k, j_k))	
		return sur

	def update_poss_moves(self):
		self.poss_moves = self.get_sourrounding()


class Pawn(Figure):
	def __init__(self, color, position, poss_moves, figure = 'Pawn'):
		Figure.__init__(self, color, position, poss_moves)
		self._figure = figure

	def get_sourrounding(self):
		sur = []
		cur_Board = Chess_Board.get_positions()
		i = self.position[0]
		j = self.position[1]

		if self._color == 0:
			if (i+1, j) not in cur_Board:
				sur.append((i+1, j))
				if i == 1 and (i+2, j) not in cur_Board: 
					sur.append((i+2, j))			
			if (i+1, j+1) in cur_Board and cur_Board[(i+1, j+1)]._color != 0:
				sur.append((i+1, j+1))
			if (i+1, j-1) in cur_Board and cur_Board[(i+1, j-1)]._color != 0:
				sur.append((i+1, j-1))
		else:
			if (i-1, j) not in cur_Board:
				sur.append((i-1, j))
				if i == 6 and (i-2, j) not in cur_Board: 
					sur.append((i-2, j))			
			if (i-1, j+1) in cur_Board and cur_Board[(i-1, j+1)]._color != 1:
				sur.append((i-1, j+1))
			if (i-1, j-1) in cur_Board and cur_Board[(i-1, j-1)]._color != 1:
				sur.append((i-1, j-1))			
		return sur

	def update_poss_moves(self):
		self.poss_moves = self.get_sourrounding()	


def check_if_move_is_possible(start_position, end_position):
	cur_Board = Chess_Board.get_positions()
	if end_position in Chess_Board.Fig_Pos[(start_position)].poss_moves:
		return True
	else:
		return False


def check_if_own_king_in_danger(start_position, end_position):
	current_color = Chess_Board.Fig_Pos[start_position]._color
	position_own_king = ()

	Chess_Board.Fig_Pos[start_position].position = end_position
	Chess_Board.update_positions(start_position, end_position)

	for to_update in Chess_Board.Fig_Pos:
		Chess_Board.Fig_Pos[to_update].update_poss_moves()
		if Chess_Board.Fig_Pos[to_update]._figure == 'King' and Chess_Board.Fig_Pos[to_update]._color == current_color:
			position_own_king = Chess_Board.Fig_Pos[to_update].position

	for figures in Chess_Board.Fig_Pos:
		if Chess_Board.Fig_Pos[figures]._color != current_color and position_own_king in Chess_Board.Fig_Pos[figures].poss_moves:
			print('Move not possible. Own King would be in chess.')
			Chess_Board.Fig_Pos[end_position].position = start_position
			Chess_Board.update_positions(end_position, start_position)
			for to_update in Chess_Board.Fig_Pos:
				Chess_Board.Fig_Pos[to_update].update_poss_moves()	
			return False
	return True


def check_if_checkmate(current_color, start_position, end_position):
	global is_check, check_mate, playing
	is_check = False
	check_mate = False
	enemy_king_pos = ()

	for find_king in Chess_Board.Fig_Pos:
		if Chess_Board.Fig_Pos[find_king]._figure == 'King' and Chess_Board.Fig_Pos[find_king]._color != current_color:
			enemy_king_pos = Chess_Board.Fig_Pos[find_king].position

	who_attacks = []
	attackers_moves = []

	for find_attacker in Chess_Board.Fig_Pos:
		if Chess_Board.Fig_Pos[find_attacker]._color == current_color and enemy_king_pos in Chess_Board.Fig_Pos[find_attacker].poss_moves:
			who_attacks.append(Chess_Board.Fig_Pos[find_attacker].position)
			attackers_moves.extend(Chess_Board.Fig_Pos[find_attacker].poss_moves)

	if not who_attacks:
		return True

	for king_move in Chess_Board.Fig_Pos[enemy_king_pos].poss_moves:
		if king_move not in attackers_moves:
			print('check!')
			is_check = True
			return True

	for find_helpers in Chess_Board.Fig_Pos:
		if Chess_Board.Fig_Pos[find_helpers]._color != current_color and Chess_Board.Fig_Pos[find_helpers]._figure != 'King':
			for helpers_poss_move in Chess_Board.Fig_Pos[find_helpers].poss_moves:
				if helpers_poss_move in attackers_moves:
					old_position = Chess_Board.Fig_Pos[find_helpers].position
					new_position = helpers_poss_move

					Chess_Board.Fig_Pos[old_position].position = new_position
					Chess_Board.update_positions(old_position, new_position)

					for to_update in Chess_Board.Fig_Pos:
						Chess_Board.Fig_Pos[to_update].update_poss_moves()
					if enemy_king_pos not in Chess_Board.Fig_Pos[end_position].poss_moves:
						print('check!')
						is_check = True
						Chess_Board.Fig_Pos[new_position].position = old_position
						Chess_Board.update_positions(new_position, old_position)

						for to_update in Chess_Board.Fig_Pos:
							Chess_Board.Fig_Pos[to_update].update_poss_moves()
						return True

					Chess_Board.Fig_Pos[new_position].position = old_position
					Chess_Board.update_positions(new_position, old_position)

					for to_update in Chess_Board.Fig_Pos:
						Chess_Board.Fig_Pos[to_update].update_poss_moves()				

	print('check mate!')
	check_mate = True
	return True


def check_rochade(current_color, start_position, end_position):
	cur_Board = Chess_Board.get_positions()
	if start_position not in cur_Board or end_position not in cur_Board:
		return False
	p1 = cur_Board[start_position]
	p2 = cur_Board[end_position]
	p1_position = p1.position
	p2_position = p2.position

	if p1._color != p2._color or p1._figure not in ('King', 'Rook') or p2._figure not in ('King', 'Rook'):
		return False

	if p1.already_moved or p2.already_moved:
		return False

	pos_between = []
	if p1.position == (0,0) or p2.position == (0,0):
		pos_between = [(0,1), (0,2), (0,3)]
	elif p1.position == (0,7) or p2.position == (0,7):
		pos_between = [(0,5), (0,6)]
	elif p1.position == (7,0) or p2.position == (7,0):
		pos_between = [(7,1), (7,2), (7,3)]
	elif p1.position == (7,7) or p2.position == (7,7):
		pos_between = [(7,5), (7,6)]

	for check_poss_attack in Chess_Board.Fig_Pos:
		if Chess_Board.Fig_Pos[check_poss_attack].position in pos_between:
			return False
		if Chess_Board.Fig_Pos[check_poss_attack]._color != current_color:
			for positions_between in pos_between:
				if positions_between in Chess_Board.Fig_Pos[check_poss_attack].poss_moves:
					return False

	Chess_Board.Fig_Pos[start_position].position = end_position
	Chess_Board.Fig_Pos[end_position].position = start_position
	Chess_Board.update_position_rochade(start_position, end_position)

	for to_update in Chess_Board.Fig_Pos:
		Chess_Board.Fig_Pos[to_update].update_poss_moves()

	position_own_king = ()
	for to_update in Chess_Board.Fig_Pos:
		if Chess_Board.Fig_Pos[to_update]._figure == 'King' and Chess_Board.Fig_Pos[to_update]._color == current_color:
			position_own_king = Chess_Board.Fig_Pos[to_update].position

	for figures in Chess_Board.Fig_Pos:
		if Chess_Board.Fig_Pos[figures]._color != current_color and position_own_king in Chess_Board.Fig_Pos[figures].poss_moves:	
			Chess_Board.Fig_Pos[end_position].position = start_position
			Chess_Board.Fig_Pos[start_position].position = end_position
			Chess_Board.update_position_rochade(end_position, start_position)

			for to_update in Chess_Board.Fig_Pos:
				Chess_Board.Fig_Pos[to_update].update_poss_moves()			
			return False 
	p1.already_moved = True
	p2.already_moved = True
	return True

def process_input(current_color, start_position, end_position):
	global history_infos_temp

	colors_turn = 'white' if current_color == 1 else 'black'
	history_infos_temp = [colors_turn, Chess_Board.Fig_Pos[start_position]._figure, start_position, end_position]

	cur_Board = Chess_Board.get_positions()
	if start_position not in cur_Board:
		return False

	if current_color != Chess_Board.Fig_Pos[start_position]._color:
		print(f'It´s {colors_turn} turn.')
		return False

	if check_rochade(current_color, start_position, end_position):
		return True
	else:
		pass

	if check_if_move_is_possible(start_position, end_position) and check_if_own_king_in_danger(start_position, end_position) and check_if_checkmate(current_color, start_position, end_position):
		history_infos_temp.append(is_check)
		if Chess_Board.Fig_Pos[(end_position)]._figure in ('King', 'Rook'):
			Chess_Board.Fig_Pos[(end_position)].already_moved = True
		return True
	else:
		return False


def update_history_gui(history_infos_temp):
	global start_count_rounds

	start_count_rounds += 1
	history.append(history_infos_temp)
	sp = history_infos_temp[2]
	se = history_infos_temp[3]

	translate =    {(0,0):'a8', (0,1):'b8', (0,2):'c8', (0,3):'d8', (0,4):'e8', (0,5):'f8', (0,6):'g8', (0,7):'h8', 
					(1,0):'a7', (1,1):'b7', (1,2):'c7', (1,3):'d7', (1,4):'e7', (1,5):'f7', (1,6):'g7', (1,7):'h7', 
					(2,0):'a6', (2,1):'b6', (2,2):'c6', (2,3):'d6', (2,4):'e6', (2,5):'f6', (2,6):'g6', (2,7):'h6',
					(3,0):'a5', (3,1):'b5', (3,2):'c5', (3,3):'d5', (3,4):'e5', (3,5):'f5', (3,6):'g5', (3,7):'h5', 
					(4,0):'a4', (4,1):'b4', (4,2):'c4', (4,3):'d4', (4,4):'e4', (4,5):'f4', (4,6):'g4', (4,7):'h4', 
					(5,0):'a3', (5,1):'b3', (5,2):'c3', (5,3):'d3', (5,4):'e3', (5,5):'f3', (5,6):'g3', (5,7):'h3', 
					(6,0):'a2', (6,1):'b2', (6,2):'c2', (6,3):'d2', (6,4):'e2', (6,5):'f2', (6,6):'g2', (6,7):'h2', 
					(7,0):'a1', (7,1):'b1', (7,2):'c1', (7,3):'d1', (7,4):'e1', (7,5):'f1', (7,6):'g1', (7,7):'h1'}

	hist_out = str(start_count_rounds) + ' ' + str(history_infos_temp[0]) + ' ' + str(history_infos_temp[1]) + ' ' +  translate[sp] + ' ' + translate[se]

	if history_infos_temp[-1]:
		hist_out += ' check'
	if check_mate:
		hist_out += ' check mate'

	history_gui.configure(state='normal')
	history_gui.insert(END, hist_out + '\n')
	history_gui.configure(state='disabled')


def play_game():
	global error, current_color, tkstart, tkend, start_position, end_position, is_check, check_mate, history_infos_temp, history

	is_check = False
	check_mate = False
	start_position = tkstart
	end_position = tkend

	if process_input(current_color, start_position, end_position):
		current_color = 0 if current_color == 1 else 1
		Chess_Board.draw_Board()
		update_history_gui(history_infos_temp)
		error = 0


def main():
	global Chess_Board, current_color, history, start_count_rounds, check_mate

	Chess_Board = Board()
	current_color = 1
	start_count_rounds = 0
	check_mate = False
	history = []
	print('Welcome to this Chess Game. Have fun!')
	Chess_Board.draw_Board()
	for to_update in Chess_Board.Fig_Pos:
		Chess_Board.Fig_Pos[to_update].update_poss_moves()

tk.mainloop()
