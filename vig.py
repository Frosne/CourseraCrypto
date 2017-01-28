def key_lengthen(key, length):
    result = ""
    for i in range(length):
        result = result + key[i%len(key)]
    return result 

def rekey(key):
    return "".join(map(lambda x : chr(ord('a') + (26 - (ord(x) - ord('a')))%26), key))

def compute_shift(a,b):
    return  (ord(a) + ord(b) - 2* ord('a'))%26

def compute_letter(a,b):
    if b > 'z' or b <'a' :
        return b
    else:
        return chr(ord('a') + compute_shift(a,b))    

def encrypt(key, message):
    key = key_lengthen(key, len(message))
    return "".join(map(lambda x,y : compute_letter(x,y), key, message))

def decrypt(key, message):
    return encrypt(rekey(key), message)    

def main():
    key = "relations"
    message = "to be or not to be that is the question"
    ciphered = encrypt(key, message)
    print (ciphered)
    print (decrypt(key, ciphered))

if __name__ == '__main__':
    main()