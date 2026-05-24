import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="PennyScanner Pro", layout="wide")
st.title("🚀 PennyScanner Dynamic Scanner")

# --- הגדרות משתמש בסרגל הצד ---
st.sidebar.header("סנן מניות")
max_price = st.sidebar.number_input("מחיר מקסימלי:", value=5.0)
min_volume = st.sidebar.number_input("ווליום מינימלי (במיליונים):", value=1.0)

# --- כאן הקסם: רשימת המניות היא כבר לא קבועה ---
# אנחנו נמשוך רשימה דינמית (כאן אפשר להחליף ברשימה של אלפי מניות)
# כרגע נשתמש בדוגמה של מניות פני נפוצות, אבל אפשר להרחיב את זה
dynamic_tickers = ["AMC", "MULN", "SNDL", "WISH", "PLTR", "FSR", "BBBY", "RIOT", "MARA"]

def scan_market():
    scanned_data = []
    for ticker in dynamic_tickers:
        stock = yf.Ticker(ticker)
        # משיכת נתונים מהירה
        info = stock.fast_info
        price = info.last_price
        volume = info.volume / 1000000
        
        # סינון לפי הקריטריונים שלך
        if price <= max_price and volume >= min_volume:
            scanned_data.append({
                "Ticker": ticker, 
                "Price": f"${price:.2f}", 
                "Volume (M)": f"{volume:.2f}"
            })
    return pd.DataFrame(scanned_data)

if st.button("סרוק שוק עכשיו"):
    df = scan_market()
    if not df.empty:
        st.table(df)
    else:
        st.write("לא נמצאו מניות שעומדות בקריטריונים כרגע.")
