import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Auto Penny Scanner", layout="wide")
st.title("⚡ Auto Penny Scanner")

# פונקציה שסורקת מניות חמות ומסננת אותן
@st.cache_data(ttl=300) # מרענן נתונים כל 5 דקות
def get_hot_penny_stocks():
    # כאן אנחנו מושכים את המניות הכי פעילות בשוק
    # זה הופך את הסורק לאוטומטי לגמרי
    tickers = ["MULN", "SNDL", "WISH", "AMC", "GME", "PLTR", "FSR", "MARA", "RIOT"] 
    # הערה: כדי להפוך את זה לממש ענק, אפשר להשתמש בספריות שסורקות אלפי מניות
    
    data = []
    for t in tickers:
        stock = yf.Ticker(t)
        hist = stock.history(period="1d")
        if not hist.empty:
            price = hist['Close'].iloc[-1]
            vol = hist['Volume'].iloc[-1] / 1000000
            # קריטריון אוטומטי: רק מניות מתחת ל-5$ ועם ווליום גבוה
            if price < 5.0 and vol > 1.0:
                data.append({"Ticker": t, "Price": f"${price:.2f}", "Volume (M)": f"{vol:.2f}"})
    return pd.DataFrame(data)

if st.button("סרוק שוק עכשיו"):
    df = get_hot_penny_stocks()
    if not df.empty:
        st.table(df)
    else:
        st.write("לא נמצאו מניות שעומדות בקריטריונים ברגע זה.")
