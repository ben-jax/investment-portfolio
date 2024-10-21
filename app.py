import streamlit as st
import main
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.set_page_config(layout='wide')

st.title('Stock Portfolio')


port = main.Portfolio()

port.buy('VOO', 30, 500)
port.buy('VXUS', 20, 50)
port.buy('SCHD', 150, 20)

# creating columns for webpage, col1 and 2 are for first row, where col1 is 70% of availble space and col2 is 30%
# col 3 and 4 are for second row
col1, col2 = st.columns([0.6, 0.4])
col3, col4 = st.columns([0.6, 0.4])

# pandas df of positions, make index one so row starts at 1 not 0
df = port.get_pandas_df()
df.index = pd.RangeIndex(start=1, stop=len(df) + 1, step=1)

with col1:
    st.header('Current Holdings')
    st.dataframe(df)


# creating pie chart for col 2
labels = port.holdings.keys()
prices = port.current_value_stocks()
sizes = []

for i in range(len(prices)):
    sizes.append(prices[i] / port.market_value())

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')

with col2:
    st.pyplot(fig1)


with col3:
    st.header('Allocation by Sector')

with col4:
    pass

'''
Home page has a total of 2 rows and 4 columns, 2 columns per row
only dipslaying info on current holdings, cost value ect and pie chart representing position percentage of total portfolio

then displaying the distribution between sector, stocks, bonds, etfs, cash and other investments

Other pages will include, managing positions (adding or removing shares)
    profit will be tracked in this page

stock valuation page

dividend info page

'''


