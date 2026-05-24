import streamlit as st
import yfinance as yf

st.set_page_config(page_title="PennyScanner Real", layout="centered")
st.title("📈 PennyScanner Live")

# הוספת "Caching" כדי לא להפציץ את השרת בבקשות
@st.cache_data(ttl=3600) # שומר את הנתונים לשעה כדי למנוע חסימה
def get_market_data():
    tickers = ["AAPL", "AMD", "NVDA", "TSLA", "PLTR"] 
    data = []
    for t in tickers:
        stock = yf.Ticker(t)
        # שימוש ב-fast_info לעיתים חוסך את שגיאת ה-Rate Limit
        info = stock.fast_info
        data.append({
            "ticker": t,
            "price": info.last_price,
            "vol": info.volume / 1000000
        })
    return data

if st.button('רענן נתונים'):
    try:
        stocks = get_market_data()
        for s in stocks:
            st.markdown(f"""
            <div style="background:#1e2530; padding:15px; border-radius:10px; margin-bottom:10px; color:white;">
                <h3 style="margin:0;">{s['ticker']} - ${s['price']:.2f}</h3>
                <p style="margin:5px 0;">Volume: {s['vol']:.2f}M</p>
            </div>
            """, unsafe_allow_html=True)
    except Exception as e:
        st.error("השרת עמוס מדי כרגע, נסה שוב בעוד דקה.")
else:
    st.write("לחץ על הכפתור כדי לטעון נתונים מהבורסה")
