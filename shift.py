def modulo(number, n):
    return number % n

def shift(number, shift, n):
    shf = number - ord('a')
    return chr(ord('a') + modulo(shf + shift, n))    

def Gen():
    import random
    random.seed()
    return random.randint(0,25)

def Enc(text, key):
    return map((lambda x: shift(ord(x),key, 25)), text)

def Dec(text, key):
    return Enc(text, 25 - key)

def main():
    import sys
    if (len(sys.argv) >= 2):
        text = sys.argv[1]
    else:
        text = str(raw_input("Text? \n"))
    key = Gen()
    _enc = Enc(text,key)
    print (_enc)
    _dec = Dec(_enc, key)
    print(_dec)


if __name__ == '__main__':
    main()