from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import time
from .constants import *
from .browser import Chrome
from .custom_typer import CustomTyper

class TestTyping():
    def __init__(self, speed=0.097): 
        """The lower the value for 'speed', the faster the bot will run. """
        self.chrome=Chrome()
        self.speed=speed
        self.finished="Failed/Finished typing"
        self.driver=self.chrome.driver
        self.typer=CustomTyper(chrome=self.chrome, speed=self.speed)

    def typing_com_typer(self,url=typing_com_url):
        '''Opens typing.com and performs a 3-minute typing test'''
        print('If the test doesn\'t work, try logging into the website and running it again')
        self.driver.get(url)
        try:
            while True:
                key=self.driver.find_element(By.CLASS_NAME, 'is-active').text
                self.typer.type(key)   
        except:
            print(self.finished)

    def ratatype_typer(self, url=ratatype_url):
        '''Opens ratatype.com and performs the typing test.'''
        self.driver.get(url)
        try:
            text=self.driver.find_element(By.ID, 'root').get_attribute('data-text-placeholder')
        except:
            print("Failed: couldn't find attribute.\n\n")
            raise
        self.typer.wait_for_website(15)
        self.typer.type(text)

    def livechat_com_typer(self,url=livechat_url):
        '''Opens livechat.com and perfroms a typing test'''
        self.driver.get(url)
        self.typer.trailing_space=True
        try:
            end_time=time() + 60
            while time() < end_time:
                text = self.driver.find_element(By.CLASS_NAME, 'u-pl-0').text
                self.typer.type(text)
        except:
            print(self.finished)
    
    def ten_fast_fingers_typer(self, url=ten_fast_fingers_url):
        '''You may have to open the first once before running the fuction to dismiss cookie prompt...'''
        self.driver.get(url)
        self.driver.find_element(By.ID, 'inputfield').click()
        self.typer.trailing_space=True

        try:
            end_time=time() + 60
            while time() < end_time:
                text = self.driver.find_element(By.CLASS_NAME, 'highlight').text
                self.typer.type(text)
        except:
            print(self.finished)
    
    def speedy_typing_online_typer(self, url=speedy_typing_online_url):
        '''Runs a typing test on speedytypingonline.com'''
        self.driver.get(url)
        container=self.driver.find_element(By.ID, 'blockDivContainer')
        try:
            end_time=time() + 62
            while time() < end_time:
                letter = container.find_element(By.CLASS_NAME, 'nxtLetter').text #This lookup may be expensive
                self.typer.type(letter)
        except:
            print(self.finished)
        
    def typing_speed_net_typer(self, url=typing_speed_net_url):
        '''Runs a typing test on typing-speed.net'''
        self.driver.get(url)
        container=self.driver.find_element(By.ID, 'text')
        self.driver.implicitly_wait(self.speed/2) #To reduce lookup time for whitespaces
        try:
            end_time=time() + 62
            while time() < end_time:
                try: #The method used here to find element may bottleneck the bot
                    letter = container.find_element(By.CLASS_NAME, 'letter_marked').text #This lookup may be expensive
                    self.typer.type(letter)
                except:
                    self.typer.type(" ")        
        except:
            print(self.finished)
        self.driver.implicitly_wait(15)

    def keyhero_typer(self, url=Keyhero_url):
        '''A bot which types on keyhero.com.'''
        print("This function may not terminate by itself... :)")
        self.driver.get(url)
        self.typer.type(Keys.ESCAPE)
        self.typer.select_text_field(By.CSS_SELECTOR, 'input[placeholder="Type the words here."]')
        container=self.driver.find_element(By.CLASS_NAME, 'quote')
        self.typer.trailing_space=True
        try:
            while True:
                text=container.find_element(By.CLASS_NAME, 'quote-current').text
                self.typer.type(text)
        except:
            print(self.finished)

    def w3schools_typer(self, url=w3s_url):
        self.driver.get(url)
        text=self.driver.find_element(By.ID, 'atext').text
        self.typer.type(text)

    def thetypingcat_com_typer(self, url=typingcat_url):
        self.driver.get(url)
        self.typer.letter_to_replace={'⏎': Keys.ENTER}
        screen=self.driver.find_element(By.CLASS_NAME, 'screen-display ')
        self.typer.wait_for_website()
        self.typer.type('⏎')
        end_time=time() + 62
        while time() < end_time:
            try:
                letter=screen.find_element(By.CLASS_NAME, 'Line__CharSpan-copnkx-0').get_attribute('data-char')
                self.typer.type(letter)
            except:
                print(self.finished)

    def custom_typing_bot(self, target_url:str='https://www.instructables.com/'):
        self.driver.get(target_url)
        print("\nCustom bot is not implemented...yet...feel free to implement it (╯°□°)╯︵ ┻━┻")
            






