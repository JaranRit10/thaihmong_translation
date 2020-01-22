from flask import render_template, Flask, redirect, url_for, request,jsonify,session
from Database import Database
from Translate import Translate
import base64
from io import BytesIO
from PIL import Image


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
        for image_names in os.listdir('static/img/user_/'):
            user_image = str(userid) + ".png"
            if image_names == user_image:
                user_image = "user_/" + user_image
                break
            else:
                user_image = "default_user.png"
        send = [userName, userid, Privilege_user, user_image]
        return render_template('public/index.html', send=send)
    else:
        return render_template('public/index.html')


@app.route('/about')
def about():
    if "USERNAME" in session and "USER_ID" in session:
        userName = session["USERNAME"]
        userid = session["USER_ID"]
        Privilege_user = session["Privilege_user"]
        for image_names in os.listdir('static/img/user_/'):
            user_image = str(userid) + ".png"
            if image_names == user_image:
                user_image = "user_/" + user_image
                break
            else:
                user_image = "default_user.png"
        send = [userName, userid, Privilege_user, user_image]
        return render_template('public/about.html', send = send)
    return render_template('public/about.html')

@app.route('/recommend')
def recommend():
    if "USERNAME" in session and "USER_ID" in session:
        userName = session["USERNAME"]
        userid = session["USER_ID"]
        Privilege_user = session["Privilege_user"]
        for image_names in os.listdir('static/img/user_/'):
            user_image = str(userid) + ".png"
            if image_names == user_image:
                user_image = "user_/" + user_image
                break
            else:
                user_image = "default_user.png"
        send = [userName, userid, Privilege_user, user_image]
        return render_template('public/test.html', send = send)
    return redirect(url_for("Hompage"))


@app.route('/help')
def help():
    if "USERNAME" in session and "USER_ID" in session:
        userName = session["USERNAME"]
        userid = session["USER_ID"]
        Privilege_user = session["Privilege_user"]
        for image_names in os.listdir('static/img/user_/'):
            user_image = str(userid) + ".png"
            if image_names == user_image:
                user_image = "user_/" + user_image
                break
            else:
                user_image = "default_user.png"
        send = [userName, userid, Privilege_user, user_image]
        return render_template('public/help.html',send = send)
    return render_template('public/help.html')

# @app.route('/login')
# def login():
#     return render_template('public/login.html')

@app.route('/checkLogin',methods=['POST'])
def checkLogin():
    user = request.form['username']
    password = request.form['password']
    print(user,password)
    database = Database()
    get = database.login(user,password)
    print(get)
    if(get=="None"):
        return render_template('public/login.html')
    elif (get == "notNone"):
        return render_template('public/login.html')
    # for admin
    elif (get[0][1]==0):
        session["USERNAME"] = [get[0][5] , get[0][6]]
        session["USER_ID"] = get[0][0]
        session["Privilege_user"] = get[0][1]

        userName = session["USERNAME"]
        userid = session["USER_ID"]
        Privilege_user = session["Privilege_user"]

        for image_names in os.listdir('static/img/user_/'):
            user_image = str(userid) + ".png"
            if image_names == user_image:
                user_image = "user_/" + user_image
                break
            else:
                user_image = "default_user.png"
        send = [userName, userid, Privilege_user, user_image]
        print("sesion : " + str(send[0]) + " : " + str(send[1]))
        return render_template('admin/index.html',send = send,Privilege_user=0)
    # for user public
    elif (get[0][1] == 1):
        session["USERNAME"] = [get[0][5], get[0][6]]
        session["USER_ID"] = get[0][0]
        session["Privilege_user"] = get[0][1]

        userName = session["USERNAME"]
        userid = session["USER_ID"]
        Privilege_user = session["Privilege_user"]
        for image_names in os.listdir('static/img/user_/'):
            user_image = str(userid) + ".png"
            if image_names == user_image:
                user_image = "user_/" + user_image
                break
            else:
                user_image = "default_user.png"
        send = [userName, userid, Privilege_user, user_image]
        # print("sesion :::"+str( send[0])+"**"+ str(send[1]))
        return render_template('public/index.html',send = send)
    else:
        return redirect(url_for("Hompage"))

@app.route('/getdata-user', methods=['POST'])
def getdatauser():
    if "USERNAME" in session and "USER_ID" in session:
        userName = session["USERNAME"]
        userid = session["USER_ID"]
        Privilege_user = session["Privilege_user"]
        for image_names in os.listdir('static/img/user_/'):
            user_image = str(userid) + ".png"
            if image_names == user_image:
                user_image = "user_/" + user_image
                break
            else:
                user_image = "default_user.png"
        send = [userName, userid, Privilege_user, user_image]
    else:
        send = ""
    return jsonify({'dataUser':send})


@app.route('/checksignup', methods=['POST'])
def chekcsignup():
    username = request.form['name_signUp']
    username = str(username).strip()
    db = Database()
    if (db.checkUsername_signUp(username)):
        return "0"
    else:
        return "1"

@app.route('/signup', methods=['POST'])
def signup():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    username = request.form['username']
    password = request.form['pass']
    db = Database()
    check = db.addNewUser(username,password,fname,lname,email)
    if(check):
        return "1"
    else:
        return "0"


@app.route('/logout')
def logout():
    session.pop("USERNAME", None)
    session.pop("USER_ID", None)
    return redirect(url_for("Hompage"))

@app.route('/check_recommend')
def check_recommend():
    if "USERNAME" in session and "USER_ID" in session:
        userName = session["USERNAME"]
        userid = session["USER_ID"]
        Privilege_user = session["Privilege_user"]
        for image_names in os.listdir('static/img/user_/'):
            user_image = str(userid) + ".png"
            if image_names == user_image:
                user_image = "user_/" + user_image
                break
            else:
                user_image = "default_user.png"
        send = [userName, userid, Privilege_user, user_image]
        return render_template('public/recommend.html', send=send)
    else:
        return redirect(url_for("Hompage"))



@app.route("/check_newRecomment",methods=['POST'])
def increase_reliability():
    try:
        print("increase_Reliability")
        dataJson = request.form['sendJson']
        # userID = dataJson['userID']
        # id_recommend = dataJson['id_recommend']
        # state_reliability = dataJson['state_reliability']
        # print("data :",userID,id_recommend,state_reliability)
        # db = Database()
        # check = db.increase_Reliability(userID,id_recommend,state_reliability)
        return jsonify({'status': 200})
    except:
        pass

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
    # time.sleep(5)
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


# from run ***************************************************************************

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


@app.route('/profile_user')
def profile_user():
    if "USERNAME" in session and "USER_ID" in session:
        userName = session["USERNAME"]
        userid = session["USER_ID"]
        Privilege_user = session["Privilege_user"]
        for image_names in os.listdir('static/img/user_/'):
            user_image = str(userid) + ".png"
            if image_names == user_image:
                user_image = "user_/" + user_image
                break
            else:
                user_image = "default_user.png"
        send = [userName, userid, Privilege_user, user_image]
        return render_template('public/profile_user.html', send=send)
    else:
        return render_template('public/index.html')
# -------------- profile page ---------------------------------
import os
from uuid import uuid4

from flask import Flask, request, render_template, send_from_directory

__author__ = 'ibininja'

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/profile')
def profile():
    if "USERNAME" in session and "USER_ID" in session:
        userName = session["USERNAME"]
        userid = session["USER_ID"]
        Privilege_user = session["Privilege_user"]
        # print("username:",userName)
        for image_names in os.listdir('static/img/user_/'):
            user_image = str(userid) + ".png"
            print("name image p:", image_names)
            print("user_image p:", user_image)
            if image_names == user_image:
                user_image = "user_/" + user_image
                print("user_image p:",user_image)
                break
            else:
                user_image = "default_user.png"
                print("user_image p:", user_image)

        send = [userName, userid, Privilege_user, user_image]
        return render_template('public/profile.html', send=send)
    else:
        return render_template('public/index.html')

@app.route('/getprofile',methods=['POST'])
def getprofile():
    # id_user = request.form["id_user"]
    # print("id user = ",id_user)
    data = Database()
    result = data.getprofile()
    return jsonify({'getData':result})


@app.route('/crop',methods=['POST'])
def crop():
    try:
        image = request.form["image"]
        id_user = request.form["getUser_id"]
        print("id_user:", id_user)

        file = image
        starter = file.find(',')
        image_data = file[starter + 1:]
        image_data = bytes(image_data, encoding="ascii")
        im = Image.open(BytesIO(base64.b64decode(image_data)))
        # print("im:",im)
        image_path = "static/img/user_/"
        # print("image_path:", image_path)
        image_name = id_user + '.png'
        print("image_name:", image_name)

        im.save(image_path + image_name)
        path = image_path + image_name
        print("path:", path)


    except Exception as e:
        print(e)
        print("error in update funtion update Recommend")
    return jsonify({'getData': path})


# @app.route("/profile", methods=["POST"])
# def upload():
#     target = os.path.join(APP_ROOT, 'static/img/user_')
#     # target = os.path.join(APP_ROOT, 'static/')
#     print(target)
#     if not os.path.isdir(target):
#         os.mkdir(target)
#     else:
#         print("Couldn't create upload directory: {}".format(target))
#     print(request.files.getlist("file"))
#     # i = 1
#     for upload in request.files.getlist("file"):
#
#         print(upload)
#         print("{} is the file name".format(upload.filename))
#         filename = upload.filename
#
#         # dst = str(i) + ".jpg"
#         # src = "static/img/user_/" + filename
#         # dst = "static/img/user_/" + dst
#         # # rename() function will
#         # # rename all the files
#         # os.rename(src, dst)
#         # i += 1
#
#         destination = "/".join([target, filename])
#         print ("Accept incoming file:", filename)
#         print ("Save it to:", destination)
#         upload.save(destination)
#
#
#
#     i = 1
#     for rename in os.listdir("static/img/user_/"):
#         print("rename:",rename)
#         print("i:",i)
#         # print("id:",id)
#         if (rename != i):
#             dst = str(i) + ".jpg"
#             src = "static/img/user_/" + rename
#             dst = "static/img/user_/" + dst
#             # rename() function will
#             # rename all the files
#             os.rename(src, dst)
#
#     image_names = os.listdir('static/img/user_/')
#     print("name image:",image_names)
#
#     if "USERNAME" in session and "USER_ID" in session:
#         userName = session["USERNAME"]
#         userid = session["USER_ID"]
#         Privilege_user = session["Privilege_user"]
#         send = [userName, userid, Privilege_user]
#         return render_template('public/profile.html', send=send)
#         # return filename
#     else:
#         return render_template('public/index.html')
#     # return send_from_directory("images", filename, as_attachment=True)
#
# @app.route('/profile')
# def send_image():
#     image_names = os.listdir('static/img/user_/')
#     print("name image:",image_names)
#     return render_template("profile.html", image_names=image_names)

# @app.route('/send_imageProfile', methods=["POST"])
# def send_imageProfile():
#     image_names = os.listdir('static/img/user_/')
#     print("name image:",image_names)
#     return jsonify({'send_imageProfile': image_names})
    # return render_template("send_imageProfile", image_names=image_names)

# @app.route('/profile/<filename>')
# def send_image(filename):
#     return send_from_directory("static/img/user_", filename)


# save word page newword
@app.route('/save_Profile', methods=["POST"])
def save_Profile():
    check = False
    if (request.method == 'POST'):
        try:
            id_user = request.form["id_user_"]
            input_user = request.form["input_user_"]
            input_pass = request.form["input_pass_"]
            input_email = request.form["input_email_"]
            print("id_recommend ", id_user)
            print("Thai_recommend ", input_user)
            print("Hmong_recommend ", input_pass)
            print("Grammar_recommend ", input_email)
            database = Database()
            state = database.update_profile(id_user,input_user,input_pass,input_email)
            print("state:",state)
            check = True

        except Exception as e:
            print(e)
            print("error in update funtion update Recommend")
            return jsonify({'state': False})

    return jsonify({'state': check})

# ------------- end profile page -------------------------------
# save word page recomend
@app.route('/save_wordRecommend', methods=["POST"])
def save_wordRecommend():
    check = False
    if (request.method == 'POST'):
        try:
            id_recommend = request.form["id_recommend"]
            Thai_recommend = request.form["Thai_recommend"]
            Hmong_recommend = request.form["Hmong_recommend"]
            Grammar_recommend = request.form["Grammar_recommend"]
            # User_id = request.form["User_id"]
            print("id_recommend ", id_recommend)
            print("Thai_recommend ", Thai_recommend)
            print("Hmong_recommend ", Hmong_recommend)
            print("Grammar_recommend ", Grammar_recommend)
            database = Database()
            state = database.update_recommend(id_recommend,Thai_recommend,Hmong_recommend,Grammar_recommend)
            print("state:",state)
            check = True

        except Exception as e:
            print(e)
            print("error in update funtion update Recommend")
            return jsonify({'state': False})

    return jsonify({'state': check})

@app.route('/delete_Recommend',methods=['POST'])
def delete_Recommend():
    check = False
    if(request.method=='POST'):
        try:
            id_recommend = request.form["id_recommend"]
            Thai_recommend = request.form["Thai_recommend"]
            Hmong_recommend = request.form["Hmong_recommend"]
            Grammar_recommend = request.form["Grammar_recommend"]
            # User_id = request.form["User_id"]
            print("id_recommend ", id_recommend)
            print("Thai_recommend ", Thai_recommend)
            print("Hmong_recommend ", Hmong_recommend)
            print("Grammar_recommend ", Grammar_recommend)

            data = Database()
            data.delete_recommend(id_recommend,Thai_recommend,Hmong_recommend,Grammar_recommend)
            check = True

        except Exception as e:
            print(e)
            print("error in delete funtion deleteword")
            return jsonify({'state': False})

    return jsonify({'state':check})


# save word page newword
@app.route('/save_Newword', methods=["POST"])
def save_Newword():
    check = False
    if (request.method == 'POST'):
        try:
            id_newword = request.form["id_newword"]
            Thai_newword = request.form["Thai_newword"]
            Hmong_newword = request.form["Hmong_newword"]
            Grammar_newword = request.form["tpy_newword"]
            # User_id = request.form["User_id"]
            print("id_newword ", id_newword)
            print("Thai_newword ", Thai_newword)
            print("Hmong_newword ", Hmong_newword)
            print("Grammar_newword ", Grammar_newword)
            database = Database()
            state = database.update_newword(id_newword,Thai_newword,Hmong_newword,Grammar_newword)
            print("state:",state)
            check = True

        except Exception as e:
            print(e)
            print("error in update funtion update Recommend")
            return jsonify({'state': False})

    return jsonify({'state': check})

# delete newword
@app.route('/delete_Newword',methods=['POST'])
def delete_Newword():
    check = False
    if(request.method=='POST'):
        try:
            id_newword = request.form["id_newword"]
            Thai_newword = request.form["Thai_newword"]
            Hmong_newword = request.form["Hmong_newword"]
            Grammar_newword = request.form["tpy_newword"]
            print("id_recommend ", id_newword)
            print("Thai_recommend ", Thai_newword)
            print("Hmong_recommend ", Hmong_newword)
            print("Grammar_recommend ", Grammar_newword)

            data = Database()
            data.delete_newword(id_newword, Thai_newword, Hmong_newword, Grammar_newword)
            check = True

        except Exception as e:
            print(e)
            print("error in delete funtion deleteword")
            return jsonify({'state': False})

    return jsonify({'state':check})
# ----------------------------------------------------------------
# insert commend to Recommend
@app.route('/insert_commendtoRecommend', methods=["POST"])
def insert_commendtoRecommend():
    check = False
    if (request.method == 'POST'):
        try:
            getUser = request.form["getUser_id"]
            thaicommend = request.form["Thaicommend"]
            hmongcommend = request.form["Hmongcommend"]
            grammar_recommend = request.form["grammar"]
            print("id_recommend ", getUser)
            print("Thai_recommend ", thaicommend)
            print("Hmong_recommend ", hmongcommend)
            print("Grammar_recommend ", grammar_recommend)

            database = Database()
            database.insert_wordtoRecommend(thaicommend,hmongcommend,grammar_recommend,getUser)
            check = True

        except Exception as e:
            print(e)
            print("error in funtion commend to Recommend")
            return jsonify({'state': False})

    return jsonify({'state': check})

# insert commend to Recommend
@app.route('/deleteImage', methods=["POST"])
def deleteImage():
    # check = False
    send = []
    if (request.method == 'POST'):
        try:
            if "USER_ID" in session:
                userid = session["USER_ID"]
                filename = "static/img/user_/"
                st = 0
                for image_names in os.listdir('static/img/user_/'):
                    user_image = str(userid) + ".png"
                    if image_names == user_image:
                        image = filename + user_image
                        os.remove(image)
                        st = 1
                        break
                    else:
                        user_image = "default_user.png"
                        st = 0
                send = [userid, user_image, st]
                # return send

            # check = True

        except Exception as e:
            print(e)
            print("error in funtion delete image")

    return jsonify({'send': send})

# ================= end run =============================================
# admin route
@app.route('/admin')
def adminpage():
    userName = session["USERNAME"]
    userid = session["USER_ID"]
    Privilege_user = session["Privilege_user"]
    for image_names in os.listdir('static/img/user_/'):
        user_image = str(userid) + ".png"
        if image_names == user_image:
            user_image = "user_/" + user_image
            break
        else:
            user_image = "default_user.png"
    send = [userName, userid, Privilege_user, user_image]

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
    try:
        if "USERNAME" in session and "USER_ID" in session:
            userID = request.form['userID']
            get = Database()
            data = get.getNewword_toAdd(userID)
            return jsonify(data)
    except:
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
    print("branch tin from office")
    app.run()
    app.run(debug=True)


