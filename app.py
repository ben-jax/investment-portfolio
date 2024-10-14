import streamlit as st
import main
import matplotlib.pyplot as plt
import numpy as np

st.title('Stock Portfolio')


port = main.Portfolio()

port.buy('VOO', 30, 500)
port.buy('VXUS', 20, 50)
port.buy('SCHD', 150, 20)

labels = port.holdings.keys()
sizes = []

for stock in labels:
    sizes.append(port.current_value_stock(stock) / port.market_value())

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')


st.pyplot(fig1)

