def show():
    print("Enter the india currency convert the dollar:")
    print("Enter the dollar currency convert the rupees:")
    user=(input("enter the currency type(r/d): ")).strip().lower()

    currency=int(input("enter the amount:"))
    if(user=="d"):
        print(currency*82.3)
    elif(user=="r"):
        print(currency/82.3)    
    else:
        print("enter the valid currency")    
show()        
    