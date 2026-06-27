from modified_vigenere_table import vigenere_table
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

def decoderHelper(key:str, encoded: str, grid: List[List], currTextLetterIndex: int, currKeyLetterIndex:int) -> int:
    k = 1 # start from 1 to skip header row where the text is '0'
    while grid[k][0] != key[currKeyLetterIndex]:
        k += 1 # get to the row needed 
    # Gotten to the row needed, now go into that row
    j = 1 # start from 1 because the header column is meant exclusively for key letter matching
    while grid[k][j] != encoded[currTextLetterIndex]:
        j += 1 # get to the column needed
    return j


def decoder(key: str, encoded: str, grid: List[List]):
    # figure out iteration first:
    decoded = []
    pointer = 0
    encoded = encoded.lower()
    for i in range(len(encoded)):
        if pointer == len(key):
            pointer = 0
        if encoded[i].isalpha():
            decodingCol = decoderHelper(key, encoded, grid, i, pointer)
            decoded.append(grid[0][decodingCol])
            pointer = pointer + 1
        else: 
            decoded.append(encoded[i]) # pointer does not change since this thing doesn't count
    return "".join(decoded)

if __name__ == "__main__":
    key = str(input("Enter cipher key: "))
    encoded = str(input("Enter text to be deciphered: "))
    grid = vigenere_table()
    decoded = decoder(key, encoded, grid)
    print(decoded)


