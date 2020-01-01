import os
from colorama import Fore
from CommandLine import CommandLineAPI
from modules.demo_module import demo_task
from cmd import Cmd

class Assistant:
    """

    The main controller file. It handles all the operations of the assistant. 
    It controls the command line functions, calls the task modules and handles
    associated control ops.

    """
    def __init__(self):
        self.cli_api = None

    def _init_cli_api(self):
        self.cli_api = CommandLineAPI()    

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
            self.cli_api.show(self.cli_api._prompt, "blue")
        inp = input()
        #analyse inp for task . For now we are using a dummy function for demo
        #command analysis code here
        #self.execute_task(None, demo_only=inp)
        
        task = inp #for now. its actually the result of the nlp analysis
        return task

    def execute_task(self, task, demo_only):
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
         
        demo = demo_task(self.cli_api)
        code = demo.demo_task_func()
        

        return code

    def postcmd(self, code):
        """

        Function that handles post command execution ops.

        :param code: success or failure code for the given task

        """
        if code != 200:
            self.cli_api.show("Unknown Error", color="red")
        else:
            self.precmd(False)    

    def main(self):
        """

        The main controller function. It coordinates all activities.

        """
        
        try:          
            self.cli_api = CommandLineAPI()
            init_user_response = self.precmd()
            while True:
                resp_code = self.execute_task(init_user_response)
                self.postcmd(resp_code)
        except KeyboardInterrupt:
            self.cli_api.exit()   
   
        

"""    
assist = Assistant() 
assist.precmd()
"""
if __name__ == "__main__":
    assist =  Assistant()
    assist.main()