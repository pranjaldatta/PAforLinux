import bs4
import webbrowser

class search:
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