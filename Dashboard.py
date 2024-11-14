import main
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb

st.set_page_config(layout='wide', 
                   page_title='Investment Portfolio | benjax')

st.title('Stock Portfolio')

if 'port' not in st.session_state:
    st.session_state.port = main.Portfolio()

portfolio = st.session_state.port

if (len(portfolio.holdings.keys()) == 0):
    portfolio.buy('VOO', 30, 500)
    portfolio.buy('VXUS', 20, 50)
    portfolio.buy('SCHD', 150, 20)

# sidebar info and styling

# creating columns for webpage, col1 and 2 are for first row, where col1 is 60% of availble space and col2 is 40%
top = st.container()
bar = st.container()
linechart = st.container()

with top:
    col1, col2 = st.columns([0.6, 0.4])

    # pandas df of positions, make index one so row starts at 1 not 0
    df = portfolio.get_pandas_df()
    df.index = pd.RangeIndex(start=1, stop=len(df) + 1, step=1)

    with col1:
        st.header('Current Holdings')
        st.dataframe(df)

    # creating pie chart for col 2
    sb.set(style='darkgrid')
    colors = sb.color_palette('pastel')

    labels = portfolio.holdings.keys()
    prices = portfolio.current_value_stocks()
    sizes = []

    for i in range(len(prices)):
        sizes.append(prices[i] / portfolio.market_value())

    fig1, ax1 = plt.subplots(facecolor='#2D2D2D')
    ax1.pie(sizes, autopct='%1.1f%%', startangle=90, colors=colors, wedgeprops={'edgecolor' : 'black'})
    ax1.axis('equal')
    ax1.legend(labels=labels)

    with col2:
        st.pyplot(fig1)


with bar:
    # creating bar chart for cost vs value
    fig2, ax2 = plt.subplots()

    fig2.patch.set_facecolor('#2D2D2D')
    ax2.set_facecolor('#2D2D2D')

    width = 0.25
    index = range(len(df))

    bar_one = ax2.bar(index, df['market value'], width, label='Market Value')
    bar_two = ax2.bar([i + width for i in index], df['cost basis (total)'], width, label='Cost')

    ax2.set_xlabel('Stock', color='white')
    ax2.set_ylabel('Value ($)', color='white')
    ax2.set_title('Market Value vs Cost For Each Holding', color='white')

    ax2.set_xticks([i + width / 2 for i in index])
    ax2.set_xticklabels(df['ticker'], color='white')

    ax2.legend()

    st.pyplot(fig2)

with linechart:
    sb.set(style='darkgrid')  # Ensure the Seaborn style is set for the line chart

    # Get the plotting data from the portfolio
    plotting_info = portfolio.line_chart_data()

    # Create a Seaborn lineplot (instead of using plt.plot)
    plt.figure(figsize=(10, 6))
    sb.lineplot(x=plotting_info[1][next(iter(portfolio.holdings.keys()))].index, 
                y=plotting_info[0], 
                marker='o', 
                color='b', 
                label='Portfolio Value', 
                linewidth=2)

    # Title and axis labels
    plt.title('Portfolio Value Over Time', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Portfolio Value ($)', fontsize=12)

    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=45)

    # Add grid and legend
    plt.grid(True)
    plt.legend()

    # Adjust layout to avoid clipping of labels
    plt.tight_layout()

    # Display the plot in Streamlit using st.pyplot()
    st.pyplot(plt)

    
    

