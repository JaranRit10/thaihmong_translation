import mysql.connector
from backend.Database import Database
class Database_test() :


    mydb:any
    mydb_test: any

    def __init__(self):
        self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345678",
                database="thaihmong_translator"
            )

        self.mydb_test = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="12345678",
            database="for_test"
        )


    def delete_word(self,id):
        mycursor = self.mydb_test.cursor()
        sql = "DELETE FROM thaihmongword WHERE id_word = %s"
        adr = (id,)
        mycursor.execute(sql, adr)
        self.mydb.commit()


    def delete_repeatedly(self):

        try:
            mycursor = self.mydb_test.cursor()
            sql_insert_query = """
            select * from thaihmongword
                inner join ( select *,COUNT(thaihmongword.thai_word) from thaihmongword
                GROUP by thaihmongword.thai_word
                HAVING COUNT(thaihmongword.thai_word)>1 )as b
                on thaihmongword.Thai_word = b.Thai_word
                where thaihmongword.id_word != b.id_word AND (thaihmongword.thai_word = b.thai_word AND thaihmongword.hmong_word IS null )
            
            """

            mycursor.execute(sql_insert_query)
            myresult = mycursor.fetchall()
            db = Database_test()
            for row in myresult:
                print(row[0])
                db.delete_word(row[0])
            print(len(myresult)/2)


        except Exception as e:
            print(e)

    def check_word(self,word_hmong,word_thai):
        have = True
        try:
            mycursor = self.mydb.cursor()
            query_formtest = """
                                  SELECT * FROM thaihmongword
                                  WHERE Thai_word =%s and Hmong_word = %s
                            """
            adr = (word_hmong, word_thai)
            mycursor.execute(query_formtest, adr)
            myresult = mycursor.fetchall()
            print(myresult)
            if(myresult == []):
                return False
            else:
                return True

        except Exception as e:
            print(e)



    # เพิ่มคำศัพท์จากฐานข้อมูลอื่นเข้ามาในฐานข้อมูหลัก โดยไม่ซ้ำกับข้อมุลเดิม หมายเหตุ ภาษาไทยซ้ำได้แต่ภาษาม้งต้องไม่ซ้ำ
    def add_word(self):
        mycursor = self.mydb_test.cursor()
        query_formtest = """
              SELECT * FROM thaihmongword_last_from_run
              WHERE Hmong_word IS not NULL
        """
        mycursor.execute(query_formtest)
        myresult = mycursor.fetchall()
        # print(myresult)
        cout =0
        for data in myresult:
            have = self.check_word(data[1],data[2])
            print(have)
            if(have == False ):
                dd = Database()
                # dd.insertNewword_addmin(data[1], data[2], data[3], 0)
                cout +=1
                print(data)
                input()
        print(cout)
if __name__ == '__main__':


    d = Database_test()
    a = d.add_word()