#Nicholas Hester
#CS 150
#September 29, 2021
#Project 1
import string

cipher_in = "aeostr"
cipher_out = "rtsoea"
trantab = str.maketrans(cipher_in, cipher_out)

string_length = int(input("Enter String Length"))
str = str.lower(input("What is your code? "))

ticker = 1

while ticker <= string_length:
    ticker = ticker + 1
    if 'a' in str:
        print(str.translate(trantab))
    elif 'e' in str:
        print(str.translate(trantab))
    elif 'o' in str:
        print(str.translate(trantab))
    elif 's' in str:
        print(str.translate(trantab))
    elif 't' in str:
        print(str.translate(trantab))
    elif 'r' in str:
        print(str.translate(trantab))
    else:
        print("ERROR")


