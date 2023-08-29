import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import requests
import json
quote = '台積電(2330)'

def candlestick(stockNo, CompanyName):
	quote = CompanyName + '(' + stockNo + ')'
	stockNo_Csv = stockNo + '.csv'
	stockdata_df = pd.DataFrame(pd.read_csv(stockNo_Csv, sep = ",", header = 0))

	fig = go.Figure(data=[go.Candlestick(x=stockdata_df['Date'],
	open=stockdata_df['Open'],
	high=stockdata_df['High'],
	low=stockdata_df['Low'],
	close=stockdata_df['Close'])])
	fig.update_layout(
		title= {
			'text': quote,
			'y':0.9,
			'x':0.5,
			'xanchor': 'center',
			'yanchor': 'top'},
		font=dict(
			family='Courier New, monospace',
			size=20,
			color='#7f7f7f'
		)
	)
	fig.show()
 
 