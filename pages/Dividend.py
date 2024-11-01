import streamlit as st
import yfinance as yf

st.set_page_config(layout='wide',
                   page_title='Dividend Dashboard | benjax')

top = st.container()

with top:
    col1, col2 = st.columns(2)

    with col1:
        st.title('Dividend Dashbaord')
        st.write('Your dividend dashboard, enter a ticker to the right, and all kinds of dividend metrics will be provided.')