# Holiday Manager

This project entails creating a text-based Holiday Manager that allows users to manage and modify holiday lists, which can be saved as JSON files. The techniques utilized include classes and web scraping. Additionally, the module covers object-oriented programming concepts in Python, starting from fundamental topics like variables, loops, conditionals, and functions, and then advancing to function wrappers and classes. Finally, it introduces commonly used tasks in web-based environments, including web scraping.

### Design features and requirements:
•	Created an easy-to-use interface.

•	An initial JSON file named holidays.json, containing a set of 10 starting holidays, was provided. 

•	All the holidays from https://www.timeanddate.com/holidays/us/  were preloaded. **NOTE: Only preload holidays with concrete dates. Do not calculate holiday dates. The team expects you to include holidays from the present year, 2 years of past holidays, and 2 years of future holidays.

•	The holidays were saved in JSON, following the formatting of the provided file. A distinct JSON file named savedholidays.json was generated to store all the holidays obtained from web scraping, in addition to those from the holidays.json file.

•	The weather forecast for the holidays of the current week was obtained from the following URL: https://weather.com/weather/tenday/l/3397f813e2a7833d07c1756bf7fb0ff62a68918b04566dcd9ccb15451a0a2a64

### Inside the Holiday Manager are five main sections (Interface):
  1.	Adding a Holiday - where a user can add a holiday to the holiday list
  2.	Remove a Holiday - where the user can remove a holiday currently on the holiday list
  3.	Save - where any progress made in the user session can be saved
  4.	View Holidays - where a user can specify a specific year and a specific week in that year to see what the holidays are. If you select the current week, you'll be able to select to see the weather forecast for the holidays within that week as well.
  5.	Exit - Exit Holiday Manager.

Please enjoy my Holiday Manager!
