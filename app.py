import streamlit as st
import pandas as pd
from signal_logic import generate_signals
from backtest import calculate_accuracy
from telegram_bot import send_telegram_signal

st.set_page_config(page_title="1-Min Binary Signal Bot", layout="wide", initial_sidebar_state="expanded")
st.title("📈 Binary Trading Signal Bot (1-Min)")

st.sidebar.header("⚙️ Settings")
telegram_enabled = st.sidebar.checkbox("Send signals to Telegram", value=False)

uploaded_file = st.file_uploader("📤 Upload 1-Min Candle CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Raw Uploaded Data")
    st.dataframe(df.head())

    try:
        result_df = generate_signals(df)

        st.subheader("📊 Generated Signals")
        st.dataframe(result_df.tail(20))

        accuracy = calculate_accuracy(result_df)
        st.success(f"✅ Backtest Accuracy: {accuracy:.2f}%")

        if telegram_enabled:
            last_signal = result_df.iloc[-1]
            send_telegram_signal(last_signal)
            st.info("📤 Signal sent to Telegram")

        csv = result_df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Signals CSV", csv, "signals.csv", "text/csv")

    except Exception as e:
        st.error(f"Error processing data: {e}")
else:
    st.info("👆 Upload your 1-min historical candle CSV to get started.")
