import wikipedia
import requests


class wiki:
    """

    A module that fetches wikipedia articles.

    """
    def __init__(self, cli_api, params):
        self.cli_api = cli_api
        self.params = params
    
    def _search(self, query, suggest_list=None, index=None):
        
        if index is not None:
            query = suggest_list[int(index)-1]
        self.cli_api.show(text="Hold on! fetching results...", color='cyan')    
        self.cli_api.show(text=wikipedia.summary(query))
    
    def main(self):
        _, self.params = self.params.split(" ", 1)
        resp_list = wikipedia.search(self.params, suggestion=True)
        
        if resp_list[0] == [] and resp_list[1] is not None:
            if isinstance(resp_list[1], str) is True:
                resp_list = [resp_list[1]]
            elif isinstance(resp_list[1], list) is True:
                resps = []
                for item in resp_list[1]:
                    resps.append(item)
                resp_list = resps
        else:
            resp_list = resp_list[0]
                
        resp_list = [x.lower() for x in resp_list]
        try:
            ind = resp_list.index(self.params)
            self._search(query=self.params)             
        except ValueError:                
            self.cli_api.show(text="Sorry! No Such Wikipedia page exists!", color='cyan')
            self.cli_api.show(text="But does any of the following pages cover the topic?", color='cyan')
            self.cli_api.show(text="Enter the index number and I will fetch them...", color='cyan')
            index = 1
            for item in resp_list:
                self.cli_api.show("{}. {}".format(index, item))
                index+=1
            index = self.cli_api.cmd_args_text(prompt=None)
            self._search(None,resp_list,index=index)

        return 0
                  



def eval(cli_api, params):
    wiki_obj = wiki(cli_api, params)
    return wiki_obj.main()