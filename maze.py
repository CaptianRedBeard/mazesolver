from time import sleep
import random

from cell import Cell



class Maze:

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):

        if seed:
            random.seed(seed)

        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _create_cells(self):
        for row_index in range(self._num_cols):
            new_row = []
            for col_index in range(self._num_rows):
                cell = Cell(self._win)
                new_row.append(cell)
            self._cells.append(new_row)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        # Catches possible nil needed for testing
        if self._win is None:
            return

        x1 = self._x1 + (i * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)

        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)

    def _animate(self):
        # Catches possible nil needed for testing
        if self._win is None:
            return
        
        self._win.redraw()
        sleep(.05)

    def _break_entrance_and_exit(self):
        
        entrance = ['top', 'left']
        exit = ['bottom', 'right']

        entrance = random.choice(entrance)
        exit = random.choice(exit)

        if entrance == 'top':
            self._cells[0][0].has_top_wall = False
        else:
            self._cells[0][0].has_left_wall = False

        self._draw_cell(0, 0)

        if exit == 'bottom':
            self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        else:
            self._cells[self._num_cols - 1][self._num_rows - 1].has_right_wall = False

        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
      
        while True:

            possible_moves = []
         
            # check above
            if j != 0:
                if not self._cells[i][j-1].visited:
                    possible_moves.append((i, j-1))
            
            # check below
            if j != self._num_rows - 1:
                 if not self._cells[i][j+1].visited:
                    possible_moves.append((i, j+1))

            # check left
            if i != 0:
                if not self._cells[i-1][j].visited:
                    possible_moves.append((i-1, j))


            # check right

            if i != self._num_cols - 1:
                if not self._cells[i+1][j].visited:
                    possible_moves.append((i+1, j))


            if len(possible_moves) == 0:
                self._draw_cell(i, j)
                return
            
            next_cell = random.choice(possible_moves)

            # need to break down both walls to next cell

            ni, nj = next_cell

            
            # if ni is greater the new block is to the right
            if i < ni:
                self._cells[i][j].has_right_wall = False
                self._cells[ni][nj].has_left_wall = False

            if i > ni:
                self._cells[i][j].has_left_wall = False
                self._cells[ni][nj].has_right_wall = False

            # if nj is greater the new block is to the bottom
            if j < nj:
                self._cells[i][j].has_bottom_wall = False
                self._cells[ni][nj].has_top_wall = False

            if j > nj:
                self._cells[i][j].has_top_wall = False
                self._cells[ni][nj].has_bottom_wall = False


            self._break_walls_r(next_cell[0], next_cell[1])
