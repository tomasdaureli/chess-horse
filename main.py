import time
from impleBacktracking import start_knights_tourBT 
from graphics import *

# Start Knight's Tour
try:
    N = int(input("Enter board size (n x n): "))
    if N < 1:
        raise ValueError("Board size must be positive.")
    
    Irow = int(input("Enter initial position row: "))
    if Irow < 0 or Irow >= N:
        raise ValueError("Initial row must be within board bounds.")
    
    Icol = int(input("Enter initial position column: "))
    if Icol < 0 or Icol >= N:
        raise ValueError("Initial column must be within board bounds.")
    
    algorithm = int(input("Enter algorithm: \n 1 - Backtracking \n 2 - Branch & Bound\n"))
    if algorithm not in [1, 2]:
        raise ValueError("Invalid algorithm choice.")

    # Set up the window
    win_size = 50 * N
    win = GraphWin("TP Uade Progra 3", win_size, win_size+100)

    if algorithm == 1:
        #todo: tendría que aceptar posición inicial del caballo
        start_knights_tourBT(N, win)
    else:
        #todo implementar start_knights_tourBB
        start_knights_tourBB(N, Irow, Icol)

    win.getMouse()
    win.close()
except ValueError as e:
    print(f"Error: {e}")