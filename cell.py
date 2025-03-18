from graphics import Line, Point

class Cell:

    def __init__(self, window=None):
        self._win = window

        self._x1 = None
        self._y1 = None

        self._x2 = None
        self._y2 = None

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self, x1, y1, x2, y2, fill_color = 'black'):

        self._x1 = x1
        self._y1 = y1

        self._x2 = x2
        self._y2 = y2

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, fill_color)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, fill_color)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, fill_color)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, fill_color)
            
    def center(self):
        centerx = (self._x1 + self._x2) / 2
        centery = (self._y1 + self._y2) /2

        return centerx, centery

    def draw_move(self, to_cell, undo=False):
        fill_color = 'red'
        if undo:
            fill_color = 'grey'
        
        x1, y1 = self.center()
        x2, y2 = to_cell.center()

        line = Line(Point(x1, y1), Point(x2, y2))
        self._win.draw_line(line, fill_color)