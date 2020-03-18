import os
import importlib
import json

class Help:
    """
    A module that displays all available functionality and how to use them
    """
    def __init__(self, cli_api):
        self.cli_api = cli_api        
        with open(os.path.dirname(os.path.abspath(__file__))+"/tasks.json") as f:            
            self.data = json.load(f)
        with open(os.path.dirname(os.path.abspath(__file__))+"/help.json") as f:
            self.helptexts = json.load(f)            
    
    def main(self):

        tasks = self.data["available_tasks"]
        self.helptexts = self.helptexts["available_tasks"]    
        
        for task in tasks:
            try:
                helptext = self.helptexts[task]
            except:
                continue
            self.cli_api.show("Task: "+task+"\nBrief: "+helptext+"\n", dontSpeak=True)

def eval(cli_api, params):
    helpobj = Help(cli_api)
    helpobj.main()
