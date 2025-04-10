from graphics import *
from maze import Maze

def main():
    win = Window(800,600)
    # win.draw_line(Line(Point(1,2),Point(30,40)),"white")
    # win.draw_line(Line(Point(50,60),Point(80,7)),"red")
    # win.draw_line(Line(Point(80,9),Point(7,6)),"blue")
    # cell1 = Cell(win)
    # cell1.draw(10,10,400,400)
    # cell2 = Cell(win)
    # cell2.draw(20,20,500,500)
    new_maze = Maze(100,100,10,11,50,50,win)
    
    win.wait_for_close()
    
if __name__ == "__main__":
    main()
