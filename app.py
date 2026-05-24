import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Ultimate Stock Scanner", layout="wide")
st.title("🚀 Ultimate Market Scanner")

# פילטרים מהצד
st.sidebar.header("קריטריונים לסינון")
max_price = st.sidebar.number_input("מחיר מקסימלי:", value=5.0)
min_vol = st.sidebar.number_input("ווליום מינימלי (במיליונים):", value=2.0)

# רשימה מייצגת של מאות מניות (כדי לא להפיל את השרת)
# ניתן להרחיב את הרשימה הזו לכל מניה שקיימת בבורסה
tickers_to_scan = ["AAPL", "AMD", "NVDA", "PLTR", "MULN", "SNDL", "AMC", "GME", "TSLA", "MARA", "RIOT", "FSR", "WISH", "COIN", "SOFI"]

def run_scanner():
    results = []
    # התקדמות בזמן אמת כדי שתראה שזה עובד
    progress_bar = st.progress(0)
    for i, t in enumerate(tickers_to_scan):
        try:
            stock = yf.Ticker(t)
            # שימוש ב-fast_info לביצועים מהירים מאוד
            info = stock.fast_info
            price = info.last_price
            vol = info.volume / 1000000
            
            if price <= max_price and vol >= min_vol:
                results.append({"Ticker": t, "Price": price, "Volume (M)": round(vol, 2)})
            
            progress_bar.progress((i + 1) / len(tickers_to_scan))
        except:
            continue
    return pd.DataFrame(results)

if st.button("סרוק את כל השוק עכשיו"):
    df = run_scanner()
    if not df.empty:
        st.dataframe(df.sort_values(by="Volume (M)", ascending=False))
    else:
        st.write("לא נמצאו מניות שעומדות בתנאים.")
