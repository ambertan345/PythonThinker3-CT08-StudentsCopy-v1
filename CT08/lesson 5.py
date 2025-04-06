import os
# filepath = os.getcwd()

# fullpath = os.path.join(filepath, "file.txt")


# if os.path.exists(fullpath):
#     print("{} exist".format(fullpath))
# else:
#     print("{} does not exist".format(fullpath))

# print(filepath)

# if os.path.exists(fullpath):
#     print(f"{fullpath} exist")
# else:
#     print(f"{fullpath} does nor exist")

# file = open(fullpath, "w")
# file.write("Hello world")
# file.close

# file = open(fullpath, "r")
# content = file.read()
# print(f"Flie content:\n{content}")
# file.close

FILENAME = "tasks.txt"
FILEPATH = os.getcwd()
FULLPATH = os.path.join(FILEPATH, FILENAME)


def create_new_file(fullpath: str) -> None:

    print("\nok, creating a new task file")
    if os.path.exists(fullpath):
        print(f"file [{fullpath}] exists")
    else:
        with open(fullpath, 'w') as taskfile:
            taskfile.write("task list")

def add_new_task(fullpath: str) -> None:
    with open(fullpath, 'a') as taskfile:
    # file in append mode
        newtask = input("Enter a new task: ")#get new task frm user
        taskfile.write(f"\n{newtask}")
    
def view_all_tasks(fullpath: str) -> list[str]:
    print("viewing al tasks")
    with open(fullpath, 'r')as file:
        tasks = file.readlines()

    for i in range(len(tasks)):
        if i == 0:
            print(tasks[i].strip())
        else:
            print(f"{i}.{tasks[i]}".strip())
view_all_tasks(FULLPATH)



def mark_task_as_done(fullpath: str) -> None:
    print(" making task as done")

    lines = view_all_tasks(fullpath)

    if len(lines) <= 1:
        print("\nNo tasks available to mark as done")
        return

    task_number = int(input("\n enter the task number to mar as done"))
    if task_number < 1 or task_number > len(lines) - 1:
        print("\n invalid task number. try again")
        return

    task_index = task_number
    if "[DONE]" in lines[task_index]:
        print("\n this task is already marked as done")
    else:
        lines[task_index] = lines[task_index].strip() + " [DONE]\n"
        print(f"\n task {task_number} marked as done")

    with open(fullpath, 'w') as taskfile:
        taskfile.writelines(lines) 

    # with open(fullpath, 'r') as file:
    #         tasks = file.readlines()
    
    # updated_tasks = []

    # for task in tasks:
    #         if not task.strip().endswith('done'):
    #             updated_tasks.append(task.strip() + " - done\n")  
    #         else:
    #             updated_tasks.append(task)
    # with open(fullpath, 'w') as file:
    #         file.writelines(updated_tasks)
    #     print(f"Task in {fullpath} has been marked as done.")
    
def delete_task(fullpath:str) -> None:
    print("\n deleting tasks now")
    lines = view_all_tasks(fullpath)

    if len(lines) <= 1:
        print("\nNo tasks available to delete")
        return

    task_number = int(input("\n enter the task number to delete"))
    if task_number < 1 or task_number > len(lines) - 1:
        print("\n invalid task number. try again")
        return

    confirm = input(f"\n are you sure you want to delete task {task_number} ? (y/n)").lower()
    if confirm != 'y':
        print("\n task deletion canceled")
        return
    
    task_index = task_number
    deleted_task = lines.pop(task_index).strip()

    with open(fullpath, 'w') as taskfile:
        taskfile.writelines(lines) 


def menu_system(fullpath:str) -> None:
    print("\n welcome to personal planner")

    while True:
        print("\n")
        print("1. create a new task file")
        print("2. view all tasks")
        print("3. add a new task")
        print("4. delete a task")
        print("5. mark a task as done")
        print("6. exit")

        choice = input("\n input choice: ")

        if choice == '1':
            create_new_file(FULLPATH)
        elif choice == '2':
            view_all_tasks(FULLPATH)
        elif choice == '3':
            add_new_task(FULLPATH)
        elif choice == '4':
            delete_task(FULLPATH)
        elif choice == '5':
            mark_task_as_done(FULLPATH)
        elif choice == '6':
            print("\n exiting")
            break
        else:
            print("\n invalid choice. try again")



