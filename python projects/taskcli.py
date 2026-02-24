import json
import os
import uuid

def Add_task():
    task_name = input("Input the name of your task")
    task_deadline = input("Input your task deadline if any")              #rate the function 1-10
    task_status = input("Input the status of your task")
    task_id = str(uuid.uuid4())
    #store in dictionary
    
    tasks[task_id] = {
       "task_name" : task_name,
       "task_deadline" : task_deadline,
       "task_status" : task_status
    }
    with open(tasks_file,"w") as f:     #save in memory.
     json.dump(tasks,f,indent=2)
    
  
  
      
def update_task():
      decision =input("Do you want to change the name of the task :press N if status press y" )       #rate thefnction
      if decision == 'N':
       tsk_id = input("what is the id of your task ")
       task_n_name = input("what is the new name of your task")
       if tsk_id in tasks:
           tasks[tsk_id]["task_name"] = task_n_name
           print(f"task{tsk_id} updated successfully")
       else:
          print("invalid task name")
           
       # Newtasks name
       with open(tasks_file,"w") as f:
          json.dump(tasks,f,indent=2)
       #append

      elif decision == 'Y' :
       tsk_id = input("what is the id of your task")
       #append this new name to the task

       n_status = input("What is the new status ")

       if tsk_id in tasks:
          tasks[tsk_id]["task_status"] = n_status
          print("Your task status has been changed successfully")

          with open(tasks_file,"w")as f:
             json.dump(tasks,f,indent=2)
       else:
          print('invalid id')  
      else:
         print("dR DRE SPOTTED AN ERROR ")
         with open(tasks_file,"w") as outfile:
            json.dump(tasks,outfile,indent=2)
   
         
     

def list_all():
     #list everything sure: from the dictionary
     if not tasks:
        print("no tasks found")
        return
     for task_id,task in tasks.items():
        print(f"ID{task_id}")
        print(f"name : {task['task_name']}")
        print(f"status{task['task_status']}")
        print(f"deadline{task['task_deadline']}")
        print("-"*20)
  
def list_done():
   found = False
   for task_id, task in tasks.items():
      if task["task_status"].lower() == "done":
         found = True
         print(f"ID:{task_id}")
         print(f"Task_name{task['task_name']}")
         
   if not found:
      print("No tasks are marked as done.")

        
        
        
        
  
def not_done():
     found = False
     for task_id, task in tasks.items():
        if task["task_status"].lower() in ( "inprogress" , "undone" ):
         found = True
         print(f"ID:{task_id}")
         print(f"Task_name{task['task_name']}")
         
     if not found:
      print("No tasks are marked as undone.")


def delete_task():
   decision = input("what is the name of your task")
   found = False
   for task_id, task in list(tasks.items()):
      if task["task_name"].lower() == decision.lower():
        del tasks[task_id]
        found = True
        print("Task deleted Successfully")
        break
   if not found:
      print("Task couldnt be found.")

        
def in_progress():
     found = False
     for task_id, task in tasks.items():
        if task["task_status"].lower == "inprogress":
           found = True
           print(f"{task_id}")
           print(f"the task named {task['task_name']}")

     if not found:
        print("All tasks are done")



def taskcli():
    #first ask user for data
 while True:
  Enter = input("""What would you like to do: 
Add a task,Press Y,
Update a task : Press X, 
List all tasks press ,
List all done tasks press D ,
List all tasks that are not done press I,
List all tasks that are in progress : press V,
""")
  
  if Enter == 'Y':
      Add_task()
  elif Enter == 'X':
      update_task()
  elif Enter == 'U':
      list_all()
  elif Enter == 'D':
      list_done()
  elif Enter == 'I':
       not_done()
  elif Enter == 'V':
      in_progress()
  else:
     print("Invalid printing")

  #write functions to fix the mistake done or started:
  
tasks_file = "tasks.json"
if os.path.exists(tasks_file):
   with open(tasks_file,"r") as f:
      try:                                             #loads everything from the taskfile
         tasks = json.load(f)
      except json.JSONDecodeError:
         tasks = {}
else : 
   tasks = {}
taskcli()
