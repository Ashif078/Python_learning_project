user1=int(input("enter the weight : "))
user2=float(input("entter thr height: "))/100
 
BMI=round(user1/(user2**2),2)

if(BMI<18.5): 
    print(F"you fall underweight categorie with a bmi value :{BMI}")
elif(BMI>18.5 and 24.9):
    print(F"you fall normal categorie with a bmi value :{BMI}")
elif(BMI>25.0 and 29.9):
    print(F"you fall overweight categorie with a bmi value :{BMI}")
elif(BMI >30.0):
    print(f"obese : {BMI}")
elif(BMI > 30 and 34.9):
    print(F"divided into class 1 with bmi value :{BMI}")
elif(BMI > 35 and 39.9):
    print(F"divided into class 2 with bmi value :{BMI}")
elif(BMI > 40):
    print(F"divided into class 3 with bmi value : {BMI}")

else:
    print("out of weigt")    




    