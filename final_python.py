#####password generator
import random
import string

password_length=int(input("How long do you want the password to be ?"))

while password_length<1:
     password_length= int(input("Error! The length of the password must greater than 1, please enter the length of the password:"))


symbol_length=int(input("How many symbols do you want in your password ?"))

while symbol_length<0 or symbol_length>password_length:
    symbol_length= int(input("Error! The number of symbols can not be less than 0 or greater than the length of password, try again:" ))


symbols=string.punctuation+string.ascii_letters
digits="0123456789"
password=""

length_count=0
symbol_count=0
digit_count=0

while(length_count<password_length):
    # symbol_count=0
    while(symbol_count<symbol_length):
        password+=random.choice(symbols)
        length_count+=1
        symbol_count+=1
    # digit_count=0
    while(digit_count<password_length - symbol_length) :
        password+=random.choice(digits)
        digit_count+=1
        length_count+=1

l =list(password)
random.shuffle(l)
result=''.join(l)

print("The password is :",result)        
