from flask import Flask, request, jsonify, Response, send_file, render_template, redirect, url_for
import pymysql
import json
import datetime
import os
from binance import Binance
import korbit

app = Flask(__name__)

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
 api = ""
 secret  = ""
 k1 = ''
 k2 = ''
 
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
 
 

if __name__ == "__main__":
  #app.run(host = "dkc-shina.ru", port = 8001,debug=True)
  app.run(debug=True)
