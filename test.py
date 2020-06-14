import unittest
import traceback
import sys
import PM
from PM import PHPTravelregister
import inspect


def get_tb(tb):
    traceback.print_tb(tb) # Fixed format
    tb_info = traceback.extract_tb(tb)
    filename, line, func, text = tb_info[-1]
    return text


class WebsiteTest(unittest.TestCase):
    def setUp(self):
        self.path = 'C:\Program Files (x86)\chromedriver'
        self.f = open('testresults.txt', 'a')

    def test_first_name(self):
        f_name = inspect.currentframe().f_code.co_name 
        try:
            PHPTravelregister(chrome_path = self.path,
                              FName = 'Ah0med',
                              LName = 'Raafat',
                              Number = '+00061200002',
                              Email = '12s3@aa.net',
                              Password = 'pa-A**-6',
                              ConfirmPassword = 'pa-A**-6',
                              f_name = f_name).signup()
            
            self.f.write('function '+f_name+' Success\n')         
        except AssertionError: 
            text = get_tb(sys.exc_info()[2])
            self.f.write('function '+f_name+' failed : '+ text.split(', [')[1][1:-84]+'\n')
    def test_number(self):
        f_name = inspect.currentframe().f_code.co_name 
        try: 
            PHPTravelregister(chrome_path = self.path,
                      FName = 'Ahmed',
                      LName = 'Raafat',
                      Number = '+000+61200002',
                      Email = '12s3@aa.net',
                      Password = 'pa-A**-6',
                      ConfirmPassword = 'pa-A**-6',
                      f_name = f_name).signup()
            
            self.f.write('function '+f_name +' Success\n')
        except AssertionError:
            text = get_tb(sys.exc_info()[2])
            self.f.write('function '+f_name+' failed : '+ text.split(', [')[1][1:-84]+'\n')
                
    def test_last_name(self):
        f_name = inspect.currentframe().f_code.co_name 
        try: 
            PHPTravelregister(chrome_path = self.path,
                      FName = 'Ahmed',
                      LName = 'Raaf0at',
                      Number = '+000+61200002',
                      Email = '12s3@aa.net',
                      Password = 'pa-A**-6',
                      ConfirmPassword = 'pa-A**-6',
                      f_name = f_name).signup()
            
            self.f.write('function '+f_name +' Success\n')
        except AssertionError:
            text = get_tb(sys.exc_info()[2])                
            self.f.write('function '+f_name+' failed : '+ text.split(', [')[1][1:-84]+'\n')
                
    def test_email(self):
        f_name = inspect.currentframe().f_code.co_name 
        try: 
            PHPTravelregister(chrome_path = self.path,
                      FName = 'Ahmed',
                      LName = 'Raafat',
                      Number = '+00061200002',
                      Email = '12s3@.net',
                      Password = 'pa-A**-6',
                      ConfirmPassword = 'pa-A**-6',
                      f_name = f_name).signup()
            
            self.f.write('function '+f_name+' Success\n')
        except AssertionError: 
            text = get_tb(sys.exc_info()[2])
            self.f.write('function '+f_name +' failed : '+ text.split(', [')[1][1:-84]+'\n')
                
    def test_password(self):
        f_name = inspect.currentframe().f_code.co_name 
        try: 
            PHPTravelregister(chrome_path = self.path,
                      FName = 'Ahmed',
                      LName = 'Raafat',
                      Number = '+00061200002',
                      Email = '12s3@aa.net',
                      Password = 'pa-**-6',
                      ConfirmPassword = 'pa-A**-6',
                      f_name = f_name).signup()
            
            self.f.write('function '+f_name+' Success\n')
        except AssertionError: 
            text = get_tb(sys.exc_info()[2])
            self.f.write('function '+f_name+' failed : '+ text.split(', [')[1][1:-84]+'\n')
                
    def test_signup(self):
        f_name = inspect.currentframe().f_code.co_name 
        try: 
            PHPTravelregister(chrome_path = self.path,
                      FName = 'Ahmed',
                      LName = 'Raafat',
                      Number = '+00061200002',
                      Email = '12s3@aa.net',
                      Password = 'pa-A**-6',
                      ConfirmPassword = 'pa-A**-6',
                      f_name = f_name).signup()
            
            self.f.write('function '+f_name+' Success\n')
        except AssertionError: 
            text = get_tb(sys.exc_info()[2])
            self.f.write('function '+f_name +' failed : '+ text.split(', [')[1][1:-84]+'\n')
                
    def test_valid(self):
        f_name = inspect.currentframe().f_code.co_name 
        try: 
            PHPTravelregister(chrome_path = self.path,
                      FName = 'Ahmed',
                      LName = 'Raafat',
                      Number = '+00061200002',
                      Email = '12s3@aa.net',
                      Password = 'pa-A**-6',
                      ConfirmPassword = 'pa-A**-6',
                      f_name = f_name).signup()
            
            self.f.write('function '+f_name+' Success\n')
        except AssertionError: 
            text = get_tb(sys.exc_info()[2])
            self.f.write('function '+f_name+' failed : '+ text.split(', [')[1][1:-84]+'\n')
                
    
    def tearDown(self):
        self.f.close()
        pass

if __name__ == "__main__":
    unittest.main()