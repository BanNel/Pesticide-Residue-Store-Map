# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 17:06:24 2018

@author: 我是羅聖明:D 
@Apply :route

"""
from models.connectDatabaseTest import  MyDB
from flask import Flask, render_template, request
app = Flask(__name__)


# 連結mysql Database
#Sql Query查詢   
db = MyDB(); 
db2 = MyDB();
dbMapMarker = MyDB(); 

@app.route('/indexTest')
def index():



     return render_template('user.html')
 
    
    # 開啟index  (google map 插入marker )
@app.route('/map/')
def indexTest():
    #Sql Query查詢
    queryStringMapMarker='SELECT `latitude`,`longitude` FROM `retailer` '
    result = dbMapMarker.query(queryStringMapMarker)
    features = ''
    tempCordinate = ''
    title = '嗨'
    
    #獲取好多數據
    
    for row in result:
        
        tempCordinate = "{position: new google.maps.LatLng(" + \
        row.get("latitude")+"," + row.get("longitude")+"),type: parking," + \
        "title: 'goood'},"
        features = features + tempCordinate
#        tempCordinate = '{position: new google.maps.LatLng(' + \
#        row.get('latitude')+',' + row.get('longitude')+'),type: parking,' + \
#    'title: '+title + '},'
        
        
         
    return render_template('mapwithcustommarker.html', name = features)
 
    
    
@app.route('/usr/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/')
def maps():
    return render_template('bottom_MAP.html' )

@app.route('/rank/')
def rank():
    return render_template('SORT.html' )

@app.route('/status/')
def status():
    return render_template('NEWS.html' )


@app.route('/knowledge/')
def knowledge():
    
    
    #Sql Query查詢(農藥名稱)
    queryString ='SELECT `english_name` FROM `pesticide` '
    queryStringPesti ='SELECT * FROM `pesticide` where  `english_name` = \'' + request.args.get('Pesticide', default=None, type=None)  +'\''
    queryStringPestiRange= 'SELECT crop,virus,use_time,safe_date FROM `pesticide_range` inner join pesticide on pesticide_range.code = pesticide.code where pesticide.english_name =\''+ request.args.get('Pesticide', default=None, type=None) +'\' group by crop,virus,use_time,safe_date' 
    
    #(農藥名稱)dropdown
    resultPesti = db.query(queryString)
    resultPestiDetail = db2.query(queryStringPestiRange)

    selecttion = ''
    selecttionGGGGG = ''
    
    for row1 in resultPesti:
                   selecttion +=  '<option >' + row1.get("english_name") + '</option>'

    for rowgggg in resultPestiDetail:  
        
        selecttionGGGGG  = selecttionGGGGG +'<tr> <th  width="200"><font face="微軟正黑體" size="4px">'+rowgggg.get("crop")+'</th>' +\
        '<th  width="200"><font face="微軟正黑體6666" size="4px">'+rowgggg.get("virus")+'</th> </tr>' 
        
#        '<th  width="200"><font face="微軟正黑體" size="4px">'+rowgggg.get("use_time")+'</th>'+\
#        '<th  width="200"><font face="微軟正黑體" size="4px">'+rowgggg.get("safe_date")+'</th>'
#        '<th  width="200"><font face="微軟正黑體" size="4px">'+rowgggg.get("vaild_date")+'</th>' +\
          
      
    return render_template('KNOWLEDGE.html', table_info=selecttion,corp=selecttionGGGGG,name=request.args.get('Pesticide', default=None, type=None))


#####處理path路徑
@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)


if __name__ == "__main__":
    app.run(debug=True)
    
