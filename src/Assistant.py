import os
from colorama import Fore
from CommandLine import CommandLineAPI
from cmd import Cmd
from TaskManager import TaskManager
from random import randint

class Assistant:
    """

    The main controller file. It handles all the operations of the assistant. 
    It controls the command line functions, calls the task modules and handles
    associated control ops.

    """
    def __init__(self):
        self.cli_api = None
        self.task_manager = None

    #def _init_cli_api(self):
        #self.cli_api = CommandLineAPI()
        #self.task_manager = TaskManager(self.cli_api)    

    def precmd(self, init=True):
        """

        Function that is used to accept a user response.
        Does the following:
        1. Accepts a user input
        2. Uses a NLP api to figure out a task. (Even checks predefined responses if any)
        3. Calls execute_task method to actually execute the given task

        :param init: Indicates whether this is the first user input. Made false by postcmd

        """ 
        if init == False:
            self.cli_api.show(self.cli_api._prompt[randint(0, len(self.cli_api._prompt) - 1)], color="blue")
        inp = input()
        inp = inp.lower()
        #analyse inp for task . For now we are using a dummy function for demo
        #command analysis code here
        #self.execute_task(None, demo_only=inp)

        task = self.task_manager.check_for_predefined_cmd(inp)
        #if isinstance(task, int):
            #call nlp model
            #task = ...      
        return (task, inp)
    def execute_task(self, task, params):
        """

        Function that is used to execute a particular task.
        Does the following:
        1. Accepts a task
        2. calls the required task module
        3. after successful execution, calls postcmd

        :param task: name of the task that needs to be executed.
                     Can be index corressponding to a given task
                     defined by a global scheme.

        """ 
        #print("task:", task) 
        code = self.task_manager.execute_task_module(task, params)
        return code

    def postcmd(self, code):
        """

        Function that handles post command execution ops.

        :param code: success or failure code for the given task

        """
        if code == 126: #unkown error
            self.cli_api.show("Unknown Error", color="red")
        elif code == 127:
            self.cli_api.show("Sorry! I cannot perform this task yet.", color="red")    

    def main(self):
        """

        The main controller function. It coordinates all activities.

        """        
        try:          
            self.cli_api = CommandLineAPI()
            self.task_manager = TaskManager(self.cli_api)
            resp_code = 127
            task_and_inp = self.precmd()
            while True:
                if isinstance(task_and_inp[0], int) == False:
                    resp_code = self.execute_task(task_and_inp[0], task_and_inp[1])                
                self.postcmd(resp_code)
                task_and_inp = self.precmd(init=False)

        except KeyboardInterrupt:
            self.cli_api.exit()   
   
        

"""    
assist = Assistant() 
assist.precmd()
"""
if __name__ == "__main__":
    assist =  Assistant()
    assist.main()