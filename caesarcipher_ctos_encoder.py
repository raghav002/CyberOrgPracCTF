# C to S
#diff = ord('s') - ord('c')
#print(diff)
# Shift ahead of 16 

# If we're at 0, we want to go to 16

# 97 - 97 + 16 = 16, 16 % 26 = 16, 97 + 16 = 113

def encoder(text:str)->str:
    encoded = []
    for c in text:
        if c.isalpha():
            truepos = ((ord(c) - 97 + 16) % 26) + 97
            encoded.append(chr(truepos))
        else:
            encoded.append(c)
    return "".join(encoded)

if __name__ == "__main__":
    text = str(input("Enter string you want to encode using N to S caesar cipher: "))
    encoded = encoder(text)
    print(encoded)