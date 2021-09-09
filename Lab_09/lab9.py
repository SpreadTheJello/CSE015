def encode(t, k):
    result = ""
    for i in range(len(t)):
        char = t[i]
        if char ==' ':
            result += char
        elif (char.isupper()):
            result += chr((ord(char) + k - 65) % 26 + 65)
        else:
            result += chr((ord(char) + k - 97) % 26 + 97)
    return result
def decode (t, k):
    ciphertext = input(" enter encrypted message: ")
    shift = int(input("shift value: "))
    space = []
    ciphertext = ciphertext.split()
    message = []
    for word in ciphertext:
        cipher_ords = [ord(x) for x in word]
        plaintext_ords = [o - shift for o in cipher_ords]
        plaintext_chars = [chr(i) for i in plaintext_ords]
        plaintext = ''.join(plaintext_chars)
        message.append(plaintext)
    message = ' '.join(message)
    print ("encrypted message is: ", message)
    
t = input("input your message")
k = int(input("how much would you shift it?"))

print (t)
print (str(k))
print ("Cipher: " + encode(t, k))
decode(t,k)

        
