def encrypt(text,key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + key-65) % 26 + 65)
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
    return result

def decrypt(text,key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) - key-65) % 26 + 65)
        else:
            result += chr((ord(char) - key - 97) % 26 + 97)
    return result

if __name__=="__main__":
    Message="KLMLUKAOLMVYA"
    key=7
    EncryptedMessage=encrypt(Message, key)
    print("Origininal Message: ",Message)
    print("Encrypted Message: ",EncryptedMessage)