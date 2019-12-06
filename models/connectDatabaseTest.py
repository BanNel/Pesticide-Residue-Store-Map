# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 14:22:12 2018

@author: user
"""
import pymysql.cursors
class MyDB(object):
    
    # connect to DB
    def __init__(self):
#        self._db_connection = db_module.connect('host', 'user', 'password', 'db')
        
        self._db_connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        
        self._db_cur = self._db_connection.cursor()

    def query(self, query, *params):
        self._db_cur.execute(query, *params)
        
        return self._db_cur
    
    # close the connection
    def __del__(self):
        self._db_connection.close()