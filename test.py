import ts_m

phone = "212620460419"
#aa = ts_m.add_get_message_details(phone,{'text':'hi'})
a=ts_m.show_all_users()


user_pr = ts_m.ord(phone,'a')

print(user_pr)

@app.route('/d')
def d():
    phone = "212620460419"
    #aa = ts_m.add_get_message_details(phone,{'text':'hi'})
    a=ts_m.show_all_users()


    user_pr = ts_m.ord(phone,'a')

    print(user_pr)
    return user_pr




          phone = request.form['phone']
          msg = request.form['msg']
          #return tok
          user_pr = ts_m.ord(phone,msg)

          print(user_pr)
          return user_pr