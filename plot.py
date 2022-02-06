import streamlit as st
import pandas as pd
import numpy as np 
from plotly import express
import yfinance as yf
st.set_page_config(page_title='Stock Dashboard',
                   page_icon=':bar_chart:',
                   layout='wide'
                   )
ticker=['^nsei','tcs.ns','infy.ns','adanient.ns','irctc.ns','itc.ns']
df = yf.download(ticker,period='1y')['Adj Close']
select = st.sidebar.multiselect('select the stock',
                       options=df.columns.values,
                       default=df.columns.values)
cum_s = st.sidebar.radio('Cummulative returns',['Yes','No'])
pct = df.pct_change()
cum = (1+pct).cumprod()
if cum_s == 'Yes':
    fig = express.line(cum[select],template='presentation')
else:
    fig = express.line(df[select],template='presentation')

st.plotly_chart(fig)

