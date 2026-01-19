import random
import string

lower=string.ascii_lowercase
upper=string.ascii_uppercase
symbol=string.punctuation
digit=string.digits

character=""
user_lenght=int(input("enter the lenght : "))
if(user_lenght> 8 and user_lenght<15):
    user_upper=input("you want to upper case (y/n) : ").strip().lower() == "y"
    user_lower=input("you want to lower case (y/n) : ").strip().lower() == "y"
    user_symbol=input("you want to special symbol case (y/n) : ").strip().lower() == "y"
    user_digit=input("you want to digit case (y/n) : ").strip().lower() == "y"

    if(user_upper):
        character += upper
    if(user_lower):
        character += lower
    if(user_digit):
        character += digit
    if(user_symbol):
        character += symbol

    password=""
    for _ in range(user_lenght):
        password += random.choice(character)  
    print(password)     
else:
    print("so length give 8 to 15")




