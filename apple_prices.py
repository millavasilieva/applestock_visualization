import yfinance as yf
import streamlit as st

# st.markdown(
#     """
#     <style>
#     .main{
#         background-color: aliceblue;
#         }
#     <style>
#     """,
#     unsafe_allow_html=True
# )

st.write("""
## Котировки акций компании Apple.

На графиках отображены данные о котировках акций c 2010 по 2022 гг.

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'AAPL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2012-5-31', end='2022-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits


option = st.sidebar.selectbox('Цена', ('Самые высокие/низкие цены за день',
    'Цена открытия/закрытия акций', 'Объем продаж', 'Информация о компании'))

st.header(option)

if option == 'Самые высокие/низкие цены за день':
    st.subheader('Распределение цены')

    st.write("""
    ### Самая высокая цена за день
    """)
    st.line_chart(tickerDf.High)

    st.write("""
    ### Самая низкая цена за день
    """)
    st.line_chart(tickerDf.Low)

if option == 'Цена открытия/закрытия акций':
    st.subheader('Распределение цены')

    st.write("""
    ### Цена открытия акций
    """)
    st.line_chart(tickerDf.Open)

    st.write("""
    ### Цена закрытия акций
    """)
    st.line_chart(tickerDf.Close)

if option == 'Объем продаж':

    st.line_chart(tickerDf.Volume)

if option == 'Информация о компании':

    st.write(tickerData.info)


