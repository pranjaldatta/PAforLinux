from cmd import Cmd
from colorama import Fore
import pyttsx3 as tts

class CommandLineAPI:
    """

    Thee CommandLineAPI handles all the command line operations. All common command 
    line related operations are implemented here.                                                                

    """

    def __init__(self):
        self._init_prompt = "Hello! How may I help you?"
        self._prompt = "Can I be of more assistance?"
        self._prompt_char = "->"
        self._colors = {
            "red" : Fore.RED,  #For errors
            "blue" : Fore.BLUE, #For prompts
            "green" : Fore.GREEN, #For fetch waits
            "cyan" : Fore.CYAN,  #one line replies
            "reset" : Fore.RESET,
            "default" : Fore.WHITE,
            "magenta" : Fore.MAGENTA #For task prompts
        }
        self.tts_engine = tts.init()
        self.speak = True
        self.tts_engine.setProperty("rate", 168)
        print(self._colors["blue"] + self._init_prompt + self._colors["reset"])
        if self.speak == True:
            self.tts_engine.say(self._init_prompt)
            self.tts_engine.runAndWait()       

    def show(self, text, color=None, speakOnly=None):
        """

        This functions is used to display everything into the command
        line.

        :param text: text that has to displayed.
        :param color: color that the text has to be printed in.

        """
        if color is None:
            color = "default"
        print(self._colors[color] + text + self._colors["reset"])

        if self.speak == True:
            if speakOnly is not None:
                self.tts_engine.say(speakOnly)
                self.tts_engine.runAndWait()
            else:    
                self.tts_engine.say(text)
                self.tts_engine.runAndWait()

    def cmd_args_text(self, prompt, color=None):
        """

        This function is used to accept furthur arguments required by 
        a certain task. Invoked by a certain task. 

        :param prompt: prompt which is sent by the task
        :param color: color of prompt- can be general scheme or any 
                      specific scheme required by the task 

        """ 
        if prompt is None:
            inp = input()
        else:
            inp = input(self._colors[color] + prompt + self._colors["reset"] + "\n")

        return inp.strip()

    def cmd_args_num(self, prompt, dtype=int, min=None, max=None, color=None):
        """

        This function is used to accept furthur arguments required by 
        a certain task. Invoked by a certain task. 

        :param prompt: prompt which is sent by the task
        :param color: color of prompt- can be general scheme or any 
                      specific scheme required by the task.
        :param dtype: datatype of the numbers required
        :param min: minimum threshold of the numerical input
        :param max: maximum threshold of the numerical output              

        """    
        try:
            if min is None and max is None:
                inp = input(self._colors[color] + prompt + self._colors["reset"] + "\n")
                return dtype(inp)
            else:                
                inp = dtype(input(self._colors[color] + prompt + self._colors["reset"] + "\n"))
                if max is None and inp < min:
                    raise ValueError
                if min is None and inp > max:
                    raise ValueError
                else:
                    return inp
        except ValueError:
            return ValueError

    def dummy_func(self):
        num =  self.cmd_args_num("Enter a number")
        print("The number is : ", num)


    def exit(self):
        print(self._colors['blue'] + "Goodbye! See Ya later!" + self._colors['reset'])
        if self.speak == True:
            self.tts_engine.say("Goodbye! See Ya later!")
            self.tts_engine.runAndWait()        
    

"""
cmdLine = CommandLineAPI()
val = cmdLine.cmd_args_num("enter a float", dtype=int, min=10.0, color="red")
"""