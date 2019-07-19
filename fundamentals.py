# Exercise 1
class Task:
    def __init__(self, desc, date):
        self.description = desc
        self.due_date = date

task1 = Task('Clean house', 'Tomorrow')
task2 = Task('Wash car', 'Day after tomorrow')
task3 = Task('Finish homework', 'Day after the day after tomorrow')

# Testing to see if they were installed
print(task1.description)
print(task2.description)
print(task3.description)

# Exercise 2
class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_to(self, new_task):
        self.tasks.append(new_task)

new_todo_list = TodoList()
new_todo_list.add_to(task1)
new_todo_list.add_to(task2)
new_todo_list.add_to(task3)

# Test to see if they have been properly added to the object
for task in new_todo_list.tasks:
    print(task.description)