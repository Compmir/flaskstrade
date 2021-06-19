from flask import Flask, request, jsonify, Response, send_file, render_template, redirect, url_for
import pymysql
import json
import datetime
import os
from binance import Binance
import korbit

app = Flask(__name__)
from PIL import Image, ImageDraw #Подключим необходимые библиотеки. 

# mode = int(input('mode:')) #Считываем номер преобразования. 
# draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 
# 

pairsBinance=[]
pairs=["fil", "aergo", "zil","xtz","ada","eos","xrp","eth","trx","xlm","ltc","luna","sol","bch","btc","algo","bnb","dot","etc","qtum","bcha"]
for pair in pairs:
 pairsBinance.append(pair.upper()+"USDT")


@app.after_request
def apply_caching(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response
    
@app.route("/",methods = ['POST', 'GET'])
def main():
 return 'flask'
 
@app.route("/trade")
def trade():
 api = "xkpZpQ2qsaizMQXxv7QcTSV4vp3uH2rpmn6NOqfAzlPzBLzknzoelJEaumXa5W3V"
 secret  = "eGbOEpZWfwP1gkuZatbMLKmd7UUOCgPp58s6Kk4DafYvtyWou6w4khbprur1zmh9"
 k1 = 'uml3OR0pHnXH2daJaUyFx08ek6f1DpOZLHEzBEj4Zod0MDCOyfROnvSZPCEzM'
 k2 = 'Per35fUEd1irKgYTIrlGJwXIVjktQ4Z7wPzdmr1mAppB40Me2oICmH8Wn4312'
 
 res=[]
 botBinance = Binance(API_KEY=api,API_SECRET=secret)
 symbol="BTCUSDT"
 prices=botBinance.tickerPrice()
 for price in prices:
  print(price['symbol'],": ",price['price'])
  if(price['symbol'] in pairsBinance):
  
 
 
 # price2=korbit.ticker("btc_")
   res.append([price['symbol'],": ",price['price']])
 print(res)

 # res=[]
 return Response(json.dumps(res),  mimetype='application/json')
 
 
@app.route("/image",methods = ['POST', 'GET'])
def image():

 if request.method != 'POST':
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Определение процента вхождения разных цветов</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
 else:
  file = request.files['file']
  if file :
   #  filename = securfile.filename)
     file.save("img/test.jpg")
 
     red = Image.open("img/red.jpg").load()[1,1] #Открываем изображение. 
     yellow = Image.open("img/yellow.jpg").load()[1,1] #Открываем изображение. 
     orange = Image.open("img/orange.jpg").load()[1,1] #Открываем изображение. 
     green = Image.open("img/green.jpg").load()[1,1] #Открываем изображение. 
     blue = Image.open("img/blue.jpg").load()[1,1] #Открываем изображение. 
     black = Image.open("img/black.jpg").load()[1,1] #Открываем изображение. 
     white = Image.open("img/white.jpg").load()[1,1] #Открываем изображение. 
     cyan = Image.open("img/cyan.jpg").load()[1,1] #Открываем изображение. 
     purple = Image.open("img/purple.jpg").load()[1,1] #Открываем изображение. 

     res=[]
     
     image = Image.open("img/test.jpg")
     #Открываем изображение. 
     #print()
     pix = image.load() #Выгружаем значения пикселей
     width = image.size[0] #Определяем ширину. 
     height = image.size[1] #Определяем высоту. 	
     pixa=0
     pixb=0
     pixc=0
     colors=  ["red","orange","yellow","green","cyan","blue","purple","black","white"]
     colcount=[0,0,0,0,0,0,0,0,0]

     for i in range(width):
      for j in range(height):
       a = pix[i, j][0]
       b = pix[i, j][1]
       c = pix[i, j][2]   
       
       deltared=((a-red[0])**2 + (b-red[1])**2 + (c-red[2])**2  )** (0.5)
      # print(deltared)
       deltaorange=((a-orange[0])**2 + (b-orange[1])**2 + (c-orange[2])**2  )** (0.5)
       deltayellow=((a-yellow[0])**2 + (b-yellow[1])**2 + (c-yellow[2])**2  )** (0.5)
       deltagreen=((a-green[0])**2 + (b-green[1])**2 + (c-green[2])**2  )** (0.5)
       deltablue=((a-blue[0])**2 + (b-blue[1])**2 + (c-blue[2])**2  )** (0.5)
       deltablack=((a-black[0])**2 + (b-black[1])**2 + (c-black[2])**2  )** (0.5)
       deltawhite=((a-white[0])**2 + (b-white[1])**2 + (c-white[2])**2  )** (0.5)
       deltacyan=((a-cyan[0])**2 + (b-cyan[1])**2 + (c-cyan[2])**2  )** (0.5)
       deltapurple=((a-purple[0])**2 + (b-purple[1])**2 + (c-purple[2])**2  )** (0.5)
       lst=[deltared,deltaorange,deltayellow,deltagreen,deltacyan,deltablue,deltapurple,deltablack,deltawhite]
       ind=lst.index(min(lst))
       colcount[ind]+=1
       
     i=0
     for color in colors:
      res.append([color,colcount[i]*100/(height*width) ])
      i+=1
    
     return Response(json.dumps(res),  mimetype='application/json')
# return pix
 
 

if __name__ == "__main__":
  app.run(host = "dkc-shina.ru", port = 8001,debug=True)