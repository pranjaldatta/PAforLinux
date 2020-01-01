class demo_task:
    
    def __init__(self, cli_api):
        self.cli_api = cli_api
        

    def demo_task_func(self):
        text = self.cli_api.cmd_args_text("hey send me some text to print pls!", color="magenta")
        self.cli_api.show(color= "cyan",text=text)
        return 200


