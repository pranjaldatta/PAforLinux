from interpreter import Interpreter
from colorama import Fore
import os
from cmd import Cmd

class Assistant(Interpreter, object):
    """

    main module that handles all the functions fo the PA. 
    For example, if a search command is entered, the cli refers to the 
    search api and returns a result.

    """

    def __init__(self):
        self._colors = {
            "red": Fore.RED,
            "blue": Fore.BLUE,
            "green": Fore.GREEN,
            "cyan": Fore.GREEN,
            "white": Fore.WHITE
        }

        Interpreter.__init__(self)

        
                


        