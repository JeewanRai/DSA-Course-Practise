# creating user class with general attributes of all the users like name, id etc
class User:
    def __init__(self, username): # constructor are like initial instruction to make a object by giving some initial characteristic
        self.username = username

    def __str__(self):
        return f"The username is {self.username}"
    
class Task:
    def __init__(self, title, description, priority, due_date):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = False #task is initially assigned incomplete as its in the beginning

    def complete(self):
        self.completed = True

    def __str__(self):
        #shorter way of writing if else
        status = "Completed" if self.completed else "Pending"
        return f"Task: {self.title} ({status})"

class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        # telling instance of project class to store new task to existing task to container/list
        self.tasks.append(task)

    # this method will print the value of self.name, print will not print value of self.name
    def __str__(self):
        return f"Project: {self.name}"
    
class PriorityFilter:
    def __init__(self, priority):
        self.priority = priority

    def filter_tasks(self, tasks):
        # method is called list comprehension, faster execution, short line of code and compact wayto write for 
        # loop and if loop in one line. [task for task ] is method
        # task.priority means checking priority according to task in the list
        # task.priority == self.priority, task.priority accessing priority of Task class using task of Project class
        # and comparing with the priority of PriorityFilter class.
        return [task for task in tasks if task.priority == self.priority]

class Due_Date_Filter:
    def __init__(self, due_date):
        self.due_date = due_date

    def filter(self, tasks):
        return [task for task in tasks if task.due_date == self.due_date]

if __name__ == "__main__":
    # creating object of the User class
    user1 = User("Jeewan")
    user2 =User("Reena")

    # creating real life task1 and task2 or creating object
    task1 = Task("Task Completed", "Write Repote", 4, 2023)
    task2= Task("Task Completed or not", "Write Repote with header", 55, 2025)

    # creating instance of the Project class
    project1 = Project('Project A')
    project2 = Project('Project B')

    # calling add_task method of Project class with its object, telling python to pass objects of Task calls as argument into tasks
    project1.add_task(task1)
    project2.add_task(task2)

    # creating instanc of classes
    priority_filter = PriorityFilter(4)
    due_date_filter = Due_Date_Filter("04-03-2023")

    filtered_tasks = priority_filter.filter_tasks(project1.tasks)
    filtered_tasks = due_date_filter.filter(filtered_tasks)


    print(user1)
    print(user2)
    print(task1)
    print(task2)
    print(project1)
    print(project2)

    for task in filtered_tasks:
        print(task)