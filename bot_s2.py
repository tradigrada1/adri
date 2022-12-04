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
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
# check langague
import re
import json

#////////
import base64
import threading,random
#import ts_m

#import uuid

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))


def get_data_json():
    mdm="data.json"
    msg = os.path.join(PROJECT_ROOT, mdm)
    fileread=open("{}".format(msg), "r")

    if fileread.mode == 'r':
        all_lines = fileread.read()

        return json.loads(all_lines)


data_msgs = get_data_json()

def wr_blink():
    data = "blink2.txt"
    chat_f = os.path.join(PROJECT_ROOT, data)
    file = open(chat_f,"w+")
    file.write(str(random.randint(1254,521145)))
    file.close()

######################


#pro = "/tmp/.org.chromium.Chromium.7R9v37/Default"
#domain = "askqais.com"

######################

###################################################################################
# settings chrome
###################################################################################
options = webdriver.ChromeOptions()
options = Options() 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
options.add_experimental_option('useAutomationExtension', False) 
options.add_argument("--disable-blink-features=AutomationControlled")
#options.add_argument("user-data-dir={}".format(pro))
options.add_argument('--disable-infobars')
options.add_argument('disable-web-security')
options.add_argument('disable-popup-blocking')
options.add_argument('ignore-certificate-errors')
options.add_argument('disable-geolocation')
options.add_argument('disable-translate')
options.add_argument("--no-sandbox")
#options.add_argument('--blink-settings=imagesEnabled=false')

#-----------------------------------
# "```"+str(mess)+"```"
#***********************************




############################################################################


############################################################################
# input user -------------------------*
def print_last_msg(NAME, list_of_chatters):
    message = []
    for l in list_of_chatters:

        name = l.find('span', {'class':"emojitext ellipsify"}).get("title")
        if name == NAME:
            times = l.findAll("span", {"class":"chat-time"})
            msgs = l.findAll("span", {'class':"emojitext ellipsify"})
            tlist = ['\n' + t.getString() for t in times]
            mlist = [msg.getString() for msg in msgs]
            mlist.remove(name)

            from_me = l.findAll("span", {"class":"icon icon-status-dblcheck"}) + l.findAll("span", {"class":"icon icon-status-check"})
            if len(from_me) > 0:
                mlist.insert(0, u'Me')
            else:
                mlist.insert(0, name)

            message = message + tlist + mlist
    return message
#-------------------------------------*
from PIL import Image
from io import BytesIO


class webdriverW():
    def __init__(self, parent) :
        self.parent = parent

    def __getattr__(self, attr):
        return getattr(self.parent, attr)

    def getattB(self):
        return self.parent.br(random.randint(1254,521145))
    def setup_method(self,driver):
        print("Server start...")
        self.driver = driver #webdriver.Chrome(options=options, executable_path="/usr/bin/chromedriver")
        self.vars = {}
        
    # Function to convert the date format
    def convert24(self, str1):
        
        # Checking if last two elements of time
        # is AM and first two elements are 12
        if str1[-2:] == "AM" and str1[:2] == "12" or str1[-2:] == "am" and str1[:2] == "12" or str1[-2:] == "Am" and str1[:2] == "12":
            return "00" + str1[2:-2]
            
        # remove the AM 
        elif str1[-2:] == "AM" or str1[-2:] == "am" or str1[-2:] == "Am":
            return str1[:-3]
        
        # Checking if last two elements of time
        # is PM and first two elements are 12
        elif str1[-2:] == "PM" and str1[:2] == "12" or str1[-2:] == "pm" and str1[:2] == "12" or str1[-2:] == "Pm" and str1[:2] == "12":
            return str1[:-2]
        else:
            # add 12 to hours and remove PM
            return str(int(str1[:2]) + 12) + str1[2:5]

    def ddtimezone_get(self):
        return caller_dsh2.read_add_timezoneM()


    def rmsg(self):
        mdm="msg/msg.json"
        msg = os.path.join(PROJECT_ROOT, mdm)
        fileread=open("{}".format(msg), "r")

        if fileread.mode == 'r':
            all_lines = fileread.read()

            return json.loads(all_lines)


    def contact_upgrade_live_agent(self):
        mdm="static/txt/contacts2.txt"
        contacts = os.path.join(PROJECT_ROOT, mdm)
        fileread=open("{}".format(contacts), "r")

        if fileread.mode == 'r':
            all_lines = fileread.read()
            
            return all_lines.split("\n")
    # Driver Code       
    #print(convert24("00:24 pm").replace(" ",""))
    def teardown_method(self):
        try:
            self.driver.close()
        except:pass
        try:
            pass
            #os.system("killall chromium-browser")
        except:pass
    def openweb(self,i):
        try:
            print("Server start listening...")
            a = True
            v = 0
            while a:                
                print("reload "+str(v))
                self.driver.get('https://web.whatsapp.com/')
                self.wait = WebDriverWait(self.driver, 40)
                #self.wait2 = WebDriverWait(self.driver, 10)

                    # wait until webpage loads successfully to prevent any exception

                # try:
                #     self.element2 = self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div/div[2]/div[1]/div/div[2]/div')))
                #     if self.element2:
                        
                #         print("yes")

                #         onoff("close")
                        
                #         return "close"
                # except:
                #     pass
                try:
                    self.element = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/header/div[1]/div')))
                    break
                    return self.driver
                except:print("element error")
                # stopbm = readonoff()
                # if stopbm == "close":
                #     self.stopb = False
                #     self.teardown_method()
                #     onoff("close")
                #     time.sleep(5)
                #     return "close"

                
                # if self.element:
                #     #print("noooo")
                #     break
                #     return self.driver
                # else:
                #     pass
                    #self.driver.close()
                v+=1
                #return "close"
                if v >= 4:
                    self.driver.close()
                    break
        except:
            v+=1
            return "close"

    def ch_lg(self, txt):
        texar = re.sub(r'[^ء-يﭐ-﷿ﹰ-ﻼ]',' ', txt)
        txa = [x for x in texar if x != " " ]
        txen = texar = re.sub(r'[^a-z]',' ', txt)
        txe = [x for x in txen if x != " " ]

        if len(txa) > len(txe):
            msg = "ar"
        else:
            msg = "en"
        return msg

    def cl_m_b(self):
        def click_size():
            WebDriverWait(self.driver,2).until(EC.element_to_be_clickable((By.XPATH,"//ul[@class='_1HnQz']//li[contains(.,'Close chat')]"))).click()

        
        main_cl = self.driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/div/span').click()
        click_size()
        #btn_cl = self.driver.find_element_by_xpath("//li/span[text()='Close chat']").click()

    def get_file_content_chrome(self, uri):
        result = self.driver.execute_async_script("""
            var uri = arguments[0];
            var callback = arguments[1];
            var toBase64 = function(buffer){for(var r,n=new Uint8Array(buffer),t=n.length,a=new Uint8Array(4*Math.ceil(t/3)),i=new Uint8Array(64),o=0,c=0;64>c;++c)i[c]="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".charCodeAt(c);for(c=0;t-t%3>c;c+=3,o+=4)r=n[c]<<16|n[c+1]<<8|n[c+2],a[o]=i[r>>18],a[o+1]=i[r>>12&63],a[o+2]=i[r>>6&63],a[o+3]=i[63&r];return t%3===1?(r=n[t-1],a[o]=i[r>>2],a[o+1]=i[r<<4&63],a[o+2]=61,a[o+3]=61):t%3===2&&(r=(n[t-2]<<8)+n[t-1],a[o]=i[r>>10],a[o+1]=i[r>>4&63],a[o+2]=i[r<<2&63],a[o+3]=61),new TextDecoder("ascii").decode(a)};
            var xhr = new XMLHttpRequest();
            xhr.responseType = 'arraybuffer';
            xhr.onload = function(){ callback(toBase64(xhr.response)) };
            xhr.onerror = function(){ callback(xhr.status) };
            xhr.open('GET', uri);
            xhr.send();
            """, uri)
        if type(result) == int :
            raise Exception("Request failed with status %s" % result)
        return base64.b64decode(result)


    def open_conversation(self, phone,message):

        o = True
        #try:
        while o:
            try:

                #click on search field
                search_field = self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
                search_field.click()
                time.sleep(0.3)
            except:
                continue





            #go down to contact list
            #search_field.send_keys(Keys.ARROW_DOWN)
            search_field.clear()
            searchv = self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
            #searchv.click()
            
            #a[:-1],a[-1]
            

            # sece = str(phone)[-1]
            
            #search_field.clear()
            self.driver.execute_script("arguments[0].innerHTML = '{}'".format(phone),searchv)
            search_field.send_keys(' ')
            #search_field.send_keys(Keys.ENTER)
            
            
            if search_field.send_keys(Keys.ENTER):
                pass
                #print('done')
            time.sleep(1)
            no = self.driver.find_elements_by_class_name('i0jNr')
            pn = []
            self.p = False
            if len(message) >=1:
                for n in no:
                    n = n.text
                    if n == phone:
                        #print(n)
                        print('good')
                        pn.append(n)
                        messages = self.last_m(phone)
                        
                        html = self.driver.page_source
                        soup = BeautifulSoup(html, 'lxml')
                        im = soup.find_all("img", src=lambda value: value and value.startswith("blob:https:"))
                        
                        #print(f'img ::{im}')
                        for image in im:
                            ms = image.get('alt')
                            if ms == messages[-1][0]:
                                #print(f'Message :{messages[-1]}')
                                try:
                                    ur= self.get_file_content_chrome(image.get('src'))
                                    print(ur)
                                    # Load image from BytesIO
                                    im = Image.open(BytesIO(ur))
                                    print('Image downloaded')
                                    #ts_m.edit_last(phone,'image_text')

                                    return {"text":message,'image':ur}
                                    #return {"text":message,'image':ur}
                                    # # Display image and save image
                                    # im.show()
                                    #999999
                                    
                                except Exception as r:
                                    print(f'without image : {r}')
                        # ran = random.randint(1,987)
                        # s=threading.Thread(target=self.add_to_table_c, args=(phone,messages))
                        # s.start()
                        return {"message":message,'image':"0"}
            else:
                return {"message":message,'image':"0"}

            if no[-1].text.startswith('No chats,'):
                #print(f'no : {no.text}')
                return None
                





    def add_to_table_c(self,phone,messages):
        pack = caller_dsh2.table_msgs_control_2(phone)
        print(f'this is pack {pack}')
        days_left = caller_dsh2.count_ex_user_help(phone)
        
        
        if db_start2.check_user(phone):
            #caller_dsh2.Message_m_m(phone,messages)
            for ms in messages:
                print(ms)
                if [ms] not in pack:

                    caller_dsh2.add_table_control("live",str(""),phone,"org_upgrade_","",ms,days_left,"Unserved")



    def last_m(self,phone):
        GLOBAL_MSG = []
        
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        list_of_chatters = soup.findAll('div', {'class':"message-in"})
        
        GLOBAL_MSG = []
        for d in list_of_chatters:
            ss = d.findAll('span')
            MS = []
            for s in ss:
                if s.text != '':
                    if s.text not in MS:
                        MS.append(s.text)
            GLOBAL_MSG.append(MS)
        return GLOBAL_MSG


    def chat_co(self,phone,messages):
        phone = chnum(phone)

        #print("chat_co   :: "+str(messages))
        data = "static/txt/chat2/{}.log".format(phone)
        chat_f = os.path.join(PROJECT_ROOT, data)
        if os.path.exists(chat_f):
            pass
        else:pass
        file = open(chat_f,"w+")
        file.write(str(messages.encode('ascii',errors='ignore')))
        file.close()




    #******************




    #******************


    def get_unread_messages(self):
        # Start get info from page
        #print("loading data messages")
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        #list_contact = soup.find(class_="_3Bc7H _20c87")

        pack_info_user = soup.select_one("div[aria-label*=Chat]")
        #print(pack_info_user)
        pack_info_user_o = pack_info_user.find_all("div", class_=lambda value: value and value.startswith("_"))
        
        data_unread_user = []
        for l in pack_info_user_o:
        #     phone = l.find(class_="_3vPI2").text
        #     message = l.find(class_="_37FrU").text
        #     data = l.find(class_="_1pJ9J")


            try:
                if l.find(class_="_3vPI2").span.text:
                    data = l.select_one("span[aria-label*=unread]").text
                    
                    phone_ = l.find(class_="_3vPI2").span.text
                    mess = l.find(class_="_37FrU").span.text
                    #img = soup.find('tbody').find_all('tr')
                    #print(img)
                    # print('passss')#blob:https:

                    # im = pack_info_user.find_all("img", src=lambda value: value and value.startswith("blob:https:"))
                    # print(im)
                    if (phone_, mess) not in data_unread_user: 
                        data_unread_user.append((phone_, mess))
                        
            except:
                continue


        #     print(data)
            #time_data = data[0]
            # check_message = data
            # if not check_message == "":
            #     if str(message) == "":
            #         message = "empty"
            #     else:
            #         data_unread_user.append((phone, message))
        return data_unread_user



    def send_message(self,phone, message):
        if isinstance(message,list):
            messages = message
            for message in messages:
                hd = self.open_conversation(phone,message)
                if hd == None:
                    return None
                if hd:
                    # Sender Message
                    text_element = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
                    #Click the send button

                    self.driver.execute_script("arguments[0].innerHTML = '{}'".format(message.replace('\n','<br>').replace("\r","")),text_element)
                    text_element.send_keys('.')
                    text_element.send_keys(Keys.BACKSPACE)
                    text_element.send_keys(Keys.ENTER)
                    #Click the send button
                    
                    #send_button = self.driver.find_element_by_xpath("//span[contains(@data-testid,'send')]")
                    #text_element.send_keys(Keys.ENTER)
                    # send_button = self.driver.find_element_by_css_selector('._4sWnG > span:nth-child(1)')
                    # send_button.click()
                    #caller_dsh2.update_lock(phone,False,message)
                    time.sleep(0.3)
            self.cl_m_b()
            
            return True

        else:
            hd = self.open_conversation(phone,message)
            if hd == None:
                return None
            if hd:
                # Sender Message
                text_element = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
                #Click the send button

                self.driver.execute_script("arguments[0].innerHTML = '{}'".format(message.replace('\n','<br>').replace("\r","")),text_element)
                text_element.send_keys('.')
                text_element.send_keys(Keys.BACKSPACE)
                text_element.send_keys(Keys.ENTER)
                #Click the send button
                
                #send_button = self.driver.find_element_by_xpath("//span[contains(@data-testid,'send')]")
                #text_element.send_keys(Keys.ENTER)
                # send_button = self.driver.find_element_by_css_selector('._4sWnG > span:nth-child(1)')
                # send_button.click()
                #caller_dsh2.update_lock(phone,False,message)
                time.sleep(0.3)
                self.cl_m_b()
                
                return True
        return False
                    
            
        

    def stopb(self):
        
        self.stopb = False
        self.teardown_method()
        print("stopb closed")
        

    def listen(self):
        stopb = readonoff()
        




        # try:
        #     alert = self.driver.switch_to.alert
        #     alert.accept()
        #     print("alert accepted")
        # except TimeoutException:
        #     print("no alert")
        print("listening...")
        while stopb == "start":
            # try:

            time.sleep(2)

            #self.open_conversation("Me")
            #input()
            wr_blink()
            try:
                unread_checker = self.get_unread_messages()
            except:
                unread_checker = ""
            
            #print("pass here 1")
            if len(unread_checker) > 0:
                for (phone, message) in unread_checker:

                    if message != "typing…":

                        op = self.open_conversation(phone,message)
                        if op:
                            if message == '':
                                message = 'emoj'
                            if ':' in message:
                                if len(message.split(':')[0])<=2 and len(message.split(':')[1]) == 2:
                                    message = 'Voice_REC'
                            #user_table_msg = ts_m.get_user_details(phone)['last']
                            #if user_table_msg == False:
                            # if user_table_msg == 'title':
                            #     print("this is title")
                            #     ts_m.add_get_message_details(phone,{user_table_msg:message})
                            # print(f'phone : {phone}\nMessage :{message}')
                            # Tmsg = ts_m.ord(phone,message)
                            #print(f'This is Image :{op}')
                            # try:
                            #     pass
                            #     ts_m.add_get_message_details(phone,{'text':op['text']})
                            #     #data_8 = ts_m.get_user_detail__8(phone)
                            #     #ts_m.post_now('phone',data_8['title'],data_8['text'],data_8['image'])
                            # except Exception as g:
                            #     pass
                            #     #print(f'error 1 {g}')
                            try:
                                # name = uuid.uuid4().hex
                                
                                # name_image = os.path.join(PROJECT_ROOT, f"images_S/{name}.png")
                                # ur = Image.open(BytesIO(op['image']))
                                # ur.save(name_image)
                                name_image = op['image']
                                encoded = base64.b64encode(name_image).decode('ascii')
                                name_image = 'data:image/png;base64,{}'.format(encoded)
                                #ts_m.add_get_message_details(phone,{'image':name_image})
                                #data_8 = ts_m.get_user_detail__8(phone)
                                print('image - '+name_image)
                                #ts_m.post_now(data_8['image'],data_8['title'],data_8['text'])
                                #print(data_8['title'],data_8['text'],data_8['image'])
                                #print(data_8['image'])
                                #print(message)
                        
                                
                            except Exception as g:
                                pass
                                #print(f'error 2 {g}')
                                #print('not text and image')
                            
                            ##self.send_message(phone,Tmsg['output'])
                            self.cl_m_b()
                            morph = self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/div/span/button')
                            morph.click()

                            
                        print('message - '+message)
##############################################################################
##############################################################################


# code here
def sbot(fromw):
    # pack data help stock
    data_pack_empty = {}
    reminders_alarm = []
    try:
        print("start b")
        # try:
        #     os.system("killall chromium-browser")            
        # except:pass
        # try:
        #     os.system("sudo service apache2 restart")
        # except:pass
        # display = Display(visible=1, size=(800, 600))
        # display.start()

        run = webdriverW()
        onoff("start")
        run.setup_method()
        driver = run.openweb("2")
        
        if driver == "close":

            run.teardown_method()
            #display.stop()
            onoff("close")
        else:
            run.listen()
        #display.stop()
    except KeyboardInterrupt:
        run.teardown_method()
        
        print("quitting: KeyboardInterrupt")





def start_stopb():
    global stopb
    stopb = True
    

def t_stopb():
    global stopb
    stopb = False





def onoff(val):

    data = "static/onof2.log"
    chat_f = os.path.join(PROJECT_ROOT, data)
    file = open(chat_f,"w+")
    file.write(str(val))
    file.close()
def readonoff():
    data = "static/onof2.log"
    chat_f = os.path.join(PROJECT_ROOT, data)
    file = open(chat_f,"r").read()
    return file

#onoff("start")

#sbot("test")



# lang = "en"
# phone = "+212 770-856808"
# message = "1:10 pm"
# timezone_ = "Europe/Lisbon"
# p, reply,up_live,lang = ts2.ch_bot(lang,phone,message,timezone_)
# print(reply)








