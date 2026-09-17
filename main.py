#to-do app program
def task():
    tasks = []
    print("-----Welcome to Task Management App-----")

    while True:
        print("Welcome to task management application!.")
        try:
            total_task = int(input("\nEnter a number of task you want to add = "))
            break
        except ValueError:
            print("Please enter a valid number.")

    for i in range(1, total_task + 1):
        task_name = input(f"Enter your task {i} = ")
        tasks.append(task_name)

    print(f"Today's tasks are\n{tasks}")


    while True:
        try:
            operation = int(input("Enter:\n1.Add\n2.Update\n3.Delete\n4.View\n5.Exit/Stop\n"))
        except ValueError:
            print("Invalid operator. Please enter a valid number.")
            continue


        if operation == 1:
            add = input("Enter the task you want to Add: ")
            tasks.append(task)
            print(f"Task {add} has been successfully added!....")

        elif operation == 2:
            updated_val = input("Enter the task you want to Update: ")
            if updated_val in task:
























