from tkinter import Tk, BOTH, Canvas
import graphics_config

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("The Maze")
        self.__canvas = Canvas(self.__root, width=width, height=height,background=graphics_config.BACKGROUND_COLOR)
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW",self.close)
        
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__ (self, point_one, point_two):
        self.point_one = point_one
        self.point_two = point_two

    def draw(self, canvas, fill_color):
        canvas.create_line(self.point_one.x, self.point_one.y,
                           self.point_two.x,self.point_two.y,
                           fill=fill_color,
                           width=2)

