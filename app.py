import streamlit as st
import main
import matplotlib.pyplot as plt
import numpy as np

st.title('Stock Portfolio')


port = main.Portfolio()

port.buy('VOO', 30, 500)
port.buy('VXUS', 20, 50)
port.buy('SCHD', 150, 20)

st.write('Here is a table for portfolio info')

# display pandas df of positions
df = port.get_pandas_df()
st.dataframe(df)


labels = port.holdings.keys()
prices = port.current_value_stocks()
sizes = []

for i in range(len(prices)):
    sizes.append(prices[i] / port.market_value())

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')


st.pyplot(fig1)

