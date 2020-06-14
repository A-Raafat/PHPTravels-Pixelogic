from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome, ChromeOptions
import PIL.ImageGrab as image
import os
import time
import re

#browser = Chrome('C:\Program Files (x86)\chromedriver')
#browser.get('https://www.phptravels.net/register')

#print(browser.title)
#slow_typing(browser.find_element_by_name("firstname"), 'om')
#browser.close()


def slow_typing(element, text):
    for character in text:
        element.send_keys(character)
        time.sleep(0.15)

class PHPTravelregister():
    
    def __init__(self, chrome_path, FName, LName, Number, Email, Password, ConfirmPassword, f_name):
        
        #options = ChromeOptions()
        #options.add_argument("--start-maximized")
        self.chrome_path = chrome_path
        self.browser = Chrome(chrome_path)
        self.browser.get('https://www.phptravels.net/register')
        
        self.FName = FName
        self.LName = LName
        self.Number = Number
        self.Email = Email
        self.Password = Password
        self.ConfirmPassword = ConfirmPassword        
        self.f_name = f_name
        
    def signup(self):
        time.sleep(2)
        self.browser.find_element_by_class_name('cc-btn').click()
        
        slow_typing(self.browser.find_element_by_name("firstname"), self.FName)
        self.check_first()
        
        slow_typing(self.browser.find_element_by_name("lastname"), self.LName)
        self.check_last()
        
        slow_typing(self.browser.find_element_by_name("phone"), self.Number)
        self.check_phone()
        
        
        slow_typing(self.browser.find_element_by_name("email"), self.Email)
        self.check_email()
        
        slow_typing(self.browser.find_element_by_name("password"), self.Password)
        self.check_password()
        
        slow_typing(self.browser.find_element_by_name("confirmpassword"), self.ConfirmPassword)
        self.check_confirmpassword()
        
        self.browser.find_element_by_class_name('signupbtn').click()
        time.sleep(3)
        
        if(self.browser.title =='My Account'):
            print('Sign up succeeded!')
            self.browser.close()
            self.validate()
        else:
            assert False, ['Email Already exist!', image.grab().save(os.getcwd()+ '\\' + self.f_name +'.png'),  self.browser.close()] 
        
        
        
    def validate(self):
        self.browser = Chrome(self.chrome_path)
        self.browser.get('https://www.phptravels.net/login')
        slow_typing(self.browser.find_element_by_name("username"), self.Email)
        slow_typing(self.browser.find_element_by_name("password"), self.Password)
        self.button = self.browser.find_element_by_class_name('loginbtn').click()
        
        
        time.sleep(3)
        if(self.browser.title =='My Account'):
            print('Log in succeeded!')
            image.grab().save(os.getcwd()+ '\\' + 'Validate.png')
        else:
            print('Validation failed!') 
        time.sleep(2)
        self.browser.close()
        
            
    def check_first(self):
        assert(self.FName[0].isupper() and not bool(re.search(r'\d', self.FName))), ['Enter First Name which must start with capital letter.', image.grab().save(os.getcwd()+ '\\' + self.f_name +'.png'), self.browser.close()]
            
    def check_last(self):
        assert(self.FName!=self.LName and self.LName[0].isupper() and not bool(re.search(r'\d', self.LName))), ['Enter Last Name which must start with capital letter and can’t be equal First Name.', image.grab().save(os.getcwd()+ '\\' + self.f_name +'.png'), self.browser.close()]

    def check_email(self):
        email_rule = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        assert re.search(email_rule, self.Email), ['The Email field must contain a valid email address.', image.grab().save(os.getcwd()+ '\\' + self.f_name +'.png'), self.browser.close()]
        
    def check_password(self):
        assert (re.search('[a-z]', self.Password) and re.search('[A-Z]', self.Password) and 5<=len(self.Password)<=8), ['The Password must have capital letter, small letter, and a limit of 5-8 characters.', image.grab().save(os.getcwd()+ '\\' + self.f_name +'.png'), self.browser.close()]   
        
    def check_confirmpassword(self):
        assert self.Password == self.ConfirmPassword, ['Password not matching with confirm password.', image.grab().save(os.getcwd()+ '\\' + self.f_name +'.png'), self.browser.close()]
        
    def check_phone(self):
        num = [''.join(i) for i in self.Number.split('+') if i]
        assert (num[0].isnumeric() and len(num)==1 and len(num[0])>10), ['Enter a valid Mobile Number.', image.grab().save(os.getcwd()+ '\\' + self.f_name +'.png'), self.browser.close()]

'''
path = 'C:\Program Files (x86)\chromedriver'
PHPTravelregister(chrome_path = path,
                  FName = 'Ahmed',
                  LName = 'Raafat',
                  Number = '+00061200002',
                  Email = '12s3@aa.net',
                  Password = 'pa-A**-6',
                  ConfirmPassword = 'pa-A**-6' ).signup()
'''