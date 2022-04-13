import sqlite3
def sqlcon():
    global sqliteConnection,cur
    sqliteConnection=sqlite3.connect("sql.db")
    cur=sqliteConnection.cursor()
def sqlcreate():
    query="create table Movies(name varchar(45),actor varchar(50),actress varchar(50),director varchar(50),year_of_release Integer);"
    cur.execute(query)
def sqlinsert():
    query1="Insert into Movies values('KGF Chapter 2','YASH','SHRI NIDHI','Prashanth Neil','2022');"
    query2="Insert into Movies values('Vikranth Rona','Kiccha Sudeep','Jackline Fernandes','Anup Bhandari','2022');"
    query3="Insert into Movies values('Rajakumara','Puneeth Raj Kumar','Priya Ananad','Santhosh A','2017');"
    cur.execute(query1)
    cur.execute(query2)
    cur.execute(query3)
    sqliteConnection.commit()
def sqlselect():
    sqliteConnection=sqlite3.connect("sql.db")
    cur=sqliteConnection.cursor()
    query1="select * from Movies;"
    query2="select * from Movies where actor='Puneeth Raj Kumar';"
    cur.execute(query1)
    result1=cur.fetchall()   
    cur.execute(query2)
    result2=cur.fetchall()   
    print(result1)
    print(result2)
sqlcon()
sqlcreate()
sqlinsert()
sqlselect()
