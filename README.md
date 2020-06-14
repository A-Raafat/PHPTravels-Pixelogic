# PHPTravels-Pixelogic
Assignment for Pixelogic media

The project is built in Python 3.7

# Project libraries used:
- selenium for webdriver interface  installed using '''pip install selenium'''
- os for getting paths
- time for delays
- re for regural expressions and putting the rules
- PIL for image capturing
- sys for extracting assertion information
- traceback for getting the last assertion values
- inspect to get current function name
- unittest to run multiple test cases

# How it works
It is composed of 2 classes, PHPTravelregister for the data entering and checking, and WebsiteTest which is used to test the testcases. also there is utility function slow_typing in order not to be captured as a bot.
At first the class uses the browser and goes through the specified link, then goes through multiple checking of the entered data, where it takes a screenshot after typing wrong data format.
The wrong data format is checked through rules done by regural expressions. and if there is wrong data, a screenshot is taken and assertion is raised then sent to the WebsiteTest class

### For testing : 
You just add your desired test case in test.py function ( just copy one of the functions and edit the first name, last name, number.. etc ) and run the code.
Then it will create the screenshots for wrong data format and outputs the successful and failed test cases in text file.

# Features and Limitations : 
It checks for any mobile number with a country code or not but it fails when the user inputs dashes for ex. "15-056"
