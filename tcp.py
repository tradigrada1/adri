import ts_m
#ts_m.edit_last(phone,'image_text')
#return {"text":message,'image':ur}
#return {"message":message,'image':"0"}

phone = "222222"
message = "accaaa"

def org1(phone,message):
    user_table_msg = ts_m.get_user_details(phone)['last']
    print("user_table_msg ",user_table_msg)
    Tmsg = ts_m.ord(phone,message)
    print("Tmsg",Tmsg)
    #print()

    #if user_table_msg == False:
    #if user_table_msg == 'title':
        #print("this is title")
        ##ts_m.add_get_message_details(phone,{user_table_msg:message})
    #encoded = "image2121121"
    #name_image = 'data:image/png;base64,{}'.format(encoded)
    ##ts_m.add_get_message_details(phone,{'image':"name_image"})
    #data_8 = ts_m.get_user_detail__8(phone)
    #print("this is data8:\n ",data_8)
org1(phone,message)