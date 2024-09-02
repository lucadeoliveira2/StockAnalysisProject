import pandas as pd
from pandas import *
import streamlit as st

st.write('hello')
st.write('he;;0')

df = read_csv('sp500_stocks.csv', sep=',')
st.write(df)#