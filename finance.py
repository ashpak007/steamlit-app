#Stock Price App

import yfinance as yf
import streamlit as st

ticker_symbol = 'AAPL'

ticker_data = yf.Ticker(ticker_symbol)

ticker_df = ticker_data.history(start = '2023-01-01',
                                end = '2025-01-01',
                                interval = '1d' )

st.dataframe(ticker_df)