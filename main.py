import yfinance as yf

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
    
    # calculate the current market value for a specific stock
    def current_value_stock(self, stock):
        if stock not in self.holdings.keys():
            return
        
        ticker = yf.Ticker(stock)
        price = ticker.history(period="1d")['Close'].iloc[-1]

        return price * self.holdings[stock][0]
    
    '''
    To-Do:

    1. add any function to help manage portfolio

    2. import solara or streamline to start visualizing portfolio
        charts for cost vs market value
        pie chart for total holdings (split between stocks sectors ect.)

    3. complete stock class so I can have valuation tab on streamline

    '''

def test():
    port = Portfolio()
    port.buy('VOO', 30, 500)
    port.buy('VXUS', 20, 50)
    port.buy('SCHD', 150, 20)

    print(port.current_value_stock('VOO'))
    print(port.current_value_stock('VXUS'))
    print(port.current_value_stock('SCHD'))

    print(port.current_value_stock('VOO') / port.market_value())




