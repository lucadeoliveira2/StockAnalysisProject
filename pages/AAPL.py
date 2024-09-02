from libraries import *
from functions import *
from data_manip import *



aaplPrices, aaplVolumes, aaplReturns = stockPrices.AAPL, stockVolumes.AAPL, stockReturns.AAPL
spxPrices, spxReturns = stockPrices.SPX, stockReturns.SPX

aaplDailyVol, aaplWeeklyVol, aaplYearlyVol = myVol(aaplReturns)
spxDailyVol, spxWeeklyVol, spxYearlyVol = myVol(spxReturns)

aaplspxCorr, aaplspxSmoothCorr = myCorr(aaplReturns, spxReturns)

st.write(aaplspxCorr)
aaplspxCorr.plot()
aaplspxSmoothCorr.plot()
st.pyplot()

aaplspxBeta = myBeta(aaplYearlyVol, spxYearlyVol, aaplspxCorr, days=30)


aaplYearlyVol.plot()
spxYearlyVol.plot()
st.pyplot()