import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    def test_maze_create_cells_smaller(self):
        num_cols = 5
        num_rows = 3
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m2._cells),
            num_cols,
        )
        self.assertEqual(
            len(m2._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_larger(self):
        num_cols = 10
        num_rows = 10
        m3 = Maze(0, 0, num_rows, num_cols, 5, 5)
        self.assertEqual(
            len(m3._cells),
            num_cols,
        )
        self.assertEqual(
            len(m3._cells[0]),
            num_rows,
        )
    def test_break_entrance_and_exit(self):
        num_cols = 10
        num_rows = 10
        m4 = Maze(0, 0, num_rows, num_cols, 10, 5)
        self.assertEqual(
            m4._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m4._cells[-1][-1].has_bottom_wall,
            False,
        )
    def test_cell_visited_reset(self):
        num_cols = 10
        num_rows = 10
        m5 = Maze(0,0,num_rows,num_cols,10,10)
        for i in range(5):
            m5._cells[i][i]._visited = True
        
        m5._reset_cells_visited()
        for x in range(num_cols):
            for y in range(num_rows):
                self.assertFalse(m5._cells[x][y]._visited)
if __name__ == "__main__":
    unittest.main()