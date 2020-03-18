import calendar
import argparse 

class CalendarModule:
    """
    Module that shows the calendar for a given month
    """    
    def show(self, month, year):
        """
        displays the calendar
        """
 
        calendar.setfirstweekday(calendar.SUNDAY)
        cal = calendar.monthcalendar(year, month)
 
        if len(str(month)) == 1:
            month = '0%s' % month
        
        print ('|++++++ %s-%s +++++|' % (month, year))
        print ('|Su Mo Tu We Th Fr Sa|')
        print ('|--------------------|')
 
        border = '|'
        for week in cal:
            line = border    
            for day in week:
                if day == 0:
                    line += '   ' 
                elif len(str(day)) == 1:
                    line += ' %d ' % day
                else:
                    line += '%d ' % day 
            line = line[0:len(line) - 1] 
            line += border
            print (line) 
        print ('|--------------------|\n')

def eval(cli_api, params):
    _, month, year = params.split()
    months = {
        "january" : "1",
        "jan": "1",
        "february": "2",
        "feb": "2",
        "march": "3",
        "mar": "3",
        "april": "4",
        "apr": "4",
        "may": "5",
        "may": "5",
        "june": "6",
        "jun": "6",
        "july": "7",
        "jul": "7",
        "august": "8",
        "aug": "8",
        "september": "9",
        "sept": "9",
        "october": "10",
        "oct": "10",
        "november": "11",
        "nov": "11",
        "december": "12",  
        "dec": "12"          
    }    
    try:
        month = int(month)
    except ValueError:
        month = int(months[month])
    calobj = CalendarModule()
    calobj.show(month, int(year))

    
             


