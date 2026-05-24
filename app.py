import streamlit as st
import yfinance as yf

st.set_page_config(page_title="PennyScanner Real", layout="centered")
st.title("📈 PennyScanner Live")

# פונקציה למשיכת נתונים
def get_market_data():
    # משיכת מניות חמות (Top Gainers)
    # הערה: yfinance לא נותן סורק פני מניות מושלם, אז נביא דוגמה למניות פעילות
    tickers = ["AAPL", "AMD", "NVDA", "TSLA", "PLTR"] 
    data = []
    for t in tickers:
        stock = yf.Ticker(t)
        info = stock.info
        data.append({
            "ticker": t,
            "price": info.get('currentPrice', 0),
            "vol": info.get('volume', 0) / 1000000
        })
    return data

if st.button('רענן נתונים'):
    stocks = get_market_data()
    for s in stocks:
        st.markdown(f"""
        <div style="background:#1e2530; padding:15px; border-radius:10px; margin-bottom:10px; color:white;">
            <h3 style="margin:0;">{s['ticker']} - ${s['price']}</h3>
            <p style="margin:5px 0;">Volume: {s['vol']:.2f}M</p>
        </div>
        """, unsafe_allow_html=True)
else:
    st.write("לחץ על הכפתור כדי לטעון מניות אמיתיות מהבורסה")
