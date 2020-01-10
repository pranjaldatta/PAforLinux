import argparse

class demo_task:
    
    def __init__(self, cli_api):
        self.cli_api = cli_api
        

    def demo_task_func(self):
        text = self.cli_api.cmd_args_text("hey send me some text to print pls!", color="magenta")
        self.cli_api.show(color= "cyan",text=text)
        return 200

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--cli", help="Object to handle command line operations", action="store")
args = parser.parse_args()
demo_tsk = demo_task(args.cli)
demo_tsk.demo_task_func()
