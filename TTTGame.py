from tkinter import *
#loop to use the console version of the game

#list used to keep the state of the game
game_arr = [['-' for x in range(3)] for y in range(3)]
turn = 'x'
game_over = False

def check_vertical_win():
	global game_over
	for i in range(3):
		if game_arr[i][0] == turn and  game_arr[i][1] == turn and game_arr[i][2] == turn:
			game_over = True

def check_horizontal_win():
	global game_over
	for i in range(3):
		if game_arr[0][i] == turn and game_arr[1][i] == turn and game_arr[2][i] == turn:
			game_over = True	

def check_diagonal_win():
	global game_over
	if game_arr[0][0] == turn and game_arr[1][1] == turn and  game_arr[2][2] == turn:
		game_over = True

	elif game_arr[2][0] == turn and game_arr[1][1] == turn and game_arr[0][2] == turn:
		game_over = True

def model():
	check_vertical_win()
	check_horizontal_win()
	check_diagonal_win()

#sends the current input to the model
def controller(tup):
	global game_arr
	game_arr[tup[0]][tup[1]] = turn
	model()
	if game_over == True:
		print('Turn ', turn, ' won the game')
		exit()

#loop for console view
def console_view():
	global turn
	while(True):
		text = input('Enter coordinates in form of x,y: ')
		coordinates = (int(text[0]),int(text[2]))
		print(coordinates)
		controller(coordinates)
		if turn == 'x':
			turn = 'o'
		else:
			turn = 'x'
		for x in range(3):
			for y in range(3):
				print(game_arr[x][y], end='')
			print('\n')	
	
#loop to use the gui
root = Tk()

def get_x_quadrant(x):
	if(x < 100):
		return 50
	elif(x < 200):
		return 150
	else:
		return 250

def get_y_quadrant(y):
	if(y < 100):
		return 50
	elif(y < 200):
		return 150
	else:
		return 250
def get_cell(x,y):
	if x == 50:
		new_x = 0
	elif x == 150:
		new_x = 1
	elif x == 250:
		new_x = 2
	if y == 50:
		new_y = 0
	elif y == 150:
		new_y = 1
	else:
		new_y = 2
	
	quadrant = (new_x, new_y)
	return quadrant

def draw_x(x,y):
	c.create_line(x-50,y-50,x+50,y+50)
	c.create_line(x-50,y+50,x+50,y-50)

def draw_o(x,y):
	c.create_oval(x-50,y-50,x+50,y+50)

def callback(event):
	global turn
	c.focus_set()
	x = get_x_quadrant(event.x)
	y = get_y_quadrant(event.y)
	if(turn == 'x'):
		draw_x(x,y)
		controller(get_cell(x,y))
		turn = 'o'
	else:
		draw_o(x,y)
		controller(get_cell(x,y))
		turn = 'x'


frame = Frame(root, width=300, height=300)
frame.pack()
c = Canvas(frame, bg='white', width=300, height=300)
c.pack(fill=BOTH, expand=1)

c.create_line(1,100,300,100)
c.create_line(1,200,300,200)
c.create_line(100,1,100,300)
c.create_line(200,1,200,300)

c.bind("<Button-1>", callback)
frame.pack()


#if the command line argument is 1, use the gui
#if the command line argument is not 1, use the console view
if (sys.argv[1] == '1'):
	#using the gui view
	root.mainloop()
else:
	#using the console view 
	console_view()
