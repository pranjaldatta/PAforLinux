from cmd import Cmd
from colorama import Fore,Style

class Interpreter:
    """
    A module that handles the interpreter interface.

    Functions:
    -> show : Prints data into the command line
    -> input : Accepts commands from the command line
    """
    def __init__(self):
        self.hello = "hello"

    def show(self, text, color=None):
        """

        prints a result/error into the command line.

        :param text: Information/error that needs to be printed
        :param color: color of text
        
        """
        if color is None:
            color = Fore.WHITE
        print(color + text + Fore.RESET)

    def inputText(self, prompt=""):
        """

        Accepts an input text from the user

        :param Prompt: Prompt message

        """
        inp = input(Fore.CYAN +prompt + Fore.RESET+"\n")
        return inp.strip()

    
    
