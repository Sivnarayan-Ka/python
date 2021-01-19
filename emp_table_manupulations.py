## 18.Write a python program that read the whole data from the table employee and display all 
# the records in it.

## 20.Write a function update to accept the employee number as parameter and update the record
# in employee table.

## 22.Write a python application that fetches only those records from winfo table of worker 
# database where status is “contractual”

## All above 3 are done here as they are inter related.
## Here we are using mysql using mysql.connector module.This does not come as a default 
# package in python so we have to install first mysql.connector using pip installer
# >  python -m pip install mysql-connector  

import mysql.connector

def main():
    ## Creating the connection object use your PC username and password in below command
    psdfile = open ('psd.txt','r')
    uname = psdfile.readline().split(":")[1].strip()
    psd = psdfile.readline().split(":")[1].strip()
        
    print(f"username = {uname} and password = {psd}")        
    myconn = mysql.connector.connect(host = 'localhost',user = uname, password = psd)
    
    print(myconn)
    # Creating the cursor object
    cur = myconn.cursor()
    print(cur)
    try:
        #creating a new database
        cur.execute("create datatbase EmpDb")
        
        #getting the list of all databases which will now include the new database
        # dbs = cur.execeute("show databases")
    except:
        
        print("db cur execute for show datatabes crashed ")
        myconn.rollback()
        psdfile.close()
    
    for x in cur:
        print(x)
    
    myconn.close()
    psdfile.close()
    print("db myconn connection closed")

main()