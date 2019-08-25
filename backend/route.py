from flask import render_template,Flask, redirect, url_for, request,jsonify,session
from backend import Grammar
from backend.Database import Database

from backend import Translate

import json


app = Flask(__name__)
app.config['SECRET_KEY']='40PdS98eZy2mz5hqGIXIOg'

@app.route("/tt")
def fortest ():
    return render_template('public/fortest.html')

# public route
@app.route("/")
def Hompage ():
    if "USERNAME" in session and "USER_ID" in session:
        userName = session["USERNAME"]
        userid = session["USER_ID"]
        Privilege_user = session["Privilege_user"]
        send = [userName, userid, Privilege_user]
        return render_template('public/index.html', send=send)
    else:
        return render_template('public/index.html')

@app.route('/about')
def about():
    if "USERNAME" in session and "USER_ID" in session:
        userName = session["USERNAME"]
        userid = session["USER_ID"]
        Privilege_user = session["Privilege_user"]
        send = [userName, userid, Privilege_user]
        return render_template('public/about.html', send = send)
    return render_template('public/about.html')

@app.route('/test')
def tst():
    if "USERNAME" in session and "USER_ID" in session:
        userName = session["USERNAME"]
        userid = session["USER_ID"]
        Privilege_user = session["Privilege_user"]
        send = [userName, userid, Privilege_user]
        return render_template('public/test.html', send = send)
    return redirect(url_for("Hompage"))


@app.route('/help')
def help():
    if "USERNAME" in session and "USER_ID" in session:
        userName = session["USERNAME"]
        userid = session["USER_ID"]
        Privilege_user = session["Privilege_user"]
        send = [userName, userid, Privilege_user]
        return render_template('public/help.html',send = send)
    return render_template('public/help.html')

@app.route('/login')
def login():
    return render_template('public/login.html')

@app.route('/checkLogin',methods=['POST'])
def checkLogin():
    user = request.form['username']
    password = request.form['password']
    database = Database()
    get = database.login(user,password)
    if(get=="None"):
        return render_template('public/login.html')
    elif (get == "notNone"):
        return render_template('public/login.html')
    # for admin
    elif (get[0][1]==0):
        session["USERNAME"] = get[0][5] + " " + get[0][6]
        session["USER_ID"] = get[0][0]
        session["Privilege_user"] = get[0][1]

        userName = session["USERNAME"]
        userid = session["USER_ID"]
        Privilege_user = session["Privilege_user"]

        send = [userName, userid, Privilege_user]
        print("sesion :::" + str(send[0]) + "**" + str(send[1]))
        return render_template('admin/index.html',send = send,Privilege_user=0)
    # for user public
    elif (get[0][1] == 1):
        session["USERNAME"] = get[0][5] +" "+get[0][6]
        session["USER_ID"] = get[0][0]
        session["Privilege_user"] = get[0][1]

        userName = session["USERNAME"]
        userid = session["USER_ID"]
        Privilege_user = session["Privilege_user"]

        send = [userName, userid,Privilege_user]

        print("sesion :::"+str( send[0])+"**"+ str(send[1]))
        return render_template('public/index.html',send = send)
    else:
        return render_template('public/login.html')

@app.route('/getdata-user', methods=['POST'])
def getdatauser():
    if "USERNAME" in session and "USER_ID" in session:
        userName = session["USERNAME"]
        userid = session["USER_ID"]
        Privilege_user = session["Privilege_user"]
        send = [userName, userid,Privilege_user]
    else:
        send = ""
    return jsonify({'dataUser':send})

@app.route('/logout')
def logout():
    session.pop("USERNAME", None)
    session.pop("USER_ID", None)
    return redirect(url_for("Hompage"))

@app.route('/wellcome-to-recommend')
def wellcomeRecommend():
    if "USERNAME" in session and "USER_ID" in session:
        userName = session["USERNAME"]
        userid = session["USER_ID"]
        Privilege_user = session["Privilege_user"]
        send = [userName, userid, Privilege_user]
        return render_template('public/recommend.html', send=send)
    else:
        return redirect(url_for("Hompage"))


# for translate in weppage
@app.route("/transtate",methods=['POST'])
def transtate ():
    if(request.method=='POST'):
        text = request.form['sentence']
        check = str(text)
        check = check.strip()
        if(check!=""):
            a = Translate.Translate()
            aa = a.traslateThaiHmong_0(text)
            data = str(aa)
            data = data.split("|\\")
            # print(data)
        else:
            data = ""
    return jsonify({'sentence':data})

@app.route("/transtate2",methods=['POST'])
def transtate2 ():
    if(request.method=='POST'):
        text = request.form['sentence']
        check = str(text)
        check = check.strip()
        if(check!=""):
            data = Translate.Translate()
            data = data.traslateThaiHmong(text)
        else:
            data = ""
    return jsonify(data)

@app.route('/clickSearch',methods=['POST'])
def clickSearch():
    word = request.form['word']
    word = str(word)
    word = word.strip()
    print(word)

    if(word!=""):
        data = Database()
        result = data.clickSearch(word)
        # print(result)
        # print(word)
    else:
        result=""
    return jsonify({'getData':result})

# from run *****************************
@app.route('/Showsentence')
def Showsentence():
    # data = Database()
    # getRecommend# result_recommend = data.getRecommend()
    # result_newword = data.getNewword()
    # return render_template("public/Showsentence.html", result_recommend=result_recommend ,result_newword=result_newword)
    return render_template('public/Showsentence.html')

# send recommend
@app.route('/getRecommend',methods=['POST'])
def getRecommend():
    data = Database()
    result = data.getRecommend()
    return jsonify({'getData':result})


# send newword
@app.route('/getNewword',methods=['POST'])
def getNewword():
    data = Database()
    result = data.getNewword()
    return jsonify({'getData':result})

@app.route('/addword')
def addword():
    return render_template('public/addword.html')


# admin route
@app.route('/admin')
def adminpage():
    userName = session["USERNAME"]
    userid = session["USER_ID"]
    Privilege_user = session["Privilege_user"]
    send = [userName, userid, Privilege_user]

    if session["Privilege_user"]==0:
        return render_template('admin/index.html',send = send)
    else:
        return redirect(url_for("Hompage"))

@app.route('/searchword',methods=['POST'])
def searchword():
    word = request.form['word']
    word = str(word)
    word = word.strip()
    # print(word)
    if(word!=""):
        data = Database()
        result = data.searchWord(word)
        # print(result)
        # print(word)
    else:
        print("word null")
        result=""
    return jsonify({'getData':result})

@app.route('/addnewword',methods=['POST'])
def addNewWord():
    check = False
    if(request.method=='POST'):
       try:
            Thai_word = request.form['thaiword']
            Hmong_word = request.form['hmongword']
            Word_class = request.form['classword']
            Addmin_id = request.form['userID']

            dd = Database()
            dd.insertNewword_addmin(Thai_word, Hmong_word, Word_class,Addmin_id)
            check = True

       except Exception as e:
            print(e)
            print("error in insert funtion addnewword")
            return jsonify({'state': False})
    return jsonify({'state':check})

@app.route('/updateword',methods=['POST'])
def updateWord():
    check = False
    if(request.method=='POST'):
       try:
           id_word = request.form['idword']
           Thai_word = request.form['thaiword']
           Hmong_word = request.form['hmongword']
           Word_class = request.form['classword']
           Addmin_id = request.form['userID']



           db = Database()
           db.updateWord(id_word,Thai_word,Hmong_word,Word_class,Addmin_id)
           check = True

       except Exception as e:
            print(e)
            print("error in update funtion updateword")
            return jsonify({'state': False})
    return jsonify({'state':check})

@app.route('/deleteword',methods=['POST'])
def deleteWord():
    check = False
    if(request.method=='POST'):
       try:
            id_word = request.form['idword']
            thaiword = request.form['thaiword']
            userID = request.form['userID']
            print(id_word)
            print(thaiword)
            print(userID)

            dd = Database()
            dd.deleteWord(userID,id_word,thaiword)
            check = True
       except Exception as e:
            print(e)
            print("error in delete funtion deleteword")
            return jsonify({'state': False})
    return jsonify({'state':check})


@app.route("/addnewWord-newword",methods=['POST'])
def addnewWord_newword ():
    if "USERNAME" in session and "USER_ID" in session:
        userID = request.form['userID']
        get = Database()
        data = get.getNewword_toAdd(userID)
        return jsonify(data)
    return redirect(url_for("Hompage"))

@app.route("/checkWord-Recommend",methods=['POST'])
def checkWord_Recommend ():
    if "USERNAME" in session and "USER_ID" in session:
        userID = request.form['userID']
        get = Database()
        data = get.getRecommend_toCheck(userID)
        return jsonify(data)
    return redirect(url_for("Hompage"))

if __name__ == "__main__" :
    app.run(debug=True)