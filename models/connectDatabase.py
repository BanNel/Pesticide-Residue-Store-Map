# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:12:13 2018

@author: user
"""

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * from mytable"
        
        cursor.execute(sql)
        
        print(type(cursor))
        
        #獲取好多數據
        for row in cursor:
            print(row)

        
        
        #使用fetchone()方法獲取一條數據
#        result = cursor.fetchone()
#        print(result)
finally:
    connection.close()