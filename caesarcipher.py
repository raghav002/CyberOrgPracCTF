# N to X shift: each of the letters of the alphabet is shifted to the right by 10
# A becomes K, B->L, C->M, D->N
# BAD -> LKN

# Function that shifts entered string to the left by 10, letter-by-letter, alphabet position-wise
def deshift(coded: str) -> str:
    decoded = []
    coded = coded.lower()
    for c in coded:
        truec = chr(ord(c)-10)
        decoded.append(truec)
    return "".join(decoded)

if __name__ == "__main__":
    coded = str(input("Enter the string you want decoded using an N->X Caesar Cipher: "))
    decoded = deshift(coded)
    print(decoded)

