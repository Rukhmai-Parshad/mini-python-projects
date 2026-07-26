from database import(
    create_table,
    add_task,
    view_tasks,
    update_task,
    delete_task,
    search_task
)

def main():
    create_table()

    while True:
        print()
        print("----------WELCOME TO THE TASK MANAGEMENT APP----------")
        print()
        print("1. Add Task")
        print("2. Update Task")
        print("3. View Tasks")        
        print("4. Delete Task")
        print("5. Search Task")
        print("6. Exit")   
        print()     

        try:
            choice = int(input("Enter your choice (1-6): "))
            print()
        except ValueError:
            print("Please enter a valid number!")
            print()
            continue
       
        if choice == 1:
            task_name = input("Enter task name:\n")
            print()
            priority = input("Enter priority (Low/Medium/High):\n")
            print()

            add_task(task_name, priority)
            print()

        elif choice ==2:
            task_id = int(input("Enter Task ID:\n"))
            print()
            task_name = input("Enter new task name:\n")
            print()
            priority = input("Enter priority:\n")
            print()
            status = input("Enter status (Pending/Completed):\n")
            print()

            update_task(task_id, task_name, priority, status)
            print()

        elif choice == 3:
            view_tasks()                 
            print()

        elif choice == 4:
            task_id = int(input("Enter Task ID:\n"))
            print()

            delete_task(task_id)
            print()

        elif choice == 5:
            keyword = input("Enter keyword:\n")
            print()

            search_task(keyword) 
            print()

        elif choice == 6:
            print("Closing the program...")
            break

        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
