import streamlit as st
import yfinance as yf

st.set_page_config(layout='wide',
                   page_title='Stock Valuations | benjax')

top = st.container()
simple = st.container()
advanced = st.container()
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
            tpe = stock.info.get('trailingPE')
            fpe = stock.info.get('forwardPE')
            de = stock.info.get('debtToEquity')
            ps = stock.info.get('priceToSalesTrailing12Months')
            ev = stock.info.get('enterpriseToEbitda')
            run = True

with simple:
    st.header('Simple Valuation Formulas:')

    col3, col4 = st.columns(2)
    

    with col3:
        st.subheader('Price to Earnings Ratio (P/E):')
        
        if run == True:
            st.write(f'Current P/E Ratio (trailing): {round(tpe, 2)}')
            st.write(f'Current P/E Ratio (forward): {round(fpe, 2)}')

        else:
            st.write('Current P/E Ratio (trailing): ')
            st.write('Current P/E Ratio (forward): ')

    with col4:
        st.subheader('Debt to Equity Ratio:')

        if run:
            st.write(f'Current Debt to Equity Ratio: {round(de, 2)}')
        else:
            st.write('Current Debt to Equity Ratio: ')

    col5, col6 = st.columns(2)

    with col5:
        st.subheader('Price to Sales Ratio')

        if run:
            st.write(f'Price to Sales Ratio: {round(ps, 2)}')
        else:
            st.write('Price to Sales Ratio: ')

    with col6:
        st.subheader('Enterprise Value to EBITDA')

        if run:
            st.write(f'Enterprise Value to EBITDA: {round(ev, 2)}')
        else:
            st.write(f'Enterprise Value to EBITDA: ')

with advanced:
    st.header('Advanced Valuation Formulas: ')
    