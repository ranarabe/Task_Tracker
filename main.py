import os
import json
import argparse
import datetime


file_path = 'tasks_file.json'
task_dict={
        "id":"",
        "description":"",
        "status":"",
        "createdAt":"",
        "updatedAt":"",
    }


def write_in_json_file(file_path:str,data):
    '''This function for write and save json file'''
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f)
    except:
        print("Error in saving json file!!")


def creat_or_read_json(file_path:str):
    '''This function checks if the file exists then creat or read the file'''
    global json_text
    if os.path.exists(file_path):
        with open(file_path) as f:
            json_text = json.load(f)
    else:
        try:
            with open(file_path, 'w' ,encoding='utf-8') as outfile:
                data={}
                json.dump(data, outfile, sort_keys=True, indent=4)
                json_text={}
        except :
            print("The file format is not correct!!")

def set_control_args():
    '''This function define the control areguments'''

    parser = argparse.ArgumentParser(
                        prog='Task CLI',
                        description='Task tracker is a project used to track and manage tasks.',
                        epilog='Text at the bottom of help')
    parser.add_argument('-add',"--add" ,help='Describtion of the task.')
    parser.add_argument('-update', '--update',nargs = '*' ,help='Update specific task.')
    parser.add_argument('-delete', '--delete', help='delete specific task.')
    parser.add_argument('-mark_in_progress', '--mark-in-progress',)
    parser.add_argument('-mark_done', '--mark-done',)
    parser.add_argument('-mark_todo', '--mark-todo',)
    parser.add_argument('-list ', '--list',choices=['done', 'todo', 'in-progress'])

    args_ = parser.parse_args()
    return args_


def add_command(task_description):
        '''This function add a new task to the json file'''

        #json_text , task_dict  global

        description = task_description  #Inserted description
        task_exists = False

        #Check if the task exists befor to avoid deplicated tasks
        for name , task in json_text.items():
            if json_text[name]['description']==task_description:
                task_exists=True
                print("This Task exists before")
                break

        if task_exists == True:
            #Generate an unique ID 
            uni_id = int(sorted(json_text.keys())[-1][5:]) + 1  if len(list(json_text.keys()))  >=1 else 1
            #Extract time 
            creating_time_date = str(datetime.datetime.now())
            
            task_name=f"Task_{uni_id}"
            json_text[task_name] = task_dict.copy()
            json_text[task_name]["id"] = uni_id
            json_text[task_name]["status"] = "todo"
            json_text[task_name]["description"] = description
            json_text[task_name]["createdAt"] = creating_time_date
            json_text[task_name]["updatedAt"] = creating_time_date
            
            #save the json file 
            write_in_json_file(file_path,json_text)

            print(f'Task added successfully (ID: {uni_id})')

def update_command(task_id,new_task_describtion=None ,task_status=None):
    '''This function update (describtion - status ) of the tasks which are existed before'''

    #json_text , task_dict  global

    updating_time_date = str(datetime.datetime.now())
    task_name=f"Task_{task_id}"
    try :
            
        json_text[task_name]["updatedAt"] = updating_time_date

        if task_status == None:
            #update the description 
            json_text[task_name]["description"] = new_task_describtion
        else :
            #update the task status 
            json_text[task_name]["status"] = task_status

        #save the json file 
        write_in_json_file(file_path,json_text)

        print(f'Task updated successfully (ID: {task_id})')
    except:
        print(f"Task with ID = {task_id} does not exist")

def delete_command(task_id):
    '''This function delete the task'''
    #json_text , task_dict  global

    task_name=f"Task_{task_id}"
    try:
        json_text.pop(task_name)
        write_in_json_file(file_path,json_text)
        print(f'Task deleted successfully (ID: {task_id})')
    except:
        print(f"Task with ID = {task_id} does not exist")



def list_command(List_type):
    '''This function list the tasks based on the list type'''

    task_in_type =[]

    for task_name , task in json_text.items():
        if json_text[task_name]['status']==List_type:
            task_in_type.append(json_text[task_name]["description"])

    if len(task_in_type) == 0:
        print(f"The List of Tasks '{List_type}' is empty")
    else:
        print(f"The List of Tasks '{List_type}':")
        for task in task_in_type:
            print(f"- {task} ")



def handle_commands(args):
    '''This function to handle the input commands from the user'''

    
    if args.add is not None :  ## Add command
        add_command(args.add)

    elif args.update is not None : ## Update command
        update_command(args.update[0],args.update[1])

    elif args.delete is not None : ## Delete command
        delete_command(args.delete)

    elif args.mark_in_progress is not None :## Update task status to in-progress
        update_command( args.mark_in_progress ,task_status="in-progress")
       
    elif args.mark_todo is not None :  ## Update task status to todo
        update_command( args.mark_todo ,task_status="todo")

    elif args.mark_done is not None : ## Update task status to done
        update_command( args.mark_done ,task_status="done")

    elif args.list is not None : ## List command
        list_command(args.list)



creat_or_read_json(file_path)

args=set_control_args()

handle_commands(args)