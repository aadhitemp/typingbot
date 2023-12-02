#The custom_typer class can be used to create custom typing bots.
from time import sleep
from random import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from .browser import Chrome


class CustomTyper():
    def __init__(self, chrome:Chrome, speed=0.09, trailing_space=False, letter_to_replace:dict=None, find_text_field_by:By=None,  text_field_value:str=None):
        ''''speed': Use this increase or decrease the typing speed(inverse relationship)\n
            'trailing_space': Presses the space key everytime the typer() method finishes\n
            'letter_to_replace': A dictionary which can be used to replace characters'''
        self.driver=chrome.driver
        self.actions=chrome.actions
        self.speed=speed
        self.find_text_field_by=find_text_field_by
        self.text_field_value=text_field_value
        self.letter_to_replace=letter_to_replace
        self.trailing_space=trailing_space

    def select_text_field(self, by:By, value:str):
         text_box=self.driver.find_element(by, value)
         text_box.click()

    def wait_for_website(self, time:float=(random()*15)):
         sleep(time)
       
    def type(self, text:str):
            for letter in text:
                sleep(random()*self.speed)
                if self.letter_to_replace:
                    if letter in self.letter_to_replace: 
                        self.actions.send_keys(self.letter_to_replace[letter]).perform()
                        continue
                if letter.isupper():
                    self.actions.key_down(Keys.SHIFT).send_keys(letter.lower()).key_up(Keys.LEFT_SHIFT).perform()
                else:
                    if letter==" ":
                        self.actions.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                    else:
                        self.actions.send_keys(letter).perform()
            if self.trailing_space:
                 self.actions.send_keys(Keys.SPACE).perform()


         
        
