from tkinter import *

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
	c.focus_set()
	x = get_x_quadrant(event.x)
	y = get_y_quadrant(event.y)
	draw_o(x,y)
	draw_x(x,y)


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

root.mainloop()

