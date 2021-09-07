import mysql.connector
def save_data(firstname,product,email):

    input_data=str(firstname)+ "," + str(product) + "," + str(email)
    file=open("output.txt","a")
    file.write(input_data)
    file.close()
# save_data("vinayvarma","6767676767","verygood")

def store_data(firstname,product,email):
    mydb=mysql.connector.connect(host="localhost",user="root",password="NJDRD@90",port=3306,database="rasadb")
    cursor=mydb.cursor()
    # cursor.execute("create database rasadb")
    cursor.execute(f'insert into rasadata(firstname,product,email) values("{firstname}","{product}","{email}");')
    mydb.commit()

def restore_data():
    mydb = mysql.connector.connect(host="localhost", user="root", password="NJDRD@90", port=3306, database="rasadb")
    cursor = mydb.cursor()
    # cursor.execute("create database rasadb")
    cursor.execute("select * from rasadata;")
    data=cursor.fetchall()
    print(data)
    list1=print(data[0])
    list2=print(data[1])
    print(list1)
    print(list2)

restore_data()

# store_data("vinay","lappyy","vinay@gmail.com")