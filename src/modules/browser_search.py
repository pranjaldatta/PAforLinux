import webbrowser
from .check_connection import check_connection
import argparse
import subprocess


class browser_search:
    """

    Task used to open up a fresh search session in the browser

    """
    def __init__(self, cli_api, query):
        self.cli_api = cli_api
        self.query = query
        
        

    def main(self):
        
        if check_connection() == False:
            self.cli_api.show("Error: No Internet Connection Found!", "red")
            return 1   
        _, self.query = self.query.split(" ", 1)
        webbrowser.open("https://www.google.com/search?q={}".format(self.query), 2)
        return 0

def eval(cli_api, args):
    
    bs = browser_search(cli_api, args)
    resp_code = bs.main()
    return resp_code
 