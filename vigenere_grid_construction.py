# 4 components:
# the table
# the ciphertext
# the key
# the decoded message

# process of decoding
# go to first letter of key + first letter of cypher text
# match the first letter of key to the time in the grid that it occurs first, in the first column
# then, in that row you found the match in, go horizontally across until you find the first letter of the cipher text
# then, go up to the first row from that column, to get the decoded letter
# move up to the second letter of the key + second letter of cypher text
# skip non-alphabetical elements
# skip spaces
# when you reach the end of the key, go back to the first letter 
# you get the message

# the grid if 27 x 27, with [0,0] being the empty space
# the first row contains all 26 letters normally (after [0,0])
# each subsequent row has the j-1th letter repeated (for example, in the second row, A is repeated twice, third row B is repeated twice, etc.)
# Whatever letter starts first in each row, is repeated twice (AABCDE...) and once you reach Z, you wrap around back to A...

def vigenere_table()->List[List]:
    rows = cols = 27
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    grid[0][0] = 0
    for j in range(1, 27):
        grid[0][j] = chr(96+j)
        grid[j][0] = chr(96+j)

    for i in range(1, 27):
        for j in range(1, 27):
            if j==1:
                grid[i][j] = grid[i][0]
            else:
                # grid[1][1] = b, grid[1][2] = c
                # ord(b) = 98
                # We want 99, then wrap around back to 97
                # So let's say we go 124 at some point 
                # We need to go back to 97
                # We specify that if the ord of the previous thing is greater than 123, change the calculation to ord of previous thing 
                # -97 % 26 + 97 perhaps
                prevpos = ord(grid[i][j-1])
                grid[i][j] = chr(((prevpos + 1 - 97) % 26) + 97)
    return grid

if __name__ == "__main__":
    testtable = vigenere_table()
    for row in testtable:
        print(row)