import os
import json
import argparse
import datetime

class Task_traker():

    def __init__(self):
        self.file_path = 'tasks_file.json'
        self.task_dict ={
                "id":"",
                "description":"",
                "status":"",
                "createdAt":"",
                "updatedAt":"",
            }
        self.json_text = {}

    def write_in_json_file(self):
        '''This function for write and save json file'''
        try:
            with open(self.file_path, 'w') as f:
                json.dump(self.json_text, f)
        except:
            print("Error in saving json file!!")

    def creat_or_read_json(self):
        '''This function checks if the file exists then creat or read the file'''

        if os.path.exists(self.file_path):
            with open(self.file_path) as f:
                self.json_text = json.load(f)
        else:
            try:
                with open(self.file_path, 'w' ,encoding='utf-8') as outfile:
                    json.dump(self.json_text, outfile, sort_keys=True, indent=4)
            except :
                print("The file format is not correct!!")

    def set_control_args(self):
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
        parser.add_argument('-list ', '--list',nargs="?", default='all', const='all')

        args_ = parser.parse_args()
        return args_

    def add_command(self,task_description):
            '''This function add a new task to the json file'''

            description = task_description  #Inserted description
            task_exists = False

            #Check if the task exists befor to avoid deplicated tasks
            for name , task in self.json_text.items():
                if self.json_text[name]['description']== task_description:
                    task_exists=True
                    print("This Task exists before")
                    break

            if task_exists == False:
                #Generate an unique ID 
                uni_id = int(sorted(self.json_text.keys())[-1][5:]) + 1  if len(list(self.json_text.keys()))  >=1 else 1
                #Extract time 
                creating_time_date = str(datetime.datetime.now())
                
                task_name=f"Task_{uni_id}"
                self.json_text[task_name] = self.task_dict.copy()
                self.json_text[task_name]["id"] = uni_id
                self.json_text[task_name]["status"] = "todo"
                self.json_text[task_name]["description"] = description
                self.json_text[task_name]["createdAt"] = creating_time_date
                self.json_text[task_name]["updatedAt"] = creating_time_date
                
                #save the json file 
                self.write_in_json_file()

                print(f'Task added successfully (ID: {uni_id})')

    def update_command(self,task_id,new_task_describtion=None ,task_status=None):
        '''This function update (describtion - status ) of the tasks which are existed before'''

        updating_time_date = str(datetime.datetime.now())
        task_name=f"Task_{task_id}"
        try :
                
            self.json_text[task_name]["updatedAt"] = updating_time_date

            if task_status == None:
                #update the description 
                self.json_text[task_name]["description"] = new_task_describtion
            else :
                #update the task status 
                self.json_text[task_name]["status"] = task_status

            #save the json file 
            self.write_in_json_file()

            print(f'Task updated successfully (ID: {task_id})')
        except:
            print(f"Task with ID = {task_id} does not exist")

    def delete_command(self,task_id):
        '''This function delete the task'''
        #json_text , task_dict  global

        task_name=f"Task_{task_id}"
        try:
            self.json_text.pop(task_name)
            self.write_in_json_file()
            print(f'Task deleted successfully (ID: {task_id})')
        except:
            print(f"Task with ID = {task_id} does not exist")

    def list_command(self,List_type):
        '''This function list the tasks based on the list type'''

        task_in_type =[]
        if List_type not in  ['done', 'todo', 'in-progress','all']:
            print(f"The list of tasks does not exist")
        else:
        
            for task_name , task in self.json_text.items():
                if self.json_text[task_name]['status']==List_type or List_type =="all":
                    task_in_type.append(self.json_text[task_name]["description"])

            if len(task_in_type) == 0:
                print(f"The list of tasks '{List_type}' is empty")
            else:
                if List_type == "all":
                    print(f"The list of all tasks :")
                else:
                    print(f"The list of tasks '{List_type}':")
                for task in task_in_type:
                    print(f"- {task} ")

    def handle_commands(self,args):
        '''This function to handle the input commands from the user'''

        if args.add is not None :  ## Add command
            self.add_command(args.add)

        elif args.update is not None : ## Update command
            self.update_command(args.update[0],args.update[1])

        elif args.delete is not None : ## Delete command
            self.delete_command(args.delete)

        elif args.mark_in_progress is not None :## Update task status to in-progress
            self.update_command( args.mark_in_progress ,task_status="in-progress")
        
        elif args.mark_todo is not None :  ## Update task status to todo
            self.update_command( args.mark_todo ,task_status="todo")

        elif args.mark_done is not None : ## Update task status to done
            self.update_command( args.mark_done ,task_status="done")

        elif args.list is not None : ## List command
            self.list_command(args.list)

    def main(self):
        '''This function calls function to make the workflow works'''

        self.creat_or_read_json() # creat or read json file

        args = self.set_control_args() # get input from users

        self.handle_commands(args) # deal with the commands


if __name__ == "__main__":

    tracker = Task_traker()
    tracker.main()