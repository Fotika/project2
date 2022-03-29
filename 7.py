def decrypt(encrypted, distance):
    #start coding here
    print("Decryption results")
    # decrypted = set()
    for word in encrypted:
        code = ""
        for ch in word:
            cipherValue = ord(ch) - distance
            if cipherValue < ord('a'):
                cipherValue = ord('z') - distance - (ord(ch) - ord('a') - 1)
            code += chr(cipherValue)
        print(word + "->" + code)
    return


def main():
    words = set()
    encrypted = set()
    distance = int(input("Enter a distance value between 0 and 25: "))
    for i in range(3):
        words.add(input("Enter a one-word, lowercase message: "))
    for word in words:
        code = ""
        for ch in word:
            cipherValue = ord(ch) + distance
            if cipherValue > ord('z'):
                cipherValue = ord('a') + distance - (ord('z') - ord(ch) + 1)
            code += chr(cipherValue)
        encrypted.add(code)
    print("The encrypted set includes", encrypted)
    decrypt(encrypted, distance)

main()
