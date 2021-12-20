#function to encrypt a string
def encrypt(text,key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + key-65) % 26 + 65) #for upper case letters
        else:
            result += chr((ord(char) + key - 97) % 26 + 97) #for lowercase letters
    return result

#function to decrypt a text
def decrypt(text,key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()): 
            result += chr((ord(char) - key-65) % 26 + 65) #for upper case letters
        else:
            result += chr((ord(char) - key - 97) % 26 + 97)#for lowercase letters
    return result

if __name__=="__main__":
    Message="KLMLUKAOLMVYA"
    key=7
    EncryptedMessage=encrypt(Message, key)
    print("Origininal Message: ",Message)
    print("Encrypted Message: ",EncryptedMessage)