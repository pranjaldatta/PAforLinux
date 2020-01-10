import requests
import json
import os

class dictionary:
    """

    A module that return definition, synonymns of a word
    Note: can explore the api more. include subsenses, synonymns etc

    """
    def __init__(self, cli_api, params):
        self.cli_api = cli_api
        self.params = params
        self.appID = None
        self.appKey = None
        self.base_url = None
        with open("/home/pranjal/Projects/PAforLinux/src/modules/keys.json") as f:
            data = json.load(f)
            self.appID = data[os.path.basename(__file__)]["app_id"]
            self.appKey = data[os.path.basename(__file__)]["app_key"]
            self.base_url = data[os.path.basename(__file__)]["base_url"]

    def main(self):
        _, self.params = self.params.split(" ", 1)

        r = requests.get(self.base_url+"/entries/en-us/"+self.params.lower()+"?fields="+"definitions", 
            headers={'app_id': self.appID, 'app_key': self.appKey})
        if r.status_code == 404:
            self.cli_api.show(text="Sorry no such word found!", color="cyan")
        else:    
            self.cli_api.show(text="Here's what it means...", color="cyan")            
            r = r.json()        
            results = r["results"][0]
            #print(results['lexicalEntries'])
            for res in results['lexicalEntries']:
                if len(results['lexicalEntries']) > 1:
                    self.cli_api.show(text="------------------------------------", color="cyan")
                self.cli_api.show(res['entries'][0]['senses'][0]['definitions'][0])
        return 0
            
def eval(cli_api, params):
    dic = dictionary(cli_api, params)
    return dic.main()

