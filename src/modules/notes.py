import os
import subprocess

class notes:
    """
    A class to interface a terminal based note taking application with 
    the personal assistant.

    Full credits to the developer of this amazingly simple and effective 
    note taking application: https://github.com/pimterry/notes

    """

    def __init__(self, cli_api, query):
        self.cli_api = cli_api
        self.query = query

    def main(self):
        
        notes_cmds = {
            "new": "n",
            "find": "f",
            "open": "o",
            "ls": "ls",           
        }
        try:        
            if len(self.query.split()) == 2 : 
                help_text = "How to Use Notes ?\n \
                            notes <command> <argument if any>\n \
                            1. notes new <new note name> \n \
                            2. notes find <note name> \n \
                            3. notes open <note name> \n \
                            4. notes help \n \
                            5. notes ls \n"
                            

                _, cmd = self.query.split()

                if cmd == "help":
                    self.cli_api.show(text=help_text, dontSpeak=True)
                elif cmd == "ls":
                    subprocess.call(["notes", "ls"])
            else:
                _, cmd, param = self.query.split()
                subprocess.call(["notes", cmd, param])  
                return 0
        except:
            return 1        


def eval(cli_api, args):
    noteobj = notes(cli_api, args)
    resp = noteobj.main()
    return resp
    







