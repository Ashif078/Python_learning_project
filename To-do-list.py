def add_task():
    task=(input("Enter the task: "))
    with open("task_file.txt","w") as f:
        f.write(task + "\n")




def view():
    pass


def delete_task():
    pass

def main():
    print("----To Do list-----")
    print("1. Add task \n2. View \n3. delect task")
    user=int(input("Enter what you want you do: "))

    if user== 1:
        add_task()
main()        

    