import threading
import time
import random
from threading import Thread,Lock,enumerate as list_threads
from psutil import Process
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# BeautifulSoup
from bs4 import BeautifulSoup
import os
import datetime
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from socket import error as socket_error
#/*
from PIL import Image
from io import BytesIO
#import bot_s
# from pyvirtualdisplay import Display
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

######################
# def info_url():
#     mdm="static/txt/info_url.txt"
#     contacts = os.path.join(PROJECT_ROOT, mdm)
#     fileread=open("{}".format(contacts), "r")

#     if fileread.mode == 'r':
#         all_lines = fileread.read()
        
#         return all_lines.split("\n")[0],all_lines.split("\n")[1],all_lines.split("\n")[2]
# pro1, domain,pro11=info_url()
#pro = "/tmp/.org.chromium.Chromium.7R9v37/Default"
#domain = "askqais.com"

######################
        

def twireadonoff():
    data = "static/twi2.log"
    chat_f = os.path.join(PROJECT_ROOT, data)
    file = open(chat_f,"r").read()
    return file

#---------------------------------


def twilog(ms):
    data = "static/twi2.log"
    qr = os.path.join(PROJECT_ROOT, data)
    file = open(qr,"w+")
    file.write(str(ms))
    file.close()


def wrs(ms):
    data = "static/txt/qr2.txt"
    qr = os.path.join(PROJECT_ROOT, data)
    file = open(qr,"w+")
    file.write(str(ms))
    file.close()
im_f = ""

pack_im = []
# dsl = Display(visible=1, size=(1000, 800))
class brow():
    """docstring for brow"""
    def __init__(self):
        ###################################################################################
        # settings chrome
        ###################################################################################
        # if not dsl.is_alive():
        #     self.display = dsl
        #     self.display.start()
        
        self.options = webdriver.ChromeOptions()
        self.options = Options() 
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
        self.options.add_experimental_option('useAutomationExtension', False) 
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        #self.options.add_argument("user-data-dir={}".format(pro11))
        self.options.add_argument('--disable-infobars')
        self.options.add_argument('disable-web-security')
        self.options.add_argument('disable-popup-blocking')
        self.options.add_argument('ignore-certificate-errors')
        self.options.add_argument('disable-geolocation')
        self.options.add_argument('disable-translate')
        self.options.add_argument("--no-sandbox")
        self.options.add_argument('--blink-settings=imagesEnabled=false')
        self.browsers=[]
        self.threads = []
        print('fodrow2')
        #wrs("scan or start")
        

    def br(self,i):
        self.driver = webdriver.Chrome(options=self.options, executable_path="/usr/bin/chromedriver")



        
        self.process=self.driver.service.process
        self.pid=self.process.pid
        self.cpids=[x.pid for x in Process(self.pid).children()]
        self.pids=[self.pid]+self.cpids
        self.browsers.extend(self.pids)
        #driver.set_page_load_timeout(10)
        #self.driver.set_window_size(800, 900) 
        self.driver.set_page_load_timeout(50)



        def check5():
            print("cheker starting...")
            try:
                element_x = self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[4]/div/div/div[2]/div[1]/h1')
                if element_x:
                    wrs("QR scanned successfully")
                    return True

            except:False

            try:
                valtwi = twireadonoff()
                if valtwi == "close":
                    wrs("Closed")
                    # try:
                    #     im_f = os.path.join(PROJECT_ROOT, 'static/im.png')
                    #     os.remove(im_f)
                    # except:pass
                    self.driver.close()
                    self.stop_threads = True
                    #self.display.stop()
                    return "close"
            except:pass


            print("start saving qr...")
            try:
                element = self.driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div[1]/div/div[2]/div/canvas') # find part of the page you want image of
                location = element.location
                size = element.size
                
                png = self.driver.get_screenshot_as_png() # saves screenshot of entire page
                

                im = Image.open(BytesIO(png)) # uses PIL library to open image in memory

                left = location['x']
                top = location['y']
                right = location['x'] + size['width']
                bottom = location['y'] + size['height']


                im = im.crop((left, top, right, bottom)) # defines crop points
                im_f = os.path.join(PROJECT_ROOT, 'static/im2.png')
                im.save(im_f) # saves new cropped image
                print("successfully saved")

                ramn = "0000"
                wrs("Waiting Scan...")
                time.sleep(3)
                return "save"
            except Exception as e:
                return e
            return False




        a = 0
        ask = True
        try:
            self.driver.get("https://web.whatsapp.com/")
            #self.wait = WebDriverWait(self.driver, 30)
            

            self.wait = WebDriverWait(self.driver, 50)
            wrs("Web opened")
            def ch_twi():
                valtwi = twireadonoff()
                if valtwi == "close":
                    #print(valtwi)
                    wrs("bot Closed")
                    
                return valtwi
            while ask:
                print("Bot Starting...")
                time.sleep(1)
                if ch_twi() == "close":
                    break
                if ch_twi() == "start":
                    print("Checking...")
                    try:
                        def con():
                            try:
                                connecting_txt = self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[3]').text
                                if connecting_txt == "Connecting…":
                                    wrs("Connecting…")
                                    return True
                            except:
                                return False
                        #print(connecting_txt)
                        if con():
                            print("Connecting…")
                            while con():
                                valtwi = twireadonoff()
                                if valtwi == "close":
                                    print(valtwi)

                                    wrs("bot Closed")
                                    break
                                print("Waiting connextion...")
                                time.sleep(1)
                                cnx = con()

                                if not cnx:
                                    wrs("Please wait...")
                                    print("Please wait...")
                        try:
                            l= self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div/div[2]/div/canvas")
                            self.driver.execute_script("arguments[0].scrollIntoView(true);", l)
                            print("qr exist")
                            cheker_ = check5()
                            print(cheker_)
                            if cheker_ == "close":
                                break
                            if cheker_:
                                print(cheker_)
                                #return self.driver
                            
                        except:
                            pass
                        try:
                            element= self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[4]/div/div/div[2]/div[1]/h1')
                            if element:

                                print(".")
                                wrs("Please wait...")
                                try:
                                    element= self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[4]/div/div/div[2]/div[1]/h1')
                                    if element:

                                        print("Bot Loged Successfully")
                                        wrs("Loged Successfully")
                                        ask = False
                                        # try:
                                        #     im_f = os.path.join(PROJECT_ROOT, 'static/im.png')
                                        #     os.remove(im_f)
                                        # except:pass

                                        return self.driver
                                except:
                                    #self.driver.close()
                                    print("no loging!")
                                #self.driver.get("https://www.binance.com")
                            
                            print('success')
                        except:
                            wrs("Waiting loging..")


                    except Exception as r:
                        print(str(r)+"connecting error")



                time.sleep(3)

        except Exception as r:
            print(r)
