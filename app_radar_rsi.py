
import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Radar RSI", layout="centered")

st.title("Radar RSI - Sinais de Compra e Venda")
st.markdown("Digite o código do ativo (ex: PETR4.SA, AAPL, BTC-USD) e veja o RSI atual com sugestão de sinal.")

ticker = st.text_input("Ativo", "PETR4.SA")

if ticker:
    try:
        df = yf.download(ticker, period="3mo")
        df['RSI'] = 100 - (100 / (1 + df['Close'].pct_change().rolling(14).mean() / df['Close'].pct_change().rolling(14).std()))
        rsi_atual = df['RSI'].iloc[-1]
        data_ult = df.index[-1].strftime('%d/%m/%Y')

        if rsi_atual < 30:
            sinal = 'COMPRA'
            cor = 'green'
        elif rsi_atual > 70:
            sinal = 'VENDA'
            cor = 'red'
        else:
            sinal = 'NEUTRO'
            cor = 'orange'

        st.markdown(f"**RSI ({data_ult}):** `{rsi_atual:.2f}`")
        st.markdown(f"**Sinal sugerido:** :{cor}[{sinal}]")

    except Exception as e:
        st.error(f"Erro ao buscar dados: {e}")
