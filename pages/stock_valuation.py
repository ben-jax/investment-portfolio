import streamlit as st
import yfinance as yf

st.set_page_config(layout='wide',
                   page_title='Stock Valuations | benjax')

top = st.container()
body = st.container()

with top:
    col1, col2 = st.columns(2)

    with col1:
        st.title('Stock Valuation')
        st.write('''
                A stock valuation tool, where you enter a ticker for a stock and
                the intrinsic value of the stock is calculated using multiple different 
                intrinsic value formulas and yfinance api.
                 ''')

    with col2:
        st.subheader('Enter a stock ticker to be valued: ')
        ticker = st.text_input('Ticker', placeholder='Example: VOO')
        enter = st.button('Enter', use_container_width=True)