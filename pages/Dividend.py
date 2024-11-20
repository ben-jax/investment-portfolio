import streamlit as st
import yfinance as yf
import main

st.set_page_config(layout='centered',
                   page_title='Dividend Dashboard | benjax')

# sidebar info and styling
st.sidebar.title("Investment Dashbaord")
st.sidebar.write("Navigate tools for managing your investments and portfolio.")

for _ in range(11):
    st.sidebar.write("")

st.sidebar.subheader("Made by Ben Jacobs")
st.sidebar.markdown("""
            [![GitHub](https://img.icons8.com/ios/50/000000/github.png)](https://github.com/ben-jax)
            [![LinkedIn](https://img.icons8.com/ios/50/000000/linkedin.png)](https://www.linkedin.com/in/ben-jax/)
        """)

top = st.container()
contents = st.container()

with top:
    col1, col2 = st.columns([0.7, 0.3])

    with col2:
        change = st.toggle('Search Ticker')

        if change:
            ticker = st.text_input('Ticker', placeholder='Example: VOO')
            if ticker:
                stock = yf.Ticker(ticker.strip().upper())
                dividend = round(stock.info.get('dividendYield'), 4)
                payout_ratio = stock.info.get('payoutRatio')
                fcf = stock.info.get('freeCashflow')
        else:
            st.write('')

    with col1:
        st.header('Dividend Dashbaord')
        if change:
            st.write('Enter a ticker to learn more dividend information about a stock:')
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

    # else we are looking up dividend information for individual stocks
    else:

        # three columns to house more information about portfolio dividends
        col3, col4, col5 = st.columns(3)

        with col3:
            st.subheader('Yield:')
            if ticker:
                st.html(f"""
                    <div style="
                    border: 2px solid #FF4B4B;
                    border-radius: 10px; 
                    padding: 20px; 
                    background-color: #f0f8f5;
                    text-align: center;
                    font-size: 36px;
                    height 100px;
                    color: #333;">
                        
                    {dividend * 100}%

                    </div>
                """)

        with col4: 
            st.subheader('Payout Ratio:')
            if ticker:
                st.html(f"""
                        <div style="
                        border: 2px solid #FF4B4B;
                        border-radius: 10px; 
                        padding: 20px; 
                        background-color: #f0f8f5;
                        text-align: center;
                        font-size: 36px;
                        height: 100px;
                        color: #333;">
                            
                        {payout_ratio}

                        </div>
                    """)


        with col5:
            st.subheader('Free Cash Flow:')
            if ticker:
                st.html(f"""
                        <div style="
                        border: 2px solid #FF4B4B;
                        border-radius: 10px; 
                        padding: 20px; 
                        background-color: #f0f8f5;
                        text-align: center;
                        font-size: 28px;
                        height: 100px;
                        color: #333;">
                            
                        ${fcf:,}

                        </div>
                    """)


    
    