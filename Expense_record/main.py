from database import(
    create_table,
    add_expense
)

def main():
    create_table()

    while True:
        print("\n------- Expense Tracker --------")
        print("\n1.Add Expense \n2.View Expenses \n3.Delete Expense \n4.Exit")
        
        choice = int(input("Choose from the menu (1-4): "))

        if choice == 1:

            amount = float(input("Enter the amount of Expense: "))
            category = input("Enter the category of expense: ")
            date = input("Enter the date of expense (YYYY-MM-DD): ")
            note = input("Enter the reason of exoense: ")

            add_expense(amount, category, date, note)
            print("Record update successfully!")

        elif choice == 4:
            print("Done Updation")
            break
        else:
            print("Choose from menu only")

if __name__ == "__main__":
    main()

