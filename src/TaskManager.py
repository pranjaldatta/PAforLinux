import os
import json
import subprocess
import sys
import importlib



class TaskManager:
    """

    A module which does the follwoing:
    -> associates some common predefined commands with certain tasks
    -> uses NLP models to interpret user input and map it to a certain task
    -> depending on the task, returns an appropriate task module

    """
    def __init__(self, cli_api, user_input = None):
        self.cli_api = cli_api
        self.user_input = user_input
        with open(os.path.dirname(__file__)+"/modules/tasks.json") as f:
            self.data = json.load(f)

    def check_for_predefined_cmd(self, cmd):
        """

        Function that checks whether a command provided by the user is
        predefined or not

        """ 
        cmd = cmd.split(" ", 1)
        try:
            task = self.data["available_tasks"][cmd[0]]
            return task
        except KeyError:
            return 127    

    def execute_task_module(self, task, params):
        """
        
        executes task module. and returns value

        """
        
        task, _ = task.split(".")
        #print("task:", task)
        #print("here:", os.path.join(os.path.dirname(__file__), task))
        task_module = importlib.import_module("..{}".format(task), "modules.subpkg")
        return task_module.eval(self.cli_api, params)
        
        





