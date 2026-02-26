from database import(
    create_table
)

from service import(
    create_client,
    add_interaction,
    update_client_status,
    view_records
    
)


def main():
    
    create_table()

    while True:

        print("---------------CRM System-------------")
        print("""
    1️⃣. Add client
    2️⃣. Add interaction
    3️⃣. update status
    4️⃣. View Records
    5️⃣. Exit                            

    """)
        choice = input("choose from menu")

        if choice== "1":
            name=input("Enter the name of client :")
            phone=input("Client phone no :")
            email=input("Client email :")

            try:
                create_client(name,phone,email)
                print("Client added Sucessfully")
            except ValueError as e:
                print(f"Error : {e}")
            except Exception as e:
                print(f"Error : {e}")

        elif choice== "2":
            
            client_id =int(input("Enter the client ID :"))
            type= input("Enter the way of Interaction :")
            note= input("Leave some note :")

            try:
                add_interaction(client_id,type,note)
            except ValueError as e:
                print(f"Error : {e}")
            except Exception as e:
                print(f"Error : {e}")


        elif choice == "3":
            client_id= int("Enter the client Id :")
            new_status=input("Enter the Updated status :")

            try:
                update_client_status(client_id,new_status)
            except ValueError as e:
                print(f"Error : {e}")
            except Exception as e:
                print(f"Error : {e}")


        elif choice== "4":
            
            status=input("Enter the status: ")

            try:
                records= view_records(status)
                for view in records:
                    print(f"{view[0]}.{view[1]} |{view[2]} | {view[3]}|{view[4]}| {view[5]}")
            except ValueError as e:
                print(f"Error : {e}")
            except Exception as e:
                print(f"Error : {e}")


        elif choice== "5":
            print("Good byee! ")
            break
        else:
            print("Choose from Menu only")

if __name__ =="__main__":
    main()