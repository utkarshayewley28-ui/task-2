tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i, item in enumerate(tasks, start=1):
                status = "Completed" if item["completed"] else "Not Completed"
                print(f"{i}. {item['task']} - {status}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to complete.")
        else:
            for i, item in enumerate(tasks, start=1):
                print(f"{i}. {item['task']}")

            number = int(input("Enter the task number to mark as completed: "))

            if 1 <= number <= len(tasks):
                tasks[number - 1]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i, item in enumerate(tasks, start=1):
                print(f"{i}. {item['task']}")

            number = int(input("Enter the task number to delete: "))

            if 1 <= number <= len(tasks):
                deleted_task = tasks.pop(number - 1)
                print(f"Deleted: {deleted_task['task']}")
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
