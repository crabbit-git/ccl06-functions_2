tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 }
]

def goto_menu():
    print("\nReturning to the main menu...\n")

def print_handsomely(task_list):
    for task in task_list:
        print(f"{task['description']} ({task['time_taken']} minutes)")

def print_tasks(filter, min_time = None):
    task_list = tasks
    if filter == "desc":
        task_list = [task["description"] for task in tasks]
        for task in task_list:
            print(task)
        goto_menu()
        return
    elif filter == True:
        task_list = [task for task in tasks if task["completed"] == True]
    elif filter == False:
        task_list = [task for task in tasks if task["completed"] == False]
    elif filter == "time":
        task_list = [task for task in tasks if task["time_taken"] >= min_time]
    print_handsomely(task_list)
    goto_menu()
    return

def find_task(query):
    task_list = [task for task in tasks if task["description"].casefold().__contains__(query.casefold())]
    if task_list == []:
        print("\nSorry, it doesn't look like that's on the list at the moment!\n")
    elif len(task_list) > 1:
        print("\nMultiple matches found:\n")
        print_handsomely(task_list)
        print("\nPlease try a more specific query.\n")
    else:
        return task_list

def mark_complete():
    query = input("\nWhich task would you like to mark as done?\n")
    print()
    search_results = find_task(query)
    if search_results == None:
        return
    for task in search_results:
        incomplete_task = task
        desc = task["description"]
        time = task["time_taken"]
        task_complete = {
            "description": desc,
            "completed": True,
            "time_taken": time
        }
    tasks[tasks.index(incomplete_task)] = task_complete
    print(f"\n{task_complete['description']} has been marked as completed!\n")
    goto_menu()

def add_task():
    new_task_desc = input("\nWhat new task would you like to add to the list?\n")
    new_task_time = input("\nHow long do you expect the task to take to complete?\n")
    new_task = {
        "description": new_task_desc,
        "completed": False,
        "time_taken": new_task_time
    }
    tasks.append(new_task)
    print(f"\n{new_task_desc} ({new_task_time} minutes) has been added to the list!")
    goto_menu()

selection = None
while selection != "q":
    print("Menu:")
    print("1: Display All Tasks")
    print("2: Display Uncompleted Tasks")
    print("3: Display Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("M or m: Display this menu")
    print("Q or q: Quit")
    selection = input("\nWhat would you like to do?\n").casefold()

#list_tasks() # Pass this True to get list of completed tasks, False for incomplete ones, "long" for longwinded tasks, or nothing to get full list

# So for MVP:
# 1. Print list of incomplete tasks:
    if selection == "2":
        print("\nTasks still to be done:\n")
        print_tasks(False)
# 2. Print list of completed tasks:
    if selection == "3":
        print("\nTasks already completed:\n")
        print_tasks(True)
# 3. Print list of all task descriptions
# NOTE: The menu makes it sound like it'll print the same way as the previous two, but the instructions say just to list the description, so I did that instead:
    if selection == "1":
        print("\nTask list:\n")
        print_tasks("desc")
# 4. Print list of tasks where time_taken is at least a given time (I chose 15 minutes):
    if selection == "5":
        min_time = int(input("What minimum time would you like to filter for? Enter a whole number, in minutes:\n"))
        # NOTE: This won't account for the user inputting anything other than an integer, but it's been a very long day, so...
        print(f"\nThe following tasks should take at least {min_time} minutes to complete:\n")
        print_tasks("time", min_time)
# 5. Print any task with a given description (casefolded search term rather than requiring exact match):
    if selection == "6":
        query = input("\nWhich task are you looking for?\n")
        print("\nThe following task matches your search query:\n") # blank line for spacing, no other reason
        print_handsomely(find_task(query))
        goto_menu()
# 6. Given a description, update that task to mark it as complete:
    if selection == "4":
        mark_complete()
# 7. Add a task to the list:
    if selection == "7":
        add_task()