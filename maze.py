from cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None, seed = None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        self._seed = seed
        if seed == None:
            random.seed(seed)
        
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
        
    def _create_cells(self):
        for _ in range(self._num_cols):
            column = []
            for _ in range(self._num_rows):
                column.append(Cell(self._window))
            self._cells.append(column)
        
        if self._window is not None:
            for i in range(len(self._cells)):
                for j in range(len(self._cells[i])):
                    self._draw_cell(i,j)

    def _draw_cell(self,i,j):
        # calculate cell top left and bottom right
        # must add the starting x y of the maze
        # top left
        cell_x1 = self._x1 + i * self._cell_size_x
        cell_y1 = self._y1 + j * self._cell_size_y
        # bottom right
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y2 = cell_y1 + self._cell_size_y
        self._cells[i][j].draw(cell_x1,cell_y1,cell_x2,cell_y2)
        self._animate()
    
    def _animate(self):
        if self._window is None:
            return
        self._window.redraw()
        time.sleep(0.025)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1,self._num_rows-1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            # Initialize the list and pointers
            cells_to_visit = []
            current_cell = self._cells[i][j]
            top_adj = None
            bottom_adj = None
            left_adj = None
            right_adj = None
            
            #top_adj = (i, j-1)
            if j-1 >= 0 and not self._cells[i][j-1]._visited:
                top_adj = (i,j-1)
                cells_to_visit.append(top_adj)
            #bottom_adj = (i,j+1)
            if j+1 < len(self._cells[i]) and not self._cells[i][j+1]._visited:
                bottom_adj = (i,j+1)
                cells_to_visit.append(bottom_adj)
            #left_adj = (i-1,j)
            if i-1 >= 0 and not self._cells[i-1][j]._visited:
                left_adj = (i-1,j)
                cells_to_visit.append(left_adj)
            #right_adj = (i+1,j)
            if i+1 < len(self._cells) and not self._cells[i+1][j]._visited:
                right_adj = (i+1,j)
                cells_to_visit.append(right_adj)
            
            if len(cells_to_visit) == 0:
                self._draw_cell(i,j)
                return

            next = random.randrange(len(cells_to_visit))
            # next tuple
            coords = cells_to_visit[next]
            next_cell = self._cells[coords[0]][coords[1]]
            
            if cells_to_visit[next] == top_adj:
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            elif cells_to_visit[next] == bottom_adj:
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            elif cells_to_visit[next] == left_adj:
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            elif cells_to_visit[next] == right_adj:
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
            
            self._break_walls_r(coords[0],coords[1])

    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell._visited = False
    
    def solve(self):
        result = self._solve_r(0,0)
        return result
        
    def _solve_r(self, i, j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell._visited = True
        if self._cells[i][j] == self._cells[self._num_cols-1][self._num_rows-1]:
            return True
        # Look right -> down -> top -> left
        right = (i+1, j)
        down = (i, j+1)
        top = (i, j-1)
        left = (i-1, j)
        
        # directions = [right, down, top, left]
        # Right
        if i + 1 < self._num_cols:
            next_cell = self._cells[i+1][j]
            if not next_cell._visited and current_cell.has_right_wall:
                move = self.solve_r(i+1, j)
                if move:
                    return True
                