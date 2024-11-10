from impleBacktracking import ResolverConBacktracking 
from impleBranchBound import ResolverConPoda
from graphics import *

"""
UADE - Universidad Argentina de la Empresa
Materia: DISEÑO Y ANÁLISIS DE ALGORITMOS
Profesor: Bianchimano, Omar Nestor Cristian
Año: 2024

Trabajo Práctico Obligatorio (TPO): Recorrido del Caballo de Ajedrez
Grupo 1

Integrantes:
    - D'Aureli, Tomas (1122820)
    - Fuertes, Noelia Miranda (1117648)
    - Gilabert, Germán Victor (1118036)
    - Toloza, Gonzalo (1153053)
"""

## Menu ###
try:
    N = int(input("Ingrese el tamaño del tablero (n x n): "))
    if N < 1:
        raise ValueError("El tamaño del tablero debe ser positivo.")
    
    Irow = int(input("Ingrese la fila de la posición inicial: "))
    if Irow < 0 or Irow >= N:
        raise ValueError("La fila inicial debe estar dentro de los límites del tablero.")
    
    Icol = int(input("Ingrese la columna de la posición inicial: "))
    if Icol < 0 or Icol >= N:
        raise ValueError("La columna inicial debe estar dentro de los límites del tablero.")
    
    algorithm = int(input("Ingrese el algoritmo: \n 1 - Backtracking \n 2 - Branch & Bound\n"))
    if algorithm not in [1, 2]:
        raise ValueError("Opción de algoritmo no válida.")

    # Set up de la ventana
    win_size = 50 * N
    win = GraphWin("Uade TPO Progra 3 G1", win_size, win_size+150)

    if algorithm == 1:
        result = ResolverConBacktracking(N, Irow, Icol)
    else:
        result = ResolverConPoda(N, Irow, Icol)
    
    displayFrame(win, result[0], result[1])

    win.getMouse()
    win.close()
except ValueError as e:
    print(f"Error: {e}")

