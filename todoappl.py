def task():
    tasks = []
    print("-----WELCOME TO TASK ORGANIZER-----")

    while True:
        try:
            total_task = int(input("Enter how many tasks you want to add = "))
            break
        except ValueError:
            print("Please enter a valid number.")

    for i in range(1, total_task + 1):
        task_name = input(f"Enter your task {i} = ")
        tasks.append(task_name)

    print(f"Today's tasks are\n{tasks}")

    while True:
        try:
            operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\n"))
        except ValueError:
            print("Invalid input, please enter a number between 1 and 5.")
            continue

        if operation == 1:
            add = input("Enter your task to add: ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added...")

        elif operation == 2:
            updated_val = input("Enter your task to update: ")
            if updated_val in tasks:
                up = input("Enter new task: ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated task '{updated_val}' to '{up}'")
            else:
                print(f"Task '{updated_val}' not found.")

        elif operation == 3:
            delete_val = input("Enter your task to delete: ")
            if delete_val in tasks:
                ind = tasks.index(delete_val)
                del tasks[ind]
                print(f"Task '{delete_val}' has been successfully deleted...")
            else:
                print(f"Task '{delete_val}' not found.")

        elif operation == 4:
            if tasks:
                print("Current tasks:")
                for i, t in enumerate(tasks, start=1):
                    print(f"  {i}. {t}")
            else:
                print("No tasks left.")

        elif operation == 5:
            print("Closing the program....")
            break

        else:
            print("Invalid input")


if __name__ == "__main__":
    task()