import webbrowser
from .check_connection import check_connection

class Play:
    """

    A task that plays a video on youtube

    """
    def __init__(self, cli_api, query):
        self.cli_api = cli_api
        self.query = query

    def main(self):
        if check_connection() == False:
            self.cli_api.show("Error: No Internet Connection Found!", "red")
            return 1
        _, query = self.query.split(" ", 1)
        webbrowser.open("https://www.youtube.com/results?search_query={}".format(query), 1)
        return 0

def eval(cli_api, params):
    play = Play(cli_api, params)
    return play.main()

