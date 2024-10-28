import streamlit as st
import yfinance as yf

st.set_page_config(layout='wide',
                   page_title='Stock Valuations | benjax')

top = st.container()
body = st.container()
run = False

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
        st.subheader('Enter a stock (no index funds) ticker to be valued: ')
        ticker = st.text_input('Ticker', placeholder='Example: VOO')
        enter = st.button('Enter', use_container_width=True)
        if enter:
            stock = yf.Ticker(f'{ticker.strip().upper()}')
            pe = stock.info.get('trialingPE')
            run = True

with body:
    col3, col4 = st.columns(2)
    st.header('Simple Valuation Formulas:')

    with col3:
        st.subheader('Price to Earnings Ratio (P/E):')
        
        if run == True:
            st.write(f'Current P/E Ratio: {pe}')
        else:
            st.write('Current P/E Ratio: ')

    with col4:
        st.subheader('')