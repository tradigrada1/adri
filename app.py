from flask import Flask, render_template, request, redirect, url_for, flash, session, Response
from functools import wraps

import threading
import datetime
import os
from time import sleep
from flask import jsonify
import json
import random
import time
#----------------
#----------------
import threading


# fn.dispstart()
#----------------/
#from pyvirtualdisplay import Display
#----------------/
import bot_s2
import fodrow2

#dsl = Display(visible=1, size=(1000, 800)).start()

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))


########################
######################
# def info_url():
#     mdm="static/txt/info_url.txt"
#     contacts = os.path.join(PROJECT_ROOT, mdm)
#     fileread=open("{}".format(contacts), "r")

#     if fileread.mode == 'r':
#         all_lines = fileread.read()
        
#         return all_lines.split("\n")[0],all_lines.split("\n")[1],all_lines.split("\n")[2]
# pro, domain,pro1=info_url()
# local_8 = "www."+str(domain)


def run_82(i):
    print('bot Starting...')
    insta = fodrow2.brow()
    driver1 = bot_s2.webdriverW(insta)
    driver = driver1.getattB()
    if driver != None and driver != False:
        driver1.listen()
        

#*******************************
def al():
    m=threading.Thread(target=run_82, args=(1,))
    m.start()



app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'


al()
ip_address = '0.0.0.0'
port = '5000'
if __name__ == "__main__":
    #app.run(debug=True)
    # app.run(host=ip_address, port=port, debug=True)
    # t = threading.Thread(target=bot_w.start_bt)
    # t.start()
    #app.run(host=ip_address, port=port)
    #al()
    app.run(host=ip_address, port=port)#, debug=True)
    # t.join()