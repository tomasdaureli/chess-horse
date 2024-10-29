import time

# All possible moves for the knight
horse_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]


def is_valid_move(x, y, board, N):
    """Check if the move is within bounds and not yet visited."""
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1


def count_next_moves(x, y, board, N):
    """Counts possible moves from the current position."""
    count = 0
    for dx, dy in horse_moves:
        if is_valid_move(x + dx, y + dy, board, N):
            count += 1
    return count


def solve_knights_tour(x, y, move_count, board, N):
    """Backtracking with Warnsdorff's heuristic to solve the knight's tour problem."""
    # If tour is complete
    if move_count == N * N:
        return True

    # Order moves by minimum onward moves
    possible_moves = []
    for dx, dy in horse_moves:
        next_x, next_y = x + dx, y + dy
        if is_valid_move(next_x, next_y, board, N):
            possible_moves.append(
                (count_next_moves(next_x, next_y, board, N), next_x, next_y)
            )
    possible_moves.sort()  # Sort moves by the fewest onward moves

    # Attempt each move in order
    for _, next_x, next_y in possible_moves:
        board[next_x][next_y] = move_count
        print_board(board, N, horse_pos=(next_x, next_y))  # Show board state
        # time.sleep(0.2)  # Pause to see the move, commented for the speed
        print(f"Move {move_count}: Knight to ({next_x}, {next_y})")

        if solve_knights_tour(next_x, next_y, move_count + 1, board, N):
            return True

        # Backtrack
        board[next_x][next_y] = -1

    return False


def start_knights_tour(N):
    # Initialize board
    board = [[-1 for _ in range(N)] for _ in range(N)]
    # Start in center or (0, 0) if size < 5 for better chances
    start_x, start_y = (N // 2, N // 2) if N >= 5 else (0, 0)
    board[start_x][start_y] = 0

    if solve_knights_tour(start_x, start_y, 1, board, N):
        print("Completed Knight's Tour:")
        print_board(board, N)
    else:
        print("No solution found for the knight's tour.")


def print_board(board, N, horse_pos=None):
    """Prints the board showing 'C' for the knight's current position."""
    for i in range(N):
        row = []
        for j in range(N):
            if horse_pos == (i, j):
                row.append(" C")
            elif board[i][j] == -1:
                row.append("--")
            else:
                row.append(f"{board[i][j]:2}")
        print(" ".join(row))
    print("\n" + "=" * 20 + "\n")


# Start Knight's Tour
try:
    N = int(input("Enter board size (n x n): "))
    if N < 1:
        raise ValueError("Board size must be positive.")
    start_knights_tour(N)
except ValueError as e:
    print(f"Error: {e}")
