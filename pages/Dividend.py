import streamlit as st
import yfinance as yf

st.set_page_config(layout='centered',
                   page_title='Dividend Dashboard | benjax')

top = st.container()
contents = st.container()

with top:
    col1, col2 = st.columns(2)

    with col2:
        change = st.toggle('Search Ticker')

        if change:
            ticker = st.text_input('Ticker', placeholder='Example: VOO')
        else:
            st.write('basic portfolio dividend info will go here')

    with col1:
        st.header('Dividend Dashbaord')
        if change:
            st.write('Look up dividend information by entering a ticker.')
        else:
            st.write('Your dividend dashboard, for information on your current dividends')

with contents:
    if not change:
        # chart of dividend info for portfolio
        st.header('Chart Goes Here')

        # three columns to house more information about portfolio dividends
        col3, col4, col5 = st.columns(3)

        with col3:
            st.write('info')

        with col4: 
            st.write('more info')

        with col5:
            st.write('and finally, more info')
    else:
        st.header('Chart')

        # three columns to house more information about portfolio dividends
        col3, col4, col5 = st.columns(3)

        with col3:
            st.write('info')

        with col4: 
            st.write('more info')

        with col5:
            st.write('and finally, more info')


    
    