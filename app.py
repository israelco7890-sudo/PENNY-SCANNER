import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="PennyScanner Pro", layout="wide")

st.title("PennyScanner Pro")

# רשימת המניות מהקובץ שלך (תוכל להוסיף עוד)
tickers = ["AMC", "GME", "MULN", "SNDL", "PLTR", "FSR", "WISH"]

def get_live_data(ticker_list):
    data = []
    for t in tickers:
        stock = yf.Ticker(t)
        # משיכת הנתונים שמופיעים בקובץ שלך
        price = stock.fast_info.last_price
        vol = stock.fast_info.volume / 1000000
        # הערה: market_cap ו-float דורשים חישוב נוסף ב-yfinance
        data.append({"Ticker": t, "Price": price, "Volume (M)": vol})
    return pd.DataFrame(data)

if st.button('סרוק מניות'):
    df = get_live_data(tickers)
    st.table(df)
else:
    st.write("לחץ על הכפתור כדי להתחיל בסריקה")
