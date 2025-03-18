from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)

    maze = Maze(50, 50, 10, 10, 50, 50, win)
    maze._create_cells()
    win.wait_for_close()

    '''
    c1 = Cell(win)
    
    c1.has_right_wall = False
    c1.draw(50, 50, 100, 100)

    c2 = Cell(win)
    c2.has_left_wall = False
    c2.draw(100, 50, 150, 100)

    c1.draw_move(c2, True)

    win.wait_for_close()'
    '''




main()
