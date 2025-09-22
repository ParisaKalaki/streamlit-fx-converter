import streamlit as st
import datetime
import pandas as pd

from frankfurter import get_currencies_list, get_latest_rates, get_historical_rate, get_rate_trend
from currency import round_rate


# App title
st.title("FX Converter")

# Fetch available currencies
currencies = get_currencies_list()
if not currencies:
    st.error("Error fetching currencies. Please try again later.")
    st.stop()

# Latest Rate Form
with st.form("latest_rate_form"):
    amount = st.number_input("Enter the amount to be converted", min_value=0.0, value=1.0, step=0.01)
    from_currency = st.selectbox("From Currency", options=currencies, index=currencies.index("USD") if "USD" in currencies else 0)
    to_currency = st.selectbox("To Currency", options=currencies, index=currencies.index("EUR") if "EUR" in currencies else 0)
    submit_latest = st.form_submit_button("Get Latest Rate")

    if submit_latest:
        latest_rate = get_latest_rates(from_currency, to_currency, 1.0)
        if latest_rate is not None:
            rounded_rate = round_rate(latest_rate)
            converted_amount = round_rate(latest_rate * amount)
            inverse_rate = round_rate(1 / latest_rate)

            date = datetime.date.today().strftime("%Y-%m-%d")
            st.success(f"The conversion rate on {date} from {from_currency} to {to_currency} was {rounded_rate}. " \
        f"So {amount} in {from_currency} corresponds to {converted_amount} in {to_currency}. " \
        f"The inverse rate was {inverse_rate}.")
        
            
            st.subheader("Rate Trend over the Last 3 years")
            trend_data = get_rate_trend(from_currency, to_currency, years=3)
            if trend_data:
                import pandas as pd
                df = pd.DataFrame(list(trend_data.items()), columns=["Date", "Rate"])
                df["Date"] = pd.to_datetime(df["Date"])
                df = df.sort_values("Date")
                st.line_chart(df.set_index("Date")["Rate"])
            else:
                st.warning("Could not fetch historical trend data.")
        else:
            st.error("Error fetching the latest rate. Please check your currencies or internet connection.")

# Historical Rate Form
with st.form("historical_rate_form"):
    date = st.date_input("Select a date for historical rates:", value=datetime.date.today(), max_value=datetime.date.today())
    submit_hist = st.form_submit_button("Conversion Rate")

    if submit_hist:
        st.subheader("Conversion Rate")
        historical_rate = get_historical_rate(from_currency, to_currency, date.strftime("%Y-%m-%d"), 1.0)
        if historical_rate is not None:
            rounded_rate = round_rate(historical_rate)
            converted_amount = round_rate(historical_rate * amount)
            inverse_rate = round_rate(1 / historical_rate)

            st.success(f"The conversion rate on {date} from {from_currency} to {to_currency} was {rounded_rate}. " \
        f"So {amount} in {from_currency} corresponds to {converted_amount} in {to_currency}. " \
        f"The inverse rate was {inverse_rate}.")

        else:
            st.error("Error fetching historical rate. Please check your currencies or date.")

