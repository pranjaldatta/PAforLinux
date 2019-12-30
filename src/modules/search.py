from bs4 import BeautifulSoup
import webbrowser
import requests


class Search:
    """

    An object that handles all the search operations. Includes general search operations. 
    -> First displays top 10 results from google allong with the summaries that google shows. 
    -> Then the user has to choose a search result (using the index value ), and then chrome is opened to display the results. 
    -> Once opened, automatically, all the search results are displayed again for futhur exploration

    Functions:
    -> search: conducts the search and scrapes the results from google
        -- Params: 
            --searchFor: query that has to be searched for
    -> display: displays a search result on the browser            

    """

    def search(self, searchFor):
        """

        Function that is used to search for a query and return the search results

        main->cnt->mw->rcnt->col(class) -> center_col->res->search->rso->bkwMgd
        """
        url = "https://www.google.com/search?q=India"
        r = requests.get(url)

        soup = BeautifulSoup(r.content, 'html.parser')
        main_data = soup.find("div", attrs={'id':'main'})
        print(main_data.prettify())
        

        
        
        """.find("div", attrs={'id':'cnt'}).find("div", attrs={'id':'mw'})
        search_data = soup.find("div", attrs={'id':'rcnt'}).find("div", attrs={'class':'col'}).find("div", attrs={'id':'center_col'})
        search_data = soup.find("div", attrs={'id':'res'}).find("div", attrs={'id':'search'}).find("div", attrs={'id':'rso'})
        """

s = Search()
s.search("abcd")