from graphics import Line, Point

class Cell:
    # Init a cell with top-left, bottom-right coords and the window it's on
    def __init__(self,window=None):
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True
        self.has_right_wall = True
        self._window = window
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._visited = False
    
    # Draw the cell with top-left, bottom-right coords and the canvas it's drawn on
    def draw(self, x1,y1,x2,y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        top_left = Point(x1,y1)
        top_right = Point(x2,y1)
        bottom_left = Point(x1,y2)
        bottom_right = Point(x2,y2)
        if self._window is not None:
            #  Draw top wall
            line = Line(top_left,top_right)
            if self.has_top_wall:
                self._window.draw_line(line)
            else:
                self._window.draw_line(line,"white")
            #  Draw bottom wall
            line = Line(bottom_left,bottom_right)
            if self.has_bottom_wall:
                self._window.draw_line(line)
            else:
                self._window.draw_line(line,"white")
            #  Draw left wall
            line = Line(top_left,bottom_left)
            if self.has_left_wall:
                self._window.draw_line(line)
            else:
                self._window.draw_line(line,"white")
            #  Draw right wall
            line = Line(top_right,bottom_right)
            if self.has_right_wall:
                self._window.draw_line(line)
            else:
                self._window.draw_line(line,"white")
            
    # Draw a path (line) from the center of this cell to that of next cell
    def draw_move(self,to_cell,undo=False):
        x1 = (self._x1 + self._x2) // 2
        y1 = (self._y1 + self._y2) // 2
        x2 = (to_cell._x1 + to_cell._x2) // 2
        y2 = (to_cell._y1 + to_cell._y2) // 2
        line_color = "red"
        if undo:
            line_color = "gray"
        line = Line(Point(x1,y1),Point(x2,y2))
        self._window.draw_line(line,line_color)
            