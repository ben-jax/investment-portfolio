import main
import streamlit as st

port = main.Portfolio()

st.set_page_config(layout='centered')
top = st.container()
body = st.container()

with top:
    text_col, toggle_col = st.columns([0.7, 0.3])
    text_col.title('Update Holdings')
    with toggle_col:
        update = st.toggle('Set New Holdings')

with body:
    st.title('Update Your Current Holdings')
    if not update:
        st.write('Enter your ticker:')
        ticker = st.text_input('Ticker')
        shares = st.number_input('Shares Purhcased')
        price = st.number_input('Price')
        action = st.selectbox('What Would You Like To Do?', ('Buy', 'Sell'))
        update = st.button('Update')
        if update:
            if action == 'Buy':
                port.buy(ticker, shares, price)
            if action == 'Sell':
                port.sell(ticker, shares)
