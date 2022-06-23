# Task Description - Create a chessboard layout using 2D matrix  

import matplotlib
import matplotlib.pyplot as plt

# Plot a chess board like layout using 2D array and store it in a variable (Hint - can use "0" to get dark block and "1" to get light colored block and create a chessboard which has 7 rows and 7 columns)
# Chessboard image - https://commons.wikimedia.org/wiki/File:AAA_SVG_Chessboard_and_chess_pieces_02.svg
# (Note: After creating 2 rows you can copy those rows 3 more times)

data= [
    [10,0,10,0,10,0,10],
    [0,10,0,10,0,10,0],
    [10,0,10,0,10,0,10],
    [0,10,0,10,0,10,0],
    [10,0,10,0,10,0,10],
    [0,10,0,10,0,10,0],
    [10,0,10,0,10,0,10]
]

plt.imshow(data, cmap="hot")
plt.show()




