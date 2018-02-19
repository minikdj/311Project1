from tkinter import *
#loop to use the console version of the game

#list used to keep the state of the game
game_arr = [[0 for x in range(3)] for y in range(3)]
turn = 'x'
game_over = False

#loop for console view
def console_view():
	#while(game_over == False):
	for x in range(3):
		for y in range(3):
			print(game_arr[x][y], end='')
		print('\n')	
	#need to ask for the user input
	
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
		turn = 'o'
	else:
		draw_o(x,y)
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
