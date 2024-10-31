from animation import *

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

def solve_knights_tour(x, y, move_count, board, N, win):
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
        displayFrame(win, board, (next_x, next_y))
        time.sleep(0.2)  # Pause to see the move, commented for the speed
        #print(f"Move {move_count}: Knight to ({next_x}, {next_y})")

        if solve_knights_tour(next_x, next_y, move_count + 1, board, N, win):
            return True

        # Backtrack
        board[next_x][next_y] = -1

    return False

def start_knights_tourBT(N, win):
    # Initialize board
    board = [[-1 for _ in range(N)] for _ in range(N)]
    # Start in center or (0, 0) if size < 5 for better chances
    start_x, start_y = (N // 2, N // 2) if N >= 5 else (0, 0)
    board[start_x][start_y] = 0

    if solve_knights_tour(start_x, start_y, 1, board, N, win):
        print("Completed Knight's Tour:")
        displayFrame(win, board, (start_x, start_y), "Solution found")
    else:
        print("No solution found for the knight's tour.")
        displayFrame(win, board, (start_x, start_y), "No solution found")