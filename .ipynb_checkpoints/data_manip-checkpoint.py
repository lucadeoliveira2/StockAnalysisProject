from libraries import *

stockData = read_csv('sp500_stocks_small.csv')
stockData.Date = pd.to_datetime(stockData.Date)
stockData = stockData.set_index('Date')['2014-09-02':]

# SP500 stock Data

spxData = read_csv('sp500_index.csv').rename(columns={'S&P500': "Adj Close"})
spxData.Date = pd.to_datetime(spxData.Date)
spxData['Symbol'] = 'SPX'
spxData.set_index('Date', inplace=True)
stockData = pd.concat([stockData, spxData], axis=0)

stockPrices = stockData.pivot_table('Adj Close', index=stockData.index, columns=stockData.Symbol)

stockVolumes = stockData.pivot_table('Volume', index=stockData.index, columns=stockData.Symbol)
stockReturns = stockPrices.pct_change().fillna(0)

stockCumReturns = (stockReturns + 1).cumprod(axis=0)

# Sector Data

companyData = read_csv('sp500_companies.csv')
companySymbols = companyData.Symbol
companySector = companyData.Sector
sectorData = stockPrices.drop(columns='SPX').groupby(companySector, axis=1)

