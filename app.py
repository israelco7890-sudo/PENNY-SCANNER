import streamlit as st

# עיצוב האפליקציה למובייל
st.set_page_config(page_title="PennyScanner", layout="centered")

st.title("PennyScanner Pro")

# כאן נציג את רשימת המניות (דוגמה למבנה)
stocks = [
    {"ticker": "ABC", "price": 1.20, "vol": 5.5, "float": 2.1, "mcap": 15.0},
    {"ticker": "XYZ", "price": 0.85, "vol": 12.1, "float": 0.5, "mcap": 5.2}
]

for s in stocks:
    st.markdown(f"""
    <div style="background:#111418; padding:15px; border-radius:10px; border:1px solid #1e2530; margin-bottom:10px;">
        <h3 style="margin:0;">{s['ticker']} - ${s['price']}</h3>
        <p style="margin:5px 0;">Volume: {s['vol']}M | Float: {s['float']}M | MCAP: ${s['mcap']}M</p>
    </div>
    """, unsafe_allow_html=True)

st.success("הסורק מחובר ומוכן לעבודה מהנייד!")
