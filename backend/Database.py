import mysql.connector
from langdetect import detect
import datetime

import jsonify, json


class Database():
    mydb:any

    def __init__(self):
        self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345678",
                database="thaihmong_translator"
            )



    def searchFortran(self, word, wordClass,tage=True):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345678",
            database="thaihmong_translator"
        )

        try:
            word_notTag =['แก่']

            if (word.find('<Fail>') == -1):
                mycursor = mydb.cursor()
                if(tage):
                    sql = "SELECT * FROM thaihmongword WHERE Thai_word = %s and Word_class= %s "
                    adr = (word, wordClass,)
                    mycursor.execute(sql, adr)
                    myresult = mycursor.fetchall()
                else:
                    myresult = []

                if (myresult == []):
                    sql = "SELECT * FROM thaihmongword WHERE Thai_word = %s and Hmong_word IS NOT null "
                    adr = (word,)
                    mycursor.execute(sql, adr)
                    myresult = mycursor.fetchall()

                    if (myresult == []):
                        myresult = list([('None', word, word, wordClass)])

                        # if(myresult[0][3]!="PUNCT"): #สำหรับตรวจสอบคำที่หายไป ในการ test
                        #     input("คำที่หาย :"+str(myresult))

            else:
                # ลบ <Fail> ออกจาก word
                if (word.find('<Fail>') != -1):
                    # print(word)
                    # print(word.find('<Fail>'))
                    word = (word[word.find('<Fail>') + 6:word.find('</Fail>')])
                myresult = list([('Fail', word, word, wordClass)])
        except Exception as e:
            print(e)
            print("Eror in method searchFortran")
        # print(myresult)
        return myresult


    def checkUsername_signUp(self,name):
        mycursor = self.mydb.cursor()
        name = (str(name).strip(),)
        try:
            sql = """
            SELECT * FROM user_
            WHERE Username = %s
            """
            mycursor.execute(sql,name)
            myresult = mycursor.fetchall()
            if(len(myresult)>0):
                return True
            else:
                return  False
        except Exception as e:
            print(e)
            print("Eror in method checkUsername_signUp")

    def login(self, username, password):
        mycursor = self.mydb.cursor()
        try:
            try:
                sql = "SELECT * FROM user_ WHERE Username = %s and User_password = %s "
                adr = (username, password,)
                mycursor.execute(sql, adr)
                myresult = mycursor.fetchall()
            except Exception as e:
                print(e)
            if (myresult == []):
                sql = "SELECT * FROM user_ WHERE Username = %s "
                adr = (username,)
                mycursor.execute(sql, adr)
                myresult = mycursor.fetchall()
                if (myresult == []):
                    myresult = "None"
                else:
                    myresult = "notNone"

        except Exception as e:
            print(e)
            print("Eror in method login")
        return myresult
# ===========================================================
    def getRecommend(self):
        mycursor = self.mydb.cursor()
        try:
            sql = "SELECT * FROM recommend"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            return myresult
        except Exception as e:
            print(e)
            print("Eror in method getRecommend")

    def getRecommend_toCheck(self, userID):
        mycursor = self.mydb.cursor()
        try:
            sql = """ SELECT recommend.id_recommend,recommend.thai_recommend,recommend.Hmong_recommend FROM check_recommend
                    RIGHT JOIN (SELECT * FROM recommend WHERE User_id != %s) AS recommend
                    ON check_recommend.id_recommend = recommend.id_recommend
                    WHERE check_recommend.User_id_user !=%s OR check_recommend.User_id_user IS NULL
            """
            adr = (userID, userID)
            mycursor.execute(sql, adr)
            myresult = mycursor.fetchall()

        except Exception as e:
            print(e)
            print("Eror in method getRecommend")
        return myresult

    def getNewword(self):
        mycursor = self.mydb.cursor()
        try:
            sql = "SELECT * FROM newword"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
        except Exception as e:
            sql = "SELECT * FROM newword"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()

            print(e)
            print("Eror in method getNewword")
        return myresult


    def getNewword_toAdd(self, userID):
        mycursor = self.mydb.cursor()
        try:
            sql = """
                SELECT newword.id_newword,newword.Sentence_id,newword.Thai_word,newword.New_word_wordclass FROM newword
                LEFT JOIN recommend
                ON newword.id_newword = recommend.id_newword
                WHERE recommend.User_id !=%s OR recommend.User_id IS NULL
            """
            adr = (userID,)
            mycursor.execute(sql, adr)
            myresult = mycursor.fetchall()

        except Exception as e:
            print(e)
            print("Eror in method getNewword")
        return myresult

    def insertSentence_newword(self, Thai_sentence, Hmong_sentence):
        mycursor = self.mydb.cursor()

        sql = "select max(id_sentence) from sentence"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        try:
            get_myresult = (myresult[0][0])
            id_sentence = get_myresult + 1
        except Exception as e:
            id_sentence = 1
        try:
            sql = """ 
                        INSERT INTO `sentence`
                        (`id_sentence`,`Thai_sentence`, `Hmong_sentence`,`Datetime`) 
                        VALUES (%s,%s,%s,%s)
                    """
            adr = (id_sentence, Thai_sentence, Hmong_sentence, datetime.datetime.now(),)
            mycursor.execute(sql, adr)
            self.mydb.commit()
        except Exception as e:
            print(e)
        return id_sentence

    def insertNewword_toNewword(self, Sentence_id, New_word, New_word_wordclass):
        mycursor = self.mydb.cursor()
        sql = "select max(id_newword) from newword"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        try:
            get_myresult = (myresult[0][0])
            id_newword = get_myresult + 1
        except Exception as e:
            id_newword = 1

        try:
            sql = """ 
                        INSERT INTO `newword`
                        (`id_newword`,`Sentence_id`, `New_word`,`New_word_wordclass`) 
                        VALUES (%s,%s,%s,%s)
                    """
            adr = (id_newword, Sentence_id, New_word, New_word_wordclass,)
            mycursor.execute(sql, adr)
            self.mydb.commit()
        except Exception as e:
            print(e)


    def insertNewword_to_recommend(self):
        try:
            connection = self.mydb
            sql_insert_query = """ 
                    INSERT INTO `recommend`
                    (`Admin_id`,`Thaihmongword_word_id`, `Recommend_id`,`Datetime`,`Management_type`,`Managed_words`) 
                    VALUES (%s,%s,%s,%s,%s,%s)
            """
            time = datetime.datetime.now()
            value_insert = ()
            cursor = connection.cursor()
            cursor.execute(sql_insert_query, value_insert)
            connection.commit()

        except Exception as e:
            print(e)

    def clickS(self,word,word_class="*"):
        try:
            mycursor = self.mydb.cursor()
            word = str(word)
            word = word.strip()
            lang = detect(word)
            if (lang =='th'):
                sql = "SELECT Word_class,Hmong_word FROM thaihmongword WHERE Thai_word = %s LIMIT 20"
                adr = (word,)
            else:
                sql = "SELECT Thai_word FROM thaihmongword WHERE Hmong_word = %s and Word_class =%s LIMIT 20"
                adr = (word,word_class)
            mycursor.execute(sql, adr)
            get = mycursor.fetchall()
            return get
        except Exception as e:
            print(e)
            print("Eror in method click to clickS")
            return ""

    def clickSearch(self, word):
        try:
            get = self.clickS(word)
            print(get)
            word_class = {}
            data = {}
            word_Hmong = {}
            for g_word in get:
                if (g_word[0] in word_class):
                    # w = data[g_word[0]]
                    # w.append(g_word[1])
                    # data[g_word[0]] = w
                    w_hmong = self.clickS(g_word[1],g_word[0])  # search hmong word
                    set_w = {g_word[1]: w_hmong}  # create word to put in class name
                    data[g_word[0]].append(set_w)   # put to class name

                    pass

                else:
                    word_class[g_word[0]] = 1 #create name in set format
                    w_hmong = self.clickS(g_word[1],g_word[0]) # search hmong word
                    set_w ={g_word[1]:w_hmong} # create word to put in class name
                    data[g_word[0]] = [set_w] # put to class name

            # print("data :", data)
            data =[word,data]
            return data
        except Exception as e:
            print(e)
            print("Eror in method click to searchword")
            return ""

    def addNewUser(self,Username,User_password,First_name,Last_name,Email):
        try:
            connection = self.mydb
            sql_insert_query = """ INSERT INTO `user_`
                         (`Privilege_user`,`Datetime_register`, `Username`,`User_password`,`First_name`,`Last_name`,`Email`,`Status`) 
                         VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""

            time = datetime.datetime.now()
            value_insert = (1, time, Username, User_password,First_name,Last_name,Email,1)
            cursor = connection.cursor()
            cursor.execute(sql_insert_query, value_insert)
            connection.commit()
            return True

        except Exception as e:
            print(e)
            return False
    def searchWord(self, word):
        myresult =[]
        try:
            mycursor = self.mydb.cursor()
            word = str(word)
            word = word.strip()
            lang = detect(word)
            for i in range(2):
                if (lang == 'th'):
                    # print(type(lang))
                    if(i==0):
                        sql = "SELECT * FROM thaihmongword WHERE Thai_word = %s "
                    else:
                        sql = "SELECT * FROM thaihmongword WHERE Thai_word like %s AND Thai_word != %s LIMIT 101"
                else:
                    if(i==0):
                        sql = "SELECT * FROM thaihmongword WHERE Hmong_word = %s "
                    else:
                        sql = "SELECT * FROM thaihmongword WHERE Hmong_word like %s AND Hmong_word != %s LIMIT 101"

                if(i==0):
                    word_used = word
                    adr = (word_used,)
                else:
                    word_used = word+ '%'
                    adr = (word_used,word)
                # print(sql,adr)
                mycursor.execute(sql, adr)
                myresult.extend(mycursor.fetchall())
                # print(myresult)
                # input(":")

            return myresult
        except Exception as e:
            print(e)
            print("Eror in method searchword")

    def insert_time_management(self, Admin_id, Thaihmongword_word_id, Recommend_id, Management_type, Managed_words):

        try:
            connection = self.mydb
            sql_insert_query = """ INSERT INTO `time_management`
                        (`Admin_id`,`Thaihmongword_word_id`, `Recommend_id`,`Datetime`,`Management_type`,`Managed_words`) 
                        VALUES (%s,%s,%s,%s,%s,%s)"""

            time = datetime.datetime.now()
            value_insert = (Admin_id, Thaihmongword_word_id, Recommend_id, time, Management_type, Managed_words)
            cursor = connection.cursor()
            cursor.execute(sql_insert_query, value_insert)
            connection.commit()

        except Exception as e:
            print(e)

    def insertNewword_addmin(self, Thai_word, Hmong_word, Word_class, Addmin_id):
        try:
            mycursor = self.mydb.cursor()
            sql = "select max(id_word) from thaihmongword"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            try:
                get_myresult = (myresult[0][0])
                id_word = get_myresult + 1
            except Exception as e:
                id_word = 1

            connection = self.mydb
            sql_insert_query = """ INSERT INTO `thaihmongword`
                                  (`id_word`,`Thai_word`, `Hmong_word`,`Word_class`,`Adder`) 
                                  VALUES (%s,%s,%s,%s,%s)"""
            value_insert = (id_word, Thai_word, Hmong_word, Word_class, Addmin_id)
            cursor = connection.cursor()
            cursor.execute(sql_insert_query, value_insert)
            connection.commit()

            # get_idword = cursor.lastrowid
            # print("get id : "+str(get_idword))

            try:
                db = Database()
                db.insert_time_management(Addmin_id, id_word, None, "insert", Thai_word)
            except Exception as e:
                print(e)

            # print("Record inserted successfully into python_users table")
        except mysql.connector.Error as error:
            connection.rollback()  # rollback if any exception occured
            print("Failed inserting record into python_users table {}".format(error))

    def updateWord(self, id_word, Thai_word, Hmong_word, Word_class, Addmin_id):
        try:
            connection = self.mydb
            cursor = connection.cursor()

            query = """ select Thai_word from thaihmongword  where id_word =%s """
            value = (id_word,)
            cursor.execute(query, value)
            Managed_words = cursor.fetchall()
            Managed_words = Managed_words[0][0]

            update_query = """ UPDATE thaihmongword SET Thai_word=%s, 
                Hmong_word=%s,Word_class=%s,Adder=%s where id_word =%s """
            value_update = (Thai_word, Hmong_word, Word_class, Addmin_id, id_word)

            cursor.execute(update_query, value_update)
            connection.commit()
            print("update successfully")
            try:
                db = Database()
                db.insert_time_management(Addmin_id, id_word, None, "update", Managed_words)
            except Exception as e:
                print(e)

        except mysql.connector.Error as error:
            connection.rollback()  # rollback if any exception occured
            print("Failed inserting record into python_users table {}".format(error))

    def deleteWord(self, userID, id_word, thaiword):
        try:
            connection = self.mydb
            cursor = connection.cursor()

            delete_query = "DELETE FROM thaihmongword WHERE id_word = %s AND Thai_word = %s"
            id_delete = (id_word, thaiword,)

            cursor.execute(delete_query, id_delete)
            connection.commit()

            db = Database()
            db.insert_time_management(userID, id_word, None, "delete", thaiword)

            print("delete successfully")
        except mysql.connector.Error as error:
            connection.rollback()  # rollback if any exception occured
            print("Failed inserting record into python_users table {}".format(error))

    def insertTranslated_sentence(self, time_translate, thai_sentence, hmong_sentence, frequency):
        try:
            connection = self.mydb
            sql_insert_query = """ INSERT INTO `translated_sentence`
                        (`time_translate`,`thai_sentence`, `hmong_sentence`,`frequency`) 
                        VALUES (%s,%s,%s,%s)"""

            time = datetime.datetime.now()
            value_insert = (time, thai_sentence, hmong_sentence, frequency)
            cursor = connection.cursor()
            cursor.execute(sql_insert_query, value_insert)
            connection.commit()
        except Exception as e:
            print(e)

    def search_translated_sentence(self, thai_sentence):
        try:
            mycursor = self.mydb.cursor()
            word = str(thai_sentence)
            word = word.strip()
            sql = """SELECT id_translated_sentence,time_translate
                  thai_sentence,hmong_sentence,frequency 
                  FROM translated_sentence 
                  WHERE thai_sentence =%s """
            adr = (word,)
            mycursor.execute(sql, adr)
            myresult = mycursor.fetchall()
            return myresult
        except Exception as e:
            print(e)

    def update_translated_sentence(self, id, frequency):
        try:
            connection = self.mydb
            cursor = connection.cursor()
            update_query = """ UPDATE translated_sentence SET frequency=%s 
                            where id_translated_sentence =%s """

            frequency = int(frequency) + 1
            value_update = (frequency, id)
            cursor.execute(update_query, value_update)
            connection.commit()
            print("update successfully")
        except mysql.connector.Error as error:
            connection.rollback()  # rollback if any exception occured
            print("Failed inserting record into python_users table {}".format(error))

    # ==============================================================
# profile data
    def getprofile(self):
        mycursor = self.mydb.cursor()
        try:
            # id = id_user
            sql = "SELECT * FROM user_ "
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            return myresult
        except Exception as e:
            print(e)
            print("Eror in method getProfile")

    # =======================================================
# update page recommend
    def update_recommend(self,id_recommend,Thai_recommend,Hmong_recommend,Grammar_recommend):
        try:
            connection = self.mydb
            cursor = connection.cursor()

            update_query = """ UPDATE recommend 
            SET Thai_recommend=%s, Hmong_recommend=%s,type_error=%s 
            WHERE id_recommend=%s"""
            value_update = (Thai_recommend, Hmong_recommend, Grammar_recommend, id_recommend)

            cursor.execute(update_query, value_update)
            connection.commit()
            print("update successfully")
            return 1
        except Exception as e:
            print("Failed inserting record into python_users table {}".format(e))
            return e

# delete page recommend
    def delete_recommend(self,id_recommend,Thai_recommend,Hmong_recommend,Grammar_recommend):
        try:
            connection = self.mydb
            cursor = connection.cursor()

            delete_query = """DELETE FROM recommend 
            WHERE id_recommend=%s and Thai_recommend=%s and Hmong_recommend=%s and type_error=%s"""
            id_delete = (id_recommend, Thai_recommend, Hmong_recommend, Grammar_recommend)

            cursor.execute(delete_query, id_delete)
            connection.commit()
            print("delete successfully")
            return 1
        except Exception as e:
            print("Failed inserting record into python_users table {}".format(e))
            return e

# update page newword
    def update_newword(self,id_newword,Thai_newword,Hmong_newword,Grammar_newword):
        try:
            connection = self.mydb
            cursor = connection.cursor()

            update_query = """ UPDATE newword 
            SET Thai_word=%s, Hmong_word=%s,New_word_wordclass=%s 
            WHERE id_newword=%s"""
            value_update = (Thai_newword,Hmong_newword,Grammar_newword, id_newword)

            cursor.execute(update_query, value_update)
            connection.commit()
            print("update successfully")
            return 1
        except Exception as e:
            print("Failed inserting record into python_users table {}".format(e))
            return e

# delete page newword
    def delete_newword(self,id_newword,Thai_newword,Hmong_newword,Grammar_newword):
        try:
            connection = self.mydb
            cursor = connection.cursor()

            delete_query = """DELETE FROM newword 
            WHERE id_newword=%s and Thai_word=%s and Hmong_word=%s and New_word_wordclass=%s"""
            id_delete = (id_newword,Thai_newword,Hmong_newword,Grammar_newword)

            cursor.execute(delete_query, id_delete)
            connection.commit()
            print("delete successfully")
            return 1
        except Exception as e:
            print("Failed inserting record into python_users table {}".format(e))
            return e

# update page profile
    def update_profile(self,id_user, Username, User_password, Email):
        try:
            connection = self.mydb
            cursor = connection.cursor()

            update_query = """ UPDATE user_ 
            SET Username=%s, User_password=%s, Email=%s 
            WHERE id_user=%s"""
            value_update = (Username,User_password,Email,id_user)

            cursor.execute(update_query, value_update)
            connection.commit()
            print("update profile successfully")
            return 1
        except Exception as e:
            print("Failed inserting record into python_users table {}".format(e))
            return e

    def insert_wordtoRecommend(self, Thai_recommend, Hmong_recommend, type_error, User_id):
        mycursor = self.mydb.cursor()
        sql = "select max(id_recommend) from recommend"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        try:
            get_myresult = (myresult[0][0])
            id_recommend = get_myresult + 1
        except Exception as e:
            id_recommend = 1

        # connection = self.mydb
        try:
            sql = """ INSERT INTO `recommend`
                    (`id_recommend`, `Thai_recommend`, `Hmong_recommend`, `type_error`, `Datetime`, `User_id`) 
                    VALUES (%s,%s,%s,%s,%s,%s)"""

            adr = (id_recommend, Thai_recommend, Hmong_recommend, type_error, datetime.datetime.now(), User_id)
            mycursor.execute(sql, adr)
            self.mydb.commit()
        except Exception as e:
            print("error from funtion insert commend to Recommend")
            print(e)



if __name__ == '__main__':
    import time

    ss = time.time()
    dd = Database()

<<<<<<< HEAD
    # aa = dd.insert_wordtoRecommend("เข้าใจ","nkag siab","gammar",4)
    # print(aa)

    bb = dd.getNewword_toAdd(3)
    print(bb)
=======
    aa = dd.insert_wordtoRecommend("เข้าใจ","nkag siab","gammar",4)
    print(aa)
    print(dd.addNewUser("sdfe","123456","tin","las","idkf@hot.com"))
>>>>>>> 8394b3360032000feab761b71840ef49265ae7b8
    # print(dd.searchWord("เป็น"))


# =======
    # aa = dd.update_recommend(7,"สระน้ำ","pas dej","word")
    # get = dd.clickSearch("ให้")
    # print(get)

    # hh = ['ให้', {'VERB': [{"pub":["ให้"]},{"muab":["ให้","กอบโกย","ควัก","หยิบ"]}], 'SCONJ': {"kom":"ให้"}}]
    # print(hh)

