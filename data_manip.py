import pandas as pd

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

# Getting Market Cap

companyData = read_csv('sp500_companies.csv').sort_values('Symbol').set_index('Symbol')
companyMC = companyData.Marketcap
companySymbols = companyData.index
companySector = companyData.Sector

stockLastPrice = stockPrices.drop(columns='SPX').iloc[-1, :]
stockShares = np.array(companyMC) / np.array(stockLastPrice)
stockMC = stockPrices.drop(columns='SPX') * stockShares
stockMC['SPX'] = stockMC.sum(axis=1)

stockWeight = stockMC.apply(lambda x: x / stockMC['SPX'])

# Sector Data

sectorMC = stockMC.T.groupby(companySector).sum().T
sectorMC['SPX'] = sectorMC.sum(axis=1)

sectorWeight = sectorMC.apply(lambda x: x / sectorMC['SPX']).drop(columns='SPX')

# Stock Sector Weight

stockSectorWeight = pd.DataFrame(np.array(stockMC.drop(columns='SPX')) / np.array(sectorMC[companySector]))

