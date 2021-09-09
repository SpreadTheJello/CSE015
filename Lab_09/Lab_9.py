def encode(t,k):
    result = ""
    for i in range(len(t)):
        char = t[i]
        result += chr((ord(char) + k - 32) % 94 + 32)
    return result

def decode (t,k):
    result = ""
    for i in range(len(t)):
        char = t[i]
        result += chr((ord(char) - k - 32) % 94 + 32)
    return result

t = input("Input the message you want encoded: ")
k = int(input("Enter your shift amount: "))
print ("Encrypted Message: " + encode(t, k))
t = input("Input the message you want decoded: ")
k = int(input("Enter your shift amount: "))
print ("Encrypted Message: " + decode(t,k))
