#
# need install requirements.txt
# pip install -r requirements.txt
#


import math
from graphics import *
from screeninfo import get_monitors
from NQueensGenetic import NQueensGenetic




####################### helpers ###########################


def calc_grid_size(n,w,h):
    x , y = (w*0.75/n) , (h/n)
    return x,y















############################ Global variables ###############################


screens = get_monitors()
width = screens[0].width*0.95 if len(screens) > 0 else 600
height = screens[0].height*0.8 if len(screens) > 0 else 600
win = GraphWin("NQueens Genetic by tim", width, height)





################## SIDE MENU #######################

side_menu_color = color_rgb(0, 151, 167)
side_menu_size = width*0.25

sideMenuBackground = Rectangle(Point(0, 0), Point(side_menu_size, height))
sideMenuBackground.setFill(side_menu_color)
sideMenuBackground.setWidth(0)
sideMenuBackground.draw(win)


sideMenuTitle = Text(Point(side_menu_size/2, height*0.10), "N Queens\nGenetic 1.0")
sideMenuTitle.setTextColor(color_rgb(255, 255, 255))
sideMenuTitle.setStyle("bold")
sideMenuTitle.setSize(18)
sideMenuTitle.draw(win)

algoritm_parameters = {
    "N": 20, "pop_size": 20, "torn_size": 80,
    "mut_prob": 0.1, "cross_prob": 0.95,  "generations": 1000
}

parameters_labels = []
parameters_entrys = []
x_,y_ = side_menu_size/2,height*0.10 + 60
for parameter, value in algoritm_parameters.items():
    temp_text = Text(Point(x_,y_), str(parameter.capitalize()))
    temp_text.setTextColor("white")
    temp_text.setStyle("bold")
    temp_text.setSize(12)
    temp_text.draw(win)

    temp_entry = Entry(Point(x_,y_+30), 5)
    temp_entry.setText(str(value))
    temp_entry.setFill(side_menu_color)
    temp_entry.setStyle("bold")
    temp_entry.setTextColor("white")

    temp_entry.draw(win)
    
    y_+= 60
    parameters_labels.append(temp_text)
    parameters_entrys.append(temp_entry)


button_start = Text(Point(side_menu_size/2,height-40), "Start Simulation")
button_start.setTextColor("white")
button_start.setStyle("bold")
button_start.draw(win)



x_grid,y_grid = calc_grid_size(algoritm_parameters["N"], width, height)
grid = {}   
queens = []
for line in range(algoritm_parameters["N"]):
    for col in range(algoritm_parameters["N"]):
        temp_w = Rectangle(Point(col*x_grid + side_menu_size, y_grid*line),Point((col+1)*x_grid + side_menu_size, y_grid*(line+1)))
        if (col % 2 != 0 and line % 2 != 0) or (col % 2 == 0 and line % 2 == 0):
            temp_w.setFill("white")
        elif col % 2 == 0 and line % 2 != 0 or (col % 2 != 0 and line % 2 == 0):
            temp_w.setFill("black")
        temp_w.draw(win)
        grid[(line, col)] = temp_w
    x = (x_grid/2) + side_menu_size
    y = (y_grid*(line+1)) - (y_grid/2)
    queen = Circle(Point(x,y),(x_grid/y_grid)*math.pi**2)
    queen.setFill("red")
    queen.draw(win)
    queens.append(queen)
nqueens = NQueensGenetic(N=algoritm_parameters["N"], mut_prob=0.15, cross_prob=0.99)

win.getMouse()

for queen, generation in nqueens.run(True, False, 20):
    if queen is not None:
        for id,gen in enumerate(queen.gens):
            queens[id].move( ((x_grid*(gen+1))  - (x_grid/2)  +side_menu_size - queens[id].getCenter().getX()),0)
            win.master.title("NQueens Genetic by tim | Geração - {} / Melhor Score - {}".format(generation, queen.score))
    else:   
        break



win.getMouse()
