#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymongo
import uuid
import datetime
from flask import jsonify
import os
import json
from pytz import timezone
import notitop
from dateutil.relativedelta import relativedelta


PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

def get_data_json():
    mdm="data.json"
    msg = os.path.join(PROJECT_ROOT, mdm)
    fileread=open("{}".format(msg), "r")

    if fileread.mode == 'r':
        all_lines = fileread.read()

        return json.loads(all_lines)


data_msgs = get_data_json()



mongo_uri = "mongodb+srv://arrayo:tradipassM@cluster0.mw9ptx3.mongodb.net/?retryWrites=true&w=majority" 
client = pymongo.MongoClient(mongo_uri)

mydb = client["user_login_system"]
mycol = mydb["users_table"]



def delet_user(_id):
    user = { "_id": _id }
    resp = mycol.delete_one(user)
    if resp:
        return "*User successfully deleted*"
    else:
        return "Unable to delete user"


def show_users():
    return [x["name"] for x in mycol.find()]

def show_all_users():
    return [x for x in mycol.find()]

def get_user_details(name):
    try:
        return [x for x in mycol.find() if x['name'] == name][0]
    except:return {'last':'','status':''}
#check status user
def check_status_user(name):
    try:
        return [x for x in mycol.find() if x['name'] == name][0]['status']
    except:
        return False
#print(check_status_user('nnn'))




now = datetime.datetime.now()

current_time = now.strftime("%Y-%m-%d %H:%M")





def add_user(name,last,days,default_time_ex=1):
    noti = notitop.sff()
    all_user = show_users()
    if name not in all_user:
        status = False
        user = {
            "_id": uuid.uuid4().hex,
            "name": name,
            "last":last,
            "days":days,
            "status":status,
            "message_details":{'title':'','image':'','text':''},
            "time_registration":current_time,
            "time_ex":noti.calc(current_time,default_time_ex)
        }
        mycol.insert_one(user)
        return True
    return False

def edit_message_d(name,s):
    myquery = { "name": name }
    status_E = { "$set": { "message_details": s } }
    mycol.update_one(myquery, status_E)

def push_message_d(name,s):
    myquery = { "name": name }
    status_E = { "$set": { "message_details": s } }
    mycol.update_one(myquery, status_E)

def edit_days(name,s):
    myquery = { "name": name }
    status_E = { "$set": { "days": s } }
    mycol.update_one(myquery, status_E)
def edit_status(name,s):
    myquery = { "name": name }
    status_E = { "$set": { "status": s } }
    mycol.update_one(myquery, status_E)


def edit_status_id(_id,s):
    myquery = { "_id": _id }
    status_E = { "$set": { "status": s } }
    if mycol.update_one(myquery, status_E):
        return True
    else:return False




def edit_last(name,s):
    myquery = { "name": name }
    status_E = { "$set": { "last": s } }
    mycol.update_one(myquery, status_E)

def delet_all_users():
    for x in mycol.find():
        mycol.delete_one(x)
    return True
#delet_all_users()

name = '+21255551'
last = 'hi'
days = '5'
#add_user(name,last,days)

def check_name_db(name):
    users = show_users()
    if name in users:
        return True
    else:
        return False


def ord(name,message,last='test',days=10):
    status = check_status_user(name)
    check_name = check_name_db(name)
    M1 = data_msgs['firs_msg'].replace('username',name)
    reply = [M1,data_msgs['sec_user']]
    user = True
    if status:
        #print('User registred')
        user_pr = get_user_details(name)
        if user_pr['status']:
            print('active')
        




        #save last msg

        #edit_last(name,reply[1])
        data_8 = get_user_detail__8(name)
        if status:
            print("good")
            print(data_8)
            if user_pr['last']=='title':
                print(f'this is a title {message}')
                edit_last(name,'image')
                reply = {'name':name,
                'output':[data_msgs['send_image']],
                'status':status}
                print('reply title passed')
                add_get_message_details(name,{user_pr['last']:message})
                return reply
            
            if user_pr['last']=='image':
                print(f'this is a title {message}')
                edit_last(name,'text')
                reply = {'name':name,
                'output':[data_msgs['send_text']],
                'status':status}
                print('reply image passed')
                add_get_message_details(name,{user_pr['last']:message})
                return reply

            if user_pr['last']=='text':
                print(f'this is a title {message}')
                
                reply = {'name':name,
                'output':[data_msgs['post_suc']],
                'status':status}
                print('reply text passed')
                add_get_message_details(name,{user_pr['last']:message})

                data_8 = get_user_detail__8(name)
                print("data_8",data_8)
                if data_8["title"]!="" and data_8["image"]!="" and data_8["text"]!="":
                    reply = {'name':name,
                    'output':[data_msgs['post_suc']],
                    'status':status}
                    #post
                    #post_now(data_8["image"],data_8["title"],data_8["text"])
                    #data:image/png;base64,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
                    edit_last(name,'')
                    t8 = ["title","image","text"]
                    for t1 in t8:
                        add_get_message_details(name,{t1:""})
                    return reply


                ########################################
                ########################################
                if data_8["title"]=="":
                    reply = {'name':name,
                    'output':[data_msgs['send_title']],
                    'status':status}
                    edit_last(name,'title')
                if data_8["image"]=="":
                    reply = {'name':name,
                    'output':[data_msgs['send_image']],
                    'status':status}
                    edit_last(name,'image')
                if data_8["text"]=="":
                    reply = {'name':name,
                    'output':[data_msgs['send_text']],
                    'status':status}
                    edit_last(name,'text')
                    return reply
                #edit_last(name,'')
                reply = "noooooo"
                return reply



            # if user_pr['last'] == 'title':
            #     print(f'this is a title {message}')
            #     edit_last(name,'image_text')
            #     reply = {'name':name,
            #     'output':[data_msgs['send_text_image']],
            #     'status':status}
            #     print('reply title passed')
            #     return reply


            # if user_pr['last'] == 'image_text':
            #     print(f'this is a image with text {message}')
            #     edit_last(name,'-')
            #     print('-------------')

            #     reply = {'name':name,
            #     'output':[data_msgs['post_suc']],
            #     'status':status}
            #     print('reply image_text passed')
            #     return reply
    else:
        user = False
    if user or not user:
        try:
            user_pr = get_user_details(name)
        except:
            user_pr = {'last':''}
        if message == 'a' or message == 'A':
            if 'Publicar Nota/Pauta?' in user_pr['last']:
                if status:
                    reply = {'name':name,
                    'output':[data_msgs['req_title']],
                    'status':status}
                    print('reply 11')
                    edit_last(name,'title')
                    return reply

                reply = {'name':name,
                'output':[data_msgs['need_act_1'],data_msgs['need_act_2'],data_msgs['need_act_3'],data_msgs['need_act_4']],
                'status':status}
                print('reply 22')
                edit_last(name,'needreg')
                return reply
        if message == 'b' or message == 'B':
            if 'Publicar Nota/Pauta?' in user_pr['last']:
                edit_last(name,'signup')
                reply = {'name':name,
                'output':['signup'],
                'status':status}
                return reply
        if message == 'c' or message == 'C':
            edit_last(name,'sign plan')
            reply = {'name':name,
            'output':['sign plan'],
            'status':status}
            return reply
        if message == 'd' or message == 'D':
            edit_last(name,'help')
            edit_last(name,'sign plan')
            reply = {'name':name,
            'output':['help'],
            'status':status}
    add_user(name,reply,days)
    try:
        edit_last(name,reply[1])
    except:
        reply = [M1,data_msgs['sec_user']]
        edit_last(name,reply[1])

    #edit_status(name,False)
    # edit_days(name,20)
    
    reply = {'name':name,
    'output':reply,
    'status':status}
    return reply



#ora = ord('w','a','vvv')
# print(ora)
#print(len(show_all_users()))
#edit_status('Hasona',False)
#edit_status('+212 770-856808',True)
#delet_all_users()
def add_get_message_details(name,val):
    user_table_msg = get_user_details(name)['message_details']
    #print(f'details :::{user_table_msg}')
    #push_message_d(name,val)
    
    details_ = {}
    for x in user_table_msg:
        if str(x) == str(list(val)[0]):
            user_table_msg[x] = val[x]
            push_message_d(name,user_table_msg)
            return user_table_msg

        #details_[list(x)[0]] = x[list(x)[0]]
    return False
#555555
#print(add_get_message_details('w',{'title':'fffjjj'}))

def get_user_detail__8(name):
    try:
        return [x['message_details'] for x in mycol.find() if x['name'] == name][0]
    except:return False

#test
#------------------------------
# alli = show_all_users()
# ur = alli[0]['message_details']


# print('this is title/text/image',ur['title'],ur['text'],len(ur['image']))
#------------------------------


# name_image = os.path.join(PROJECT_ROOT, f"images_S/a.png")
# image_data = open(name_image, "rb")



# encoded = base64.b64encode(ur).decode('ascii')
# res = 'data:image/png;base64,{}'.format(encoded)



#encoded = base64.b64encode(image_data)
#encoded = base64.b64encode()
#res = b'data:image/png;base64,' + encoded
# print(res)
def post_now(phone,image,title,text):
    #uncomment this line
    res = False#creat_post.creat_p(image,title,text)
    if res != False:
        db_s = ['title','text','image']
        for x in db_s:
            add_get_message_details(phone,{x:''})
        print('Post created')
        return True
    return False

# name = 'testc'
# title = 'API test'
# text = 'API API API API API API API API API API'
# post_now(name,title,text,ur)
# name = '+212 770-856808'
# aa = get_user_detail__8(name)
# print(aa['title'])

#edit_status('+212 770-856808',True)
#delet_all_users()

#print(show_all_users())


def get_timezone_now(val="Europe/Lisbon"):

    try:
        # get the current UTC time
        time_UTC = datetime.datetime.now(datetime.timezone.utc)
        t = timezone(val)
        print(t)
        t_nk = time_UTC.astimezone(t)
        return datetime.datetime(t_nk.year, t_nk.month ,t_nk.day ,t_nk.hour , t_nk.minute)
    except Exception as e:
        print("error: get_timezone_now")
        print(e)
        return False
def add_m_y(m_y,use_date = get_timezone_now()):
    try:
        m_y = str(m_y)
        
        if "_" not in m_y:
            m_y = m_y.replace(" ","_")
        
        if m_y.split("_")[1] == "m":
            m_yx = int(m_y.split("_")[0])
            print('here::')
            print("use_date",use_date)
            
            use_date = use_date+relativedelta(months=+m_yx)
            print("use_date",use_date.strftime('%Y-%m-%d %H:%M'))
        if m_y.split("_")[1] == "y":
            m_yx = int(m_y.split("_")[0])
            use_date = use_date+relativedelta(years=+m_yx)
        if m_y.split("_")[1] == "w":
            m_yx = int(m_y.split("_")[0])
            use_date = use_date+relativedelta(weeks=+m_yx)
        if m_y.split("_")[1] == "d":
            
            m_yx = int(m_y.split("_")[0])
            
            use_date = use_date+relativedelta(days=+m_yx)
            print("use_date",use_date.strftime('%Y-%m-%d %H:%M'))
            

        return use_date.strftime('%Y-%m-%d %H:%M')
    except Exception as dd:
        print(dd)
        return False
#print(add_m_y("8_d"))


def change_pack(_id,s):
    try:
        myquery = { "_id": _id }
        upgrade = { "$set": { "time_ex": s } }
        mycol.update_one(myquery, upgrade)
        return str(s)+" successfully upgraded"
    except:
        return str(s)+" Failed!"