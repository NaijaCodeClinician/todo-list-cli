from validation import valid_number

def input_task(task_list):
    while True:
        number = input("How many tasks do you want to add to your to-do list: ").strip()
        if not number:
            print("Input a number")
            continue
        if not valid_number(number):
            print("Enter a valid number")
            continue
        number = int(number)
        if number <= 0:
            print("Number can't be negative or equal to zero")
            continue
        break
    for t in range(1, number + 1):
        while True:
            task = input(f"\nEnter a Task {t}: ").title().strip()
            if not task:
                print("Task can't be empty")
                continue
            if task in task_list:
                print("Task already exists, input a different task")
                continue
            print("Task has been successfully added")
            task_list.append(task)
            break

def see(task_list):
    if not task_list:
        print("You have no available task")
    else:
        print("YOUR AVAILABLE TASKS:")
        for i in range(len(task_list)):
            print(f"({i+1})\t{task_list[i]}")

def remove(task_list):
    if not task_list:
        print("There are no tasks to be removed")
    else:
        print("YOU ARE ABOUT TO REMOVE SOME TASKS FROM YOUR TODO LIST.")
        while True:
            num = input("How many tasks do you want to remove from your to-do list: ").strip()
            if not num:
                print("Input a number")
                continue
            if not valid_number(num):
                print("Invalid number")
                continue
            num = int(num)
            if num <= 0:
                print("Number can't be negative or equal to zero")
                continue
            if num > len(task_list):
                print("You can't remove more than available tasks")
                continue
            break
        for rem in range(1, num + 1):
            print("\nCURRENT AVAILABLE TASKS")
            for i, task in enumerate(task_list):
                print(f"({i+1}) {task}")
            print()
            while True:
                choice = input(f"Input the number of Task {rem} to be removed: ").strip()
                index = len(task_list)
                if not choice:
                    print("Choice Field can't be empty")
                    continue
                if not valid_number(choice):
                    print("Enter a valid number")
                    continue
                choice = int(choice)
                if choice <= 0:
                    print("Number can't be negative or equal to zero")
                    continue
                if choice > index:
                    print("Task does not exist")
                    continue
                print("Task has successfully been removed")
                rem_index = choice - 1
                del task_list[rem_index]
                break 
        print("\nYOU HAVE SUCCESSFULLY REMOVED TASKS FROM YOUR TODO LIST")  
                 
print("=" * 59)
print("=" * 24, "TODO LIST", "=" * 24)
print("=" * 59)
print("Welcome to your 'Todo List' App, what would you like to do today? ")
print("\n(1)\tCreate a task\n(2)\tView your pending tasks\n(3)\tRemove tasks\n(4)\tExit")
task_list = []
while True:
    choice = input("\nChoose from 1 - 4 to select an option: ")
    if choice == "1":
       create_task = input_task(task_list)
    elif choice == "2":
        view = see(task_list)
    elif choice == "3":
        delete = remove(task_list)
    elif choice == "4":
        break
    else:
        print("Invalid Choice")
        continue

         
            
    
