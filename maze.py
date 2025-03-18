from time import sleep

from cell import Cell



class Maze:

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        
        self._cells = []

    def _create_cells(self):
        for row_index in range(self._num_rows):
            new_row = []
            for col_index in range(self._num_cols):
                cell = Cell(self._win)
                new_row.append(cell)
            self._cells.append(new_row)

        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        x1 = self._x1 + (i * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)

        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)

    def _animate(self):
        self._win.redraw()
        sleep(.05)

