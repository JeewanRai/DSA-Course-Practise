# creating globle variable task to store data in side of list
tasks = []

# function to display To-Do-List
def display_tasks():
    #if not tasks:
        #print("No tasks in your To-Do List.")
    #else:
        #print("Your To-Do List:")
        # ternary operator, shorted way of writing if else statement also known as condition operation
    print("No tasks in To-Do-List" if not tasks else "To-Do-List")
    #index = 1
    #for task in tasks:
        #print(f"{index}. {task}")
        #index += 1
    # the enumerator will iterate with some index and value
    """tasks = ["Task A", "Task B", "Task C"]
for index, task in enumerate(tasks, 1):
    print(f"{index}. {task}")
tasks = ["Task A", "Task B", "Task C"] for index, task in enumerate(tasks, 1): print(f"{index}. {task}")
The enumerate function provides both the index and the value(item or whatever is inside of list) of each element in the tasks iterable.

tasks = ["Task A", "Task B", "Task C"]
# Using enumerate to get index and value pairs
enumerated_tasks = list(enumerate(tasks, 1))
print(enumerated_tasks)
enumerate(tasks, 1) to enumerate the tasks list, and it produces a list of tuples. Each tuple contains two elements: the first element is the index (starting from 1, as specified by enumerate(tasks, 1)), and the second element is the value, which is the task description from the tasks list
Output
[(1, 'Task A'), (2, 'Task B'), (3, 'Task C')]

The for loop will iterate the list of tuples extracting the index and task description from each tuple
"""
# index and item are not explicitely but implicitely defined and in this form it will get assigned the value to index and item
# from the output of enumeration
# Index: 1, Item: Task A
# Index: 2, Item: Task B
# Index: 3, Item: Task C

    for index, item in enumerate(tasks, 1):
        print(f"{index}.{tasks}")

# function to add task on the To-Do-List
def add_task(task):
    tasks.append(task)
    print(f"Added tasks: {task}")

def delete_task(task_index):
    try:
        # converting task_index passed into delet_task is string, will convert "3" into integer 
        # tasks = ["Task 1", "Task 2", "Task 3", "Task 4"] 4 tasks, if want to delet task 2, first converted to int
        #  checks if 1<= 2 and falls between length(1 to 4), if we put 5 then 1<=5 is true but length there is only 4 task so its false
        # 
        task_index = int(task_index)
        
