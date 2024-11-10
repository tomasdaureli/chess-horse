import time

def inicializar_tablero(tamaño):
    """Inicializar un tablero de ajedrez vacío con -1 para indicar casillas no visitadas."""
    return [[-1 for _ in range(tamaño)] for _ in range(tamaño)]

def es_movimiento_valido(x, y, tablero):
    """Verificar si el movimiento es válido: dentro de los límites y no visitado aún."""
    tamaño = len(tablero)
    return 0 <= x < tamaño and 0 <= y < tamaño and tablero[x][y] == -1

def contar_movimientos_futuros(x, y, tablero):
    """Contar los movimientos futuros válidos desde la posición (x, y) en el tablero."""
    tamaño = len(tablero)
    movimientos_del_caballo = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    contador = 0
    for dx, dy in movimientos_del_caballo:
        nuevo_x, nuevo_y = x + dx, y + dy
        if es_movimiento_valido(nuevo_x, nuevo_y, tablero):
            contador += 1
    return contador

def resolver_recorrido_del_caballo(tablero, x, y, contador_de_movimientos, total_movimientos):
    """Intentar resolver el problema del recorrido del caballo utilizando backtracking con heurística de Warnsdorff."""
    tamaño = len(tablero)
    if contador_de_movimientos == tamaño * tamaño:
        return True

    # Movimientos posibles del caballo
    movimientos_del_caballo = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]

    # Ordenar movimientos usando la heurística de Warnsdorff
    movimientos_del_caballo = sorted(
        movimientos_del_caballo,
        key=lambda move: contar_movimientos_futuros(x + move[0], y + move[1], tablero)
    )

    for dx, dy in movimientos_del_caballo:
        total_movimientos[0] += 1
        nuevo_x, nuevo_y = x + dx, y + dy
        if es_movimiento_valido(nuevo_x, nuevo_y, tablero):
            tablero[nuevo_x][nuevo_y] = contador_de_movimientos
            if resolver_recorrido_del_caballo(tablero, nuevo_x, nuevo_y, contador_de_movimientos + 1, total_movimientos):
                return True
            tablero[nuevo_x][nuevo_y] = -1  # Retroceder
    return False

def ResolverConPoda(size, start_x, start_y):
    t1 = time.process_time()
    board = inicializar_tablero(size)
    board[start_x][start_y] = 0  # Inicializar la posición de inicio con el primer movimiento
    contador_de_mov = [0]
    configMsg = f"Estrategia: Branch & Bound\nN:{size} Inicio: {start_x},{start_y}\n"
    if resolver_recorrido_del_caballo(board, start_x, start_y, 1, contador_de_mov):
        message = f"{configMsg}Solución encontrada en\n {contador_de_mov[0]} iteraciones.\n"
    else:
        message = f"No se encontró solución en\n {contador_de_mov[0]} iteraciones.\n"
    t2 = time.process_time()
    elapsed_time = t2 - t1
    message = message + f"\nTiempo de ejecución:\n {'menor a 0.00001' if elapsed_time < 0.00001 else f'{elapsed_time:0,.5f}'} segundos."
    return (board, message)