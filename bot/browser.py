#Contains the Chrome class used to start the web-browser


from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from .constants import path_to_chrome,cant_find_chrome_error
from os import chdir,getcwd
from subprocess import Popen



class Chrome():  
    '''Use this class start an instance of 'chrome.exe' and connect to it.'''
    def __init__(self): 
        """The lower the value for 'speed', the faster the bot will run. """
        self.start_chrome()
        options=Options()
        options.add_experimental_option("debuggerAddress", "localhost:9014")
        self.driver=webdriver.Chrome(options=options)
        self.driver.implicitly_wait(15)
        self.actions=ActionChains(self.driver)

    def start_chrome(self, path=path_to_chrome): ##WORKS
            chdir(path)
            try:
                Popen(["chrome.exe", "-remote-debugging-port=9014"]) 
            except:
                print(cant_find_chrome_error)
                print(getcwd())
                self.start_chrome(input("Input path to chrome.exe:"))