def show():
    print("----palindrome checker---")
    user=input("enter the palindrome: ")
    copy=user[::-1]

    if(user==copy):
        print("it is a palindrome")
    else:
        print("it is not palindrome")
show()            