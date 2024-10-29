import random

def genpass (passlength):
    char = "+-/*!&$#?=@()_~`abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890[}]"
    
    mypass = ''
    for i in range(passlength):
        temp = random.choice(char)
        mypass += temp

    return mypass

if __name__ == '__main__':
    digit = int(input('mau berapa panjang passwordnya:'))
    print(genpass(digit))