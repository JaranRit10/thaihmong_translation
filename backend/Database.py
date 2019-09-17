import mysql.connector
from langdetect import detect
import datetime

import jsonify, json


class Database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="12345678",
        database="thaihmong_translator"
    )

    def searchFortran(self, word, wordClass):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345678",
            database="thaihmong_translator"
        )
        try:
            if (word.find('<Fail>') == -1):
                mycursor = mydb.cursor()
                sql = "SELECT * FROM thaihmongword WHERE Thai_word = %s and Word_class= %s "
                adr = (word, wordClass,)
                mycursor.execute(sql, adr)
                myresult = mycursor.fetchall()

                if (myresult == []):
                    sql = "SELECT * FROM thaihmongword WHERE Thai_word = %s and Hmong_word IS NOT null "
                    adr = (word,)
                    mycursor.execute(sql, adr)
                    myresult = mycursor.fetchall()

                    if (myresult == []):
                        myresult = list([('None', word, word, wordClass)])

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
                SELECT newword.id_newword,newword.Sentence_id,newword.New_word,newword.New_word_wordclass FROM newword
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

    def clickS(self,word):
        try:
            mycursor = self.mydb.cursor()
            word = str(word)
            word = word.strip()
            lang = detect(word)
            if (lang =='th'):
                sql = "SELECT Word_class,Hmong_word FROM thaihmongword WHERE Thai_word = %s LIMIT 20"
            else:
                sql = "SELECT Thai_word FROM thaihmongword WHERE Hmong_word = %s LIMIT 20"

            adr = (word,)
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
                    w_hmong = self.clickS(g_word[1])  # search hmong word
                    set_w = {g_word[1]: w_hmong}  # create word to put in class name
                    data[g_word[0]].append(set_w)   # put to class name

                    pass

                else:
                    word_class[g_word[0]] = 1 #create name in set format
                    w_hmong = self.clickS(g_word[1]) # search hmong word
                    set_w ={g_word[1]:w_hmong} # create word to put in class name
                    data[g_word[0]] = [set_w] # put to class name


            # print("data :", data)
            data =[word,data]
            return data
        except Exception as e:
            print(e)
            print("Eror in method click to searchword")
            return ""

    def searchWord(self, word):
        try:
            mycursor = self.mydb.cursor()
            word = str(word)
            word = word.strip()
            lang = detect(word)
            if (lang == 'th'):
                # print(type(lang))
                sql = "SELECT * FROM thaihmongword WHERE Thai_word like %s LIMIT 101"
            else:
                sql = "SELECT * FROM thaihmongword WHERE Hmong_word like %s LIMIT 101"
            word = word + '%'
            adr = (word,)
            mycursor.execute(sql, adr)
            myresult = mycursor.fetchall()
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

            print("Record inserted successfully into python_users table")
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
            update_query = """ 
            UPDATE translated_sentence 
            SET frequency=%s 
            where id_translated_sentence =%s """

            frequency = int(frequency) + 1
            value_update = (frequency, id)
            cursor.execute(update_query, value_update)
            connection.commit()
            print("update successfully")
        except mysql.connector.Error as error:
            connection.rollback()  # rollback if any exception occured
            print("Failed inserting record into python_users table {}".format(error))


if __name__ == '__main__':
    import time

    ss = time.time()
    dd = Database()
    get = dd.clickSearch("ให้")
    print(get)
    # hh = ['ให้', {'VERB': [{"pub":["ให้"]},{"muab":["ให้","กอบโกย","ควัก","หยิบ"]}], 'SCONJ': {"kom":"ให้"}}]
    # print(hh)

['ให้', {'VERB': [{'pub': [('ให้',)]}, {'muab': [('กอบโกย',), ('ควัก',), ('หยิบ',), ('ให้',)]}], 'SCONJ': [{'kom': [('ให้',)]}]}]
