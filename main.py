import yfinance as yf
import pandas as pd

class Stock():
    def __init__(self, ticker):
        self.data = yf.Ticker(ticker)

class Portfolio():

    # Initialize our portfolio object
    # create our holdings dictionary, which will have a ticker as key and
    # the value will be a list containing shares owned and cost basis
    def __init__(self):
        self.holdings = {}

    # if we want to set our portfolio to a predetermined set of holdings for testing, experiments ect.
    def set_holdings(self, dict):
        self.holdings = dict

    # adding a position to our portfolio
    # input: stock ticker, shares purchased, price purchased at
    # updates our holding dictionary, with updated share count and cost basis (per share)
    def buy(self, stock, shares, price):
        if stock not in self.holdings:
            self.holdings[stock] = [shares, price]
        else:
            self.holdings[stock] = [self.holdings[stock][0] + shares,
                                    ((self.holdings[stock][0] * self.holdings[stock][1]) +
                                    (shares * price)) / (self.holdings[stock][0] + shares)]

    # selling a position in our portfolio
    # input: stock ticker, shares sold
    # update our holdings
    def sell(self, stock, shares):
        if stock not in self.holdings:
            return
        else:
            # handle cases where selling more shares than available or negative shares
            if shares > self.holdings[stock][0] or shares < 0:
                return
            self.holdings[stock] = [self.holdings[stock][0] - shares,
                                    self.holdings[stock][1]]
            
    # calculate the total cost for current holdings        
    def current_cost(self):
        return sum(shares * cost for shares, cost in self.holdings.values())
    
    # calculate the total market value for current holdings
    def market_value(self):
        tickers = self.holdings.keys()
        total = 0

        for ticker in tickers:
            stock = yf.Ticker(ticker)
            price = stock.history(period='1d')['Close'].iloc[-1]
            total += self.holdings[ticker][0] * price

        return total
    
    # calculate current profit and loss for this portfolio and its holding
    def profit_and_loss(self):
        return self.market_value() - self.current_cost()
    
    # calculate the current market value for a each stock
    # no input, uses self.holdings
    # returns a list that has the market value for each stock in portfolio
    def current_value_stocks(self):
        ans_list = []

        for stock in self.holdings.keys():
            ticker = yf.Ticker(stock)
            price = ticker.history(period="1d")['Close'].iloc[-1]
            ans_list.append(round(price * self.holdings[stock][0], 2))

        return ans_list 
    
    # create a pandas dataframe of holdings
    # no input, uses self.holdings and other functions
    # return a pandas data frame with ticker, shares owned, cost basis (per share)
    # market value, and profit and loss
    def get_pandas_df(self):

        # creating data frame with data from self.holdings, data that we do not have to calculate
        df = pd.DataFrame.from_dict(self.holdings, orient='index',
                                    columns=['shares', 'cost basis (per share)'])
        
        # creating market value column
        df['market value'] = self.current_value_stocks()
        
        # creating cost basis (total) column
        df['cost basis (total)'] = df['shares'] * df['cost basis (per share)']
        
        # creating profit and loss column
        df ['profit/loss'] = df['market value'] - df['cost basis (total)']

        # making ticker a column
        df.reset_index(inplace=True)
        df.rename(columns={'index': 'Ticker'}, inplace=True)

        return df
    
    '''
    To-Do:

    1. add any function to help manage portfolio

    3. complete stock class so I can have valuation tab on streamline

    '''

def test():
    port = Portfolio()
    port.buy('VOO', 30, 500)
    port.buy('VXUS', 20, 50)
    port.buy('SCHD', 150, 20)

    print(port.get_pandas_df())





