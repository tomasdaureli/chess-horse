from graphics import *
from time import sleep

#Config
tile_size = 50

def draw_chessboard(win, N):
    colors = ["white", "grey"]
    for row in range(N):
        for col in range(N):
            x = col * tile_size
            y = row * tile_size
            square = Rectangle(Point(x, y), Point(x + tile_size, y + tile_size))
            square.setFill(colors[(row + col) % 2])
            square.draw(win)

def display_matrix_on_board(win, matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            # Calculate center position of the tile
            x = col * tile_size + tile_size / 2
            y = row * tile_size + tile_size / 2
            # Convert the integer to a string and display it on the tile
            val = "-"
            if matrix[row][col] != -1:
                val = matrix[row][col]
            number_text = Text(Point(x, y), str(val))
            number_text.setSize(20)  # Adjust text size if needed
            number_text.draw(win)

def add_knight(win, row, col):
    # Positioning the knight in the center of the given tile
    knight_pos_x = col * tile_size + tile_size / 2
    knight_pos_y = row * tile_size + tile_size / 2
    # Display the knight symbol (♞)
    knight = Text(Point(knight_pos_x, knight_pos_y), "♞")
    knight.setSize(36)  # Set size to make it fit the tile
    knight.setStyle("bold")
    knight.setTextColor("red")
    knight.draw(win)
    return knight

def displayFrame(win, matrix, knight, message=None):
    # Draw the chessboard and display the matrix
    draw_chessboard(win, len(matrix))
    display_matrix_on_board(win, matrix)
    add_knight(win, knight[0], knight[1])
    if message is not None:
        # Display a message below the board
        text = Text(Point(win.getWidth() / 2, win.getHeight()-tile_size), message)
        text.setSize(12)
        text.draw(win)

