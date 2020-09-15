import sys

def genKey(plaintext , key):
    key = list(key)
    if len(plaintext) == len(key):
        return(key)
    else:
        key = list(key)
        for i in range(len(plaintext) - len(key)):
            key.append(key[i%len(key)])
        return ("".join(key))

def encrypt(plaintext , key):
    key = genKey(plaintext ,key)
    cipher = []

    for i in range(len(plaintext)):
        temp = (ord(plaintext[i]) + ord(key[i])) % 26
        temp = temp + ord('A')
        cipher.append(chr(temp))
    
    cipherText = "".join(cipher)
    return cipherText

def decrypt(plaintext , key):
    key = genKey(plaintext ,key)
    cipher = []

    for i in range(len(plaintext)):
        temp = ((ord(plaintext[i]) - ord(key[i]))+ 26) % 26
        temp = temp + ord('A')
        cipher.append(chr(temp))
    cipherText = "".join(cipher)
    return cipherText

def main():
    while True:
        print()
        print("-"*35)
        print("-"*10 + "Vigenere Cipher" +"-"*10)
        plaintext = ""
        key = ""
        print("-"*35)
        print()
        plaintext = input("[*] Text: ").upper()
        key = input("[*] Key: ").upper()
        print("-"*35)
        choice = input("[*] Action\n[1] Encrypt\n[2] Decrypt\n[0] Exit\n[>] ")
        
        if choice == "1":
            print()
            print("Encrypted Text: ",end = '')
            print(encrypt(plaintext , key))
        elif choice == "2":
            print()
            print("Decrypted Text: ",end = '')
            print(decrypt(plaintext , key))
        elif choice == "0":
            print("[*] Bye...")
            sys.exit()
        else:
            print("Wrong Choice")
            print("-"*35)


main()
