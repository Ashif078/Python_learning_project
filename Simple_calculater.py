a=int(input("enter the frist number: "))
b=int(input("enter the second number: "))

print('''enter the option 
      1) addition
      2) substraction
      3) multiplication
      4)divide''' )
add=a+b
sub=a-b
mult=a*b
div=a/b

user=int(input("enter the option: "))
if(user==1):
    print(add)
elif(user==2):
    print(sub)
elif(user==3):
    print(mult)
elif(user==4):
    print(div)   