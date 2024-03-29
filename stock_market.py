import sys
sys.path.append('c:\python310\lib\site-packages')
import streamlit as st
import pandas as pd 
import yfinance as yf 
import datetime

st.title('Stock Market App')

stock = st.text_input("Give the name of stock", "GOOG")
st.write('Currently Analyzing: ', stock)

ticker_data = yf.Ticker(stock)

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Enter Start Date", datetime.date(2024,1,1))

with col2:
    end_date = st.date_input("Enter End Date", datetime.date(2024,1,31))

hist = ticker_data.history(period="1d", start=start_date, end=end_date)

st.write(hist)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Trend in Opening prices")
    st.line_chart(hist['Open'])

with col2:
    st.subheader("Trend in Closing prices")
    st.line_chart(hist['Close'])


st.subheader("Trend in Volatility prices: (High - Low)")
st.line_chart(hist['High'] - hist['Low'])