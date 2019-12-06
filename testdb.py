# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 14:37:29 2018

@author: user
說明:透過Class去查詢資料庫
"""
from models.connectDatabaseTest import  MyDB

#Sql Query查詢   
db = MyDB(); 

#Sql Query查詢
queryString='SELECT `latitude`,`longitude` FROM `retailer` WHERE id < 50 '

#Sql Query參數
data = [
  ('18'),('5'),('8')
  ]

result = db.query(queryString)

features = ''
tempCordinate = ''
#獲取好多數據
for row in result:
    tempCordinate =  '{position: new google.maps.LatLng(' + row.get('latitude')+',' + row.get('longitude')+',type: parking},'
    features = features +tempCordinate
    
    print(features)