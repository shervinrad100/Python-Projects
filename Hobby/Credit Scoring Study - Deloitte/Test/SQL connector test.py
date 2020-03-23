# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 02:35:48 2020

@author: sherv
"""

import mysql.connector


# set up connection
mydb = mysql.connector.connect(
        host="localhost",
        user="Guest",
        passwd=""
#        database="world"
    )

#                               what does cursor do???
mycursor = mydb.cursor()

# execute queries
mycursor.execute("CREATE DATABASE IF NOT EXISTS testdb")

mycursor.execute("SHOW DATABASES")


for x in mycursor:
    print(x)
    
# information_schema isnt in the folder but it is shown here?
    
    
# create sql script and run through python using path file
