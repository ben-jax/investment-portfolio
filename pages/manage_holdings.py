import main
import streamlit as st

# imported main to make sure the format for the set holdings and buy function worked
# need to figure out how to get the same portfolio linked between all sites
# inputs must only work from data inputed on site (for now)

portfolio = st.session_state.port

# Centered layout of page, not as much wide stuff to put on here
st.set_page_config(layout='centered',
                   page_title='Manage Holdings | benjax')

# two containers, one for top (title toggle button), one for body (inputs and buttons)
top = st.container()
body = st.container()

# adding session state information for inputed info
if 'ticker' not in st.session_state:
    st.session_state.ticker = ''

if 'shares' not in st.session_state:
    st.session_state.shares = 0

if 'price' not in st.session_state:
    st.session_state.price = 0

if 'positions' not in st.session_state:
    st.session_state.positions = []

# top container things
with top:
    # two columns in top container, text for text (70%) toggle for toggle button (30%)
    text_col, toggle_col = st.columns([0.7, 0.3])

    with text_col:
        st.title('Manage Positions')
        st.write('Buy and sell positions in your portfolio or flip the toggle to set a new portfolio.')

    with toggle_col:
        change = st.toggle('Set New Holdings')

# body container (input fields and buttons)
with body:
    st.title('Update Your Current Holdings')

    # change holdings toggle
    if not change:
        st.write('Enter your ticker:')
        ticker = st.text_input('Ticker', placeholder='Example: VOO')
        shares = st.number_input('Shares Purhcased', placeholder=0)
        price = st.number_input('Price', placeholder=0)
        action = st.selectbox('What Would You Like To Do?', ('Buy', 'Sell'))

        # update button
        update = st.button('Update', use_container_width=True)

        if update:
            if action == 'Buy':
                portfolio.buy(ticker, shares, price)
            if action == 'Sell':
                portfolio.sell(ticker, shares)

    # set holdings toggle            
    else:
        # two columns (equal size), values to be in new portfolio, and the updated column which shows updates
        # does not allow you to remove, maybe a feature to add
        add_col, update_col = st.columns(2)

        with add_col:
            st.write('Enter your ticker:')
            ticker_entered = st.text_input('Ticker')
            shares_entered = st.number_input('Shares Purhcased')
            price_entered = st.number_input('Price (Cost Basis)')
            add = st.button('Add Position', use_container_width=True)

            # if they add the inputed values put it in the session state to be printed later down
            # else keep them the same
            if add:
                st.session_state.ticker = ticker_entered
                st.session_state.shares = shares_entered
                st.session_state.price = price_entered
                st.session_state.positions.append([ticker_entered, [shares_entered, price_entered]]) 
            else:
                st.session_state.ticker = ''
                st.session_state.shares = 0
                st.session_state.price = 0

        # second update button
        update_two = st.button('Update Holdings', use_container_width=True)

        # adding elements to update column
        with update_col:

            st.write('Current Added Holdings:')

            # if we update then we do the set holdings function from main.py
            # we get values from postitions in session state
            if update_two:
                temp_dict = {}
                for postion in st.session_state.positions:
                    temp_dict[postion[0]] = [postion[1][0], postion[1][1]]
                portfolio.set_holdings(temp_dict)

                # be sure to clear the positions afterwards
                st.session_state.positions.clear()

            # text to be printed after we add something, but haven't updated yet
            # this is required to be rendered after we check if the update has been pressed
            for position in st.session_state.positions:
                st.write(f'* {position[0]}: {position[1][0]} @ ${position[1][1]} a share')

        
            


