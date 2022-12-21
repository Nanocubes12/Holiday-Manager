import datetime
import json
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass


# -------------------------------------------
# Modify the holiday class to 
# 1. Only accept Datetime objects for date.
# 2. You may need to add additional functions
# 3. You may drop the init if you are using @dataclassess
# --------------------------------------------

class Holiday:
    def __init__(self,name, date):
        self.name= name
        self.date= date

    
    def __str__ (self):
        return f'{self.name}, {self.date}'

        # String output
        # Holiday output when printed.
           
# -------------------------------------------
# The HolidayList class acts as a wrapper and container
# For the list of holidays
# Each method has pseudo-code instructions
# --------------------------------------------
class HolidayList:

    def __init__(self):
       self.innerHolidays = []
   
    def addHoliday(self,holidayObj):   
        if type(holidayObj)==Holiday:                     # Make sure holidayObj is an Holiday Object by checking the type
            self.innerHolidays.append(holidayObj)    # Use innerHolidays.append(holidayObj) to add holiday
        
        return holidayObj 
        
    def findHoliday(self,HolidayName, Date):
        # Find Holiday in innerHolidays
        for i in self.innerHolidays:
            if type(i) == Holiday:
                if HolidayName == str(i).split(',')[0] and str(Date) == str(i).split(', ')[1]:
                    return i # Return Holiday
            
    def removeHoliday(self,HolidayName, Date):
        removeSuccess= True
        
         # Find Holiday in innerHolidays by searching the name and date combination.
        for i in self.innerHolidays:
            if type(i) == Holiday:
                if HolidayName == str(i).split(',')[0] and str(Date) == str(i).split(', ')[1]:
                    self.innerHolidays.remove(i)    # remove the Holiday from innerHolidays
                    removeSuccess= False

        # inform user you deleted the holiday
        if removeSuccess == False:
            print(f'The Holiday {HolidayName} on {Date} has been removed')
        else:
            print(f'Error:\n{HolidayName} not found')

                

    def read_json(self,filelocation):
        with open(filelocation,'r') as h: 
            holiday= json.load(h)                   # Read in things from json file location

        holi= holiday['holidays']
        for i in range(len(holi)):
            name= holiday['holidays'][i]['name']
            date= holiday['holidays'][i]['date']
            self.addHoliday(Holiday(name,date))      # Use addHoliday function to add holidays to inner list

    def get_date(self):
         # Verify User Input Date
        dateConfirmed=True
        while dateConfirmed==True:
            date= str(input('Enter the Holiday\'s Date [format:YYYY-MM-DD]\n'))
            try:
                date= [int(item) for item in list(date.split('-'))]
                date= datetime.date(date[0],date[1],date[2])
                dateConfirmed=False
                return date
            except:
                print('Error:\nInvalid date.Please try again.')


    def exitConfirmed(self):
        exitConfirmation=True
        while exitConfirmation==True:
            exit_input= input('Are you sure you want to exit? [y/n]: ')
            if exit_input.lower()== 'y' or exit_input.lower() =='n':
                exitConfirmation= False
                return exit_input
            else: 
                print('Invalid input. Try Again')

    def saveConfirmed(self):
        saveConfirmation=True
        while saveConfirmation==True:
            save_input= input('Are you sure you want to save your changes? [y/n]: ')
            if save_input.lower()== 'y' or save_input.lower() =='n':
                saveConfimation= False
                return save_input
            else: 
                print('Invalid input. Try Again')

    def save_to_json(self,filelocation):
        dictValues=[]
        ToSave={}
        for i in self.innerHolidays:
            dictValues.append({"name": str(i).split(',')[0],"date": str(i).split(', ')[1]})
            ToSave.update({"holidays":dictValues})
        with open(filelocation,'w') as f: # Write out json file to selected file.
            json.dump(ToSave,f, indent= 4)
       
    def scrapeHolidays(self):
        year= 2022
        url='https://www.timeanddate.com/holidays/us/'
        # holiday= []
        dictValues=[]
        holidays= {}

        for year in range(year-2, year+3):

            # year_url= url + str(year)
            request= requests.get(url)
            html= BeautifulSoup(request.text,'html.parser')
            table= html.find('table').find('tbody')
            rows= table.find_all('tr')

            for row in rows:
                if len(row.contents) == 0:
                    continue

                date_str= row.find('th').contents[0] + ' ' + str(year)
                format= '%b %d %Y'
                date= str(datetime.datetime.strptime(date_str, format).date())
                name= row.find_all('td')[1].find('a').contents[0].replace(',',':')


                self.addHoliday(Holiday(name,date))
        
        
        # Scrape Holidays from https://www.timeanddate.com/holidays/us/ 
        # Remember, 2 previous years, current year, and 2  years into the future. You can scrape multiple years by adding year to the timeanddate URL. For example https://www.timeanddate.com/holidays/us/2022
        # Check to see if name and date of holiday is in innerHolidays array
        # Add non-duplicates to innerHolidays
        # Handle any exceptions.     

    def numHolidays(self):
        num= len(self.innerHolidays)
        return num
        # Return the total number of holidays in innerHolidays
    
    def filter_holidays_by_week(self,year, week_number):
        holidays=[]
        for i in self.innerHolidays:
            d2= datetime.datetime.strptime(str(i).split(', ')[1],'%Y-%m-%d').date()
            if (int(year) == d2.isocalendar()[0]) and (int(week_number) == d2.isocalendar()[1]):
                  holidays.append(str(i))
        
        return holidays
            
        # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
        # Week number is part of the the Datetime object
        # Cast filter results as list
        # return your holidays

    def viewOtherWeek (self, year, weekNumber):
        list_holiday= self.filter_holidays_by_week(year,weekNumber)
        self.displayHolidaysInWeek(list_holiday)

    def displayHolidaysInWeek(self,holidayList):
       
        # holidayWeeks= self.filter_holidays_by_week()
        if len(holidayList)==0:
            print("There are no holidays for this week")
        else:
            for x in holidayList:
                print(x)
        # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
        # Output formated holidays in the week. 
        # * Remember to use the holiday __str__ method.

    def getWeather(self,weekNum):
        pass
        # Convert weekNum to range between two days
        # Use Try / Except to catch problems
        # Query API for weather in that week range
        # Format weather information and return weather string.

    def viewCurrentWeek(self):
        weeknumber=datetime.datetime.now().isocalendar()[1] 
        todays_year=datetime.datetime.now().isocalendar()[0]
        list_holiday= self.filter_holidays_by_week(todays_year,weeknumber)
        
        
        self.displayHolidaysInWeek(list_holiday)
        
        # Use the Datetime Module to look up current week and year
        # Use your filter_holidays_by_week function to get the list of holidays 
        # for the current week/year
        # Use your displayHolidaysInWeek function to display the holidays in the week
        # Ask user if they want to get the weather
        # If yes, use your getWeather function and display results



def main(): 
    
    # Large Pseudo Code steps
    # -------------------------------------
    # 1. Initialize HolidayList Object
    init_holidays = HolidayList()
    # 2. Load JSON file via HolidayList read_json function
    init_holidays.read_json('holidays.json')
    # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
    init_holidays.scrapeHolidays()

    print('\nHoliday Management\n===================')
    numholidays= init_holidays.numHolidays()
    print(f'There are {numholidays} holidays stored in the system\n')
    
    # 3. Create while loop for user to keep adding or working with the Calender
    menu= True
    while menu==True:
         # 4. Display User Menu (Print the menu)
        print('\nHoliday Menu\n================')
        print('1. Add a Holiday')
        print('2. Remove a Holiday')
        print('3. Save a Holiday')
        print('4. View Holidays')
        print('5. Exit')

        user_input= int(input('Choose from the Menu: '))

        if user_input ==1:
            holidayName= str(input('Enter Holiday Name\n'))
            date= init_holidays.get_date()
            result=init_holidays.addHoliday(Holiday(holidayName, date))
            print(f'{result} has been added to the list\n') 
        elif user_input ==2:
            holidayName= str(input('Enter the Holiday Name you will like to Remove\n'))
            date= init_holidays.get_date()
            init_holidays.removeHoliday(holidayName, date)
        elif user_input ==3:
            saveConfirmation= init_holidays.saveConfirmed()
            if saveConfirmation == 'y':
                init_holidays.save_to_json('savedHolidays.json')
                print('Your changes have been saved.')
            elif saveConfirmation == 'n':
                print('Canceled:\nHoliday list file save canceled.')
        elif user_input ==4:
            current_other= input('Would you like to see holidays for current week? [y:n]: ')
            if current_other.lower() == 'y':
                init_holidays.viewCurrentWeek()
            elif current_other.lower() == 'n':
                year= input('What year?: ')
                week_number= input('what week? #[1-52, Leave blank for the current week]: ')
                init_holidays.viewOtherWeek(year,week_number)
            else:
                print('Not a valid input')
        elif user_input ==5:
            exitConfirmation= init_holidays.exitConfirmed()
            if exitConfirmation == 'y':
                menu= False
            elif exitConfirmation == 'n':
                menu= True
        else:
            print('Not a valid input')

            


    
    # 5. Take user input for their action based on Menu and check the user input for errors
    # 6. Run appropriate method from the HolidayList object depending on what the user input is
    # 7. Ask the User if they would like to Continue, if not, end the while loop, ending the program.  If they do wish to continue, keep the program going. 


if __name__ == "__main__":
    main();


# Additional Hints:
# ---------------------------------------------
# You may need additional helper functions both in and out of the classes, add functions as you need to.
#
# No one function should be more then 50 lines of code, if you need more then 50 lines of code
# excluding comments, break the function into multiple functions.
#
# You can store your raw menu text, and other blocks of texts as raw text files 
# and use placeholder values with the format option.
# Example:
# In the file test.txt is "My name is {fname}, I'm {age}"
# Then you later can read the file into a string "filetxt"
# and substitute the placeholders 
# for example: filetxt.format(fname = "John", age = 36)
# This will make your code far more readable, by seperating text from code.





