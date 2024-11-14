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
st.sidebar.title("Investment Dashbaord")
st.sidebar.write("Navigate tools for managing your investments and portfolio.")

for _ in range(11):
    st.sidebar.write("")

st.sidebar.subheader("Made by Ben Jacobs")
st.sidebar.markdown("""
            [![GitHub](https://img.icons8.com/ios/50/000000/github.png)](https://github.com/ben-jax)
            [![LinkedIn](https://img.icons8.com/ios/50/000000/linkedin.png)](https://www.linkedin.com/in/ben-jax/)
        """)

# creating columns for webpage, col1 and 2 are for first row, where col1 is 60% of availble space and col2 is 40%
top = st.container()

for _ in range(5):
    st.write('')

linechart = st.container()
buttons = st.container()

for _ in range(5):
    st.write('')

bar = st.container()


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
# buttons show up after line chart because container was initialized after linechart container
# putting it before linechart so that the linechart container knows what is selected for time frame
with buttons:

    # days variable for line chart
    days = 365

    # added more columns for space
    col3, col4, col5, col6, col7, col8, col9 = st.columns(7)

    with col3:
        if st.button("1W", use_container_width=True):
            days = 7

    with col5:
        if st.button('1M', use_container_width=True):
            days = 30

    with col7:
        if st.button('1Y', use_container_width=True):
            days = 365

    with col9:
        if st.button('3Y', use_container_width=True):
            days = 1095

with linechart:
    sb.set(style='darkgrid')  # Ensure the Seaborn style is set for the line chart

    # Get the plotting data from the portfolio
    plotting_info = portfolio.line_chart_data(days)

    # Create a Seaborn lineplot (instead of using plt.plot)
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sb.lineplot(x=plotting_info[1][next(iter(portfolio.holdings.keys()))].index, 
                y=plotting_info[0], 
                color='b', 
                label='Portfolio Value', 
                linewidth=2,
                ax=ax3)
    
    fig3.patch.set_facecolor('#2D2D2D')
    ax3.set_facecolor('#2D2D2D')

    # Title and axis labels
    ax3.set_title('Portfolio Value Over Time', fontsize=16, color='white')
    ax3.set_xlabel('Date', fontsize=12, color='white')
    ax3.set_ylabel('Portfolio Value ($)', fontsize=12, color='white')

    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=45, color='white')
    plt.yticks(color='white')

    # Add grid and legend
    ax3.grid(True)
    ax3.legend()

    # Adjust layout to avoid clipping of labels
    plt.tight_layout()

    # Display the plot in Streamlit using st.pyplot()
    st.pyplot(fig3)

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

    plt.yticks(color='white')

    ax2.legend()

    st.pyplot(fig2)



    
    

