import mysql.connector

class Database() :

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="12345678",
        database="for_test"
    )


    def delete_word(self,id):
        mycursor = self.mydb.cursor()
        sql = "DELETE FROM thaihmongword WHERE id_word = %s"
        adr = (id,)
        mycursor.execute(sql, adr)
        self.mydb.commit()


    def delete_repeatedly(self):

        try:
            mycursor = self.mydb.cursor()
            sql_insert_query = """select * from thaihmongword
                inner join ( select *,COUNT(thaihmongword.thai_word) from thaihmongword
                GROUP by thaihmongword.thai_word
                HAVING COUNT(thaihmongword.thai_word)>1 )as b
                on thaihmongword.Thai_word = b.Thai_word
                where thaihmongword.id_word != b.id_word AND (thaihmongword.thai_word = b.thai_word AND thaihmongword.hmong_word IS null )"""

            mycursor.execute(sql_insert_query)
            myresult = mycursor.fetchall()
            db = Database()
            for row in myresult:
                print(row[0])
                db.delete_word(row[0])
            print(len(myresult)/2)


        except Exception as e:
            print(e)


if __name__ == '__main__':

    dd = Database()
    dd.delete_repeatedly()