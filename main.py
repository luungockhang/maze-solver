from graphics import *
from maze import Maze

def main():
    win_width = 800
    win_height = 600
    win = Window(win_width,win_height)
    # win.draw_line(Line(Point(1,2),Point(30,40)),"white")
    # win.draw_line(Line(Point(50,60),Point(80,7)),"red")
    # win.draw_line(Line(Point(80,9),Point(7,6)),"blue")
    # cell1 = Cell(win)
    # cell1.draw(10,10,400,400)
    # cell2 = Cell(win)
    # cell2.draw(20,20,500,500)
    
    num_cols = 30
    num_rows = 30
    cols_width = win_width // num_cols
    rows_height = win_height // num_rows
    
    
    new_maze = Maze(0,0,num_cols,num_rows,cols_width,rows_height,win)
    new_maze.solve()
    
    win.wait_for_close()
    
if __name__ == "__main__":
    main()
