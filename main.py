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


def creat_or_read_json(file_path:str):
    '''This function checks if the file exists then creat or read the file'''
    global json_text
    if os.path.exists(file_path):
        with open(file_path, 'r+') as f:
            json_text = json.load(f)
    else:
        try:
            with open(file_path, 'w' ,encoding='utf-8') as outfile:
                json.dump(data, outfile, sort_keys=True, indent=4)
        except :
            print("The file format is not correct!!")

def set_control_args():
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





def initialize_arguments(args):

    ## Add command
    if args.add is not None :
        #check the increasment Ids to give the task a unique ID 

        uni_id = int(sorted(json_text.keys())[-1][5:]) + 1
        creating_time_date = str(datetime.datetime.now())
        print(uni_id)
        describtion = args.add
        task_name=f"Task_{uni_id}"
        json_text[task_name] = task_dict.copy()
        json_text[task_name].id = uni_id
        json_text[task_name].status = "todo"
        json_text[task_name].description = description
        json_text[task_name].createdAt = creating_time_date
        json_text[task_name].updatedAt = creating_time_date
        





    elif args.update is not None :
        task_id = args.update[0]
        describtion = args.update[1]

    elif args.mark_in_progress is not None :
        task_marking = "in-progress"

    elif args.mark_todo is not None : 
        task_marking = "todo"

    elif args.mark_done is not None :
        task_marking = "done"

    elif args.list is not None :
        list_type = args.list 



creat_or_read_json(file_path)

args=set_control_args()

initialize_arguments(args)