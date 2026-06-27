# N to X shift: each of the letters of the alphabet is shifted to the right by 10
# A becomes K, B->L, C->M, D->N
# BAD -> LKN

# Function that shifts entered string to the left by 10, letter-by-letter, alphabet position-wise
def deshift(coded: str) -> str:
    decoded = []
    coded = coded.lower()

    # How to wrap numbers around? We have 1 to 26.
    # If we're at position 26, we want to go to 10
    # 10+26 = 36
    # 36 % 26? Works
    # If at 23, we go to 7
    # 33 % 26? Works

    # Using ord, a = 97, z = 122
    # If at 119, we want to go to 104
    # 119 - 97 gives us how it would be present if we went from 0-25
    # 119 - 97 = 23 
    # 23 + 10 = 33, 33%26 = 7, 7+97 = 104

    for c in coded:
        # Change
        if c.isalpha():
            posval = ord(c)
            actualpos = ((posval - 97 - 10) % 26) + 97
            truec = chr(actualpos) 
            decoded.append(truec)
        else:
            decoded.append(c)
    return "".join(decoded)

if __name__ == "__main__":
    coded = str(input("Enter the string you want decoded using an N->X Caesar Cipher: "))
    decoded = deshift(coded)
    print(decoded)
    #print(ord('z')) # 97
