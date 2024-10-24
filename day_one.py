def load(filename):
   try:#in case file does not exist function is wrapped with try-except block to handle errors - 'FILE NAME NOT FOUND'
      with open(filename,'r') as file:
         tasks = file.readlines() #read all created task from file
         return [task.strip() for task in tasks] #stripping each task of unwanted characters - \n
   except FileNotFoundError:
      return[] # if file is not found/does not exist, return a empty list

def save(filename, task_list): #taking two arguments filename & task_list
   with open(filename,'w') as file: #opens the file in write mode('w')
      for task in task_list:
        #writes each new task on new line
         file.write(task + '\n') # write() method writes a string to the file
    
    
def to_do():

    print("\nThis is a command line to-do application with file storage.\n\n")
    print(" Press 1 to - Add a new ask \n Press 2 for to - save the created task list\n Press 2 to - mark a task as completed\n Press 4 to - remove a task\n Press 5 to END\n")
    user_input = input("select a funciton.\n\n")
    task_list = []

    while True:
        if user_input == '1':
         user_task = input("Write your task:\n\n")
         #appending created user task to task list
         task_list.append(user_task)
         
        
        elif user_input == '2':
         #User saving task list to file
           print("Saving....\n\n")
           save()
           print("Saved Task!\n\n")
           
        elif user_input == '5':
         break


to_do()