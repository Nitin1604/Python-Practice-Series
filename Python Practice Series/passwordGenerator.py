# Practice Series 7

import string
import random

if __name__ == "__main__":
    lowercase = string.ascii_lowercase
    print('String in lowercase => ',lowercase)
    uppercase = string.ascii_uppercase
    print('String in uppercase => ',uppercase)
    digits = string.digits
    print('String containing digits => ',digits)
    punctuation = string.punctuation
    print('String containing punctuation => ',punctuation)
    plen = int(input("Enter password length: ")) 
    string = []
    string.extend(list(lowercase))
    string.extend(list(uppercase))
    string.extend(list(digits))
    string.extend(list(punctuation))
    # print(string)
    random.shuffle(string)
    # print(string)
    print("Your password is: ")
    print("".join(random.sample(string, plen)))
    # print("".join(string[0:plen]))

