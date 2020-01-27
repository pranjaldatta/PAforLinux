import os

class battery:
    """

    A module that shows battery related information

    """
    def __init__(self, cli_api):
        self.cli_api = cli_api

    def main(self):    
        cmd = "upower -i /org/freedesktop/UPower/devices/battery_BAT0 "+ \
              "| grep \"vendor\|power supply\|updated\|state\|voltage\|"+ \
              "percentage\|time to full\" $1"
        var = os.popen(cmd).read()
        response = ""
        for line in var.splitlines():
            response += line.strip() + "\n"
    
        if self.cli_api.speak == True:
            cmd = "upower -i /org/freedesktop/UPower/devices/battery_BAT0 "+ \
                "| grep \"power supply\|state\|percentage\|time to full\" $1"          
            var = os.popen(cmd).read()
            sepakResponse = ""
            for line in var.splitlines():
                sepakResponse += line.strip() + "\n"            
            
            self.cli_api.show(text=response, speakOnly=sepakResponse)
        else:
            self.cli_api.show(text=response)    


def eval(cli_api, params):
    bat = battery(cli_api)
    bat.main()
