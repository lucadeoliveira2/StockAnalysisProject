from libraries import *

def myVol(myStockReturns, days=30, minPeriods=10):

    stockDailyVol = myStockReturns.rolling(days, min_periods=minPeriods).std()
    stockWeeklyVol = stockDailyVol / (np.sqrt(1/52))
    stockYearlyVol = stockDailyVol / (np.sqrt(1/252))

    return stockDailyVol, stockWeeklyVol, stockYearlyVol

def myCorr(stock1Returns, stock2Returns, returnDays=30, corrDays=252, minPeriods1=10, minPeriods2=10):

    corrCoef = stock1Returns.rolling(returnDays, minPeriods1).corr(stock2Returns)
    smoothCorrCoef = corrCoef.rolling(corrDays, minPeriods2).mean()

    return corrCoef, smoothCorrCoef

def myBeta(stock1Vol, stock2Vol, stockCorr, days=252, smooth=True, plot=True):

    stockBeta = stockCorr * (stock1Vol/stock2Vol)
    smoothStockBeta = stockBeta.rolling(days).mean()

    if smooth:
        if plot:
            smoothStockBeta.plot()
            st.pyplot()
        return smoothStockBeta

    else:
        if plot:
            stockBeta.plot()
            st.pyplot()
        return stockBeta