import requests
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import date
import os.path
import csv
import Candle_Chart

def getStock(stockNo, CompanyName):
	stockNo_Csv = stockNo + '.csv'

	list_of_csv = []
	if os.path.isfile(stockNo_Csv):
		with open(stockNo_Csv, newline='') as f:
			reader = csv.reader(f)
			next(reader)
			list_of_csv = list(reader)
	else:
		with open(stockNo_Csv, 'w', newline='') as f:
			writer = csv.writer(f)
			writer.writerow(['Date','Open','High','Low','Close','Change','Change%','Devation%','trx_cnt','trx_record','avg_cnt','amount','FI','IT','Dealer','Big3','FI_Share%','loanM_chg','loanM_chg%','loanS_chg','loanS_chg%','loan_M_S%'])
	
	###############################################################################
	#                         股票行動機器人  【Post爬蟲】                        #
	###############################################################################

	# 要抓取的網址
	url = 'https://goodinfo.tw/StockInfo/ShowK_Chart.asp?STOCK_ID=' + stockNo + '&CHT_CAT2=DATE&PERIOD=365'
	# 附帶的資料必須要有
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}

	#請求網站
	list_req = requests.post(url, headers = headers)

	#print(list_req.text)

	#將整個網站的程式碼爬下來
	soup = BeautifulSoup(list_req.content, "html.parser")
	#items = soup.select('div[id="divPriceDetail"] > table > thead > tr')
	items = soup.select('tr[id^="row"]')
	item2 = []
	for i in items:
		ar0 = i.text.strip().split(' ')
		yy=datetime.now().strftime('%Y') + '/'
		if ar0[0] > datetime.now().strftime('%m/%d'):
			yy=date(datetime.now().year - 1, datetime.now().month, datetime.now().day).strftime('%Y') + '/'
		ar = (yy + i.text.strip()).split(' ')
		flag=1
		for row in list_of_csv:
			if ar[0]==row[0]:
				flag=0
				break
		if flag > 0:
			item2.append(yy + i.text.strip())
	with open(stockNo_Csv, 'a', newline='') as f:
		writer = csv.writer(f)
		for s2 in sorted(item2):
			ar = s2.split(' ')
			writer.writerow(ar)

	Candle_Chart.candlestick(stockNo, CompanyName)