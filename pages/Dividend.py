import streamlit as st
import yfinance as yf
import pandas as pd
import main
from datetime import datetime, timedelta

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
                payout_ratio = round(stock.info.get('payoutRatio'), 2)
                price = stock.info.get('previousClose')
                payout = stock.info.get('dividendRate')
                fcf = stock.info.get('freeCashflow')
                shares = stock.info.get('sharesOutstanding')

                # calculating dividend cagr
                dividends = stock.dividends

                if not dividends.empty:
                    end = pd.Timestamp(datetime.today())
                    start = pd.Timestamp(end - timedelta(days=1825))

                    # Handle timezone if necessary (only if dividends.index has timezone)
                    if dividends.index.tz is not None:
                        end = end.tz_localize(dividends.index.tz)
                        start = start.tz_localize(dividends.index.tz)

                    filtered_dividends = dividends[(dividends.index >= start) & (dividends.index <= end)]
                    
                    if not filtered_dividends.empty:
                        start_value = filtered_dividends.iloc[0]
                        end_value = filtered_dividends.iloc[-1]
                        n_years = (end - start).days / 365.25
                        div_cagr = ((end_value / start_value) ** (1 / n_years)) - 1
                
                historic_fcf = stock.cashflow.loc['Free Cash Flow']
                historic_fcf.index = pd.to_datetime(historic_fcf.index)
                if len(historic_fcf) >= 4:
                    start_value = historic_fcf.iloc[3]
                    end_value = historic_fcf.iloc[0]  
                    n_years = len(historic_fcf) - 1
                    fcf_cagr = ((end_value / start_value) ** (1 / n_years)) - 1

    with col1:
        st.header('Dividend Dashbaord')
        if change:
            st.write('Enter a ticker to learn more dividend information about a stock.')
            st.write('This uses companies financials, so it is not intended for ETFs.')
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
            st.caption('Current starting yeild.')
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
            st.caption('Payout ratio of earnings to dividends.')
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
                            
                        {payout_ratio * 100}%

                        </div>
                    """)


        with col5:
            st.subheader('Stock Price:')
            st.caption('Stocks most recent closing price.')
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
                            
                        ${price}

                        </div>
                    """)
                
        col6, col7, col8 = st.columns(3)

        with col6:
            st.subheader('Payout:')
            st.caption('Payout per share.')
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
                            
                        ${payout}

                        </div>
                    """)
                
        with col7:
            st.subheader('Dividend CAGR:')
            st.caption('5 year dividend CAGR.')
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
                            
                        {round(div_cagr * 100, 2)}%

                        </div>
                    """)


        with col8:
            st.subheader('FCF CAGR:')
            st.caption('4 year FCF CAGR.')
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
                            
                        {round(fcf_cagr * 100, 2)}%

                        </div>
                    """)
        
            
                


    
    