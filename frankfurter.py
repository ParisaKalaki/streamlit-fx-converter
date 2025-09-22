import datetime
from api import get_url
import json

BASE_URL = "https://api.frankfurter.app"

def get_currencies_list():
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the list of available currencies.
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the list of currency codes and return it as Python list.
    Otherwise it will return the value None.

    Parameters
    ----------
    None

    Returns
    -------
    list
        List of available currencies or None in case of error
    """
    url = f"{BASE_URL}/currencies"
    status_code, response_text = get_url(url)
    if status_code == 200:
        try:
            data = json.loads(response_text)
            currencies = list(data.keys())
            return currencies
        except json.JSONDecodeError:
            return None
    else:
        return None
    

def get_latest_rates(from_currency, to_currency, amount):
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the latest conversion rate between the provided currencies. 
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the latest conversion rate and the date and return them as 2 separate objects.
    Otherwise it will return the value None twice.

    Parameters
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted

    Returns
    -------
    str
        Date of latest FX conversion rate or None in case of error
    float
        Latest FX conversion rate or None in case of error
    """
    url = f"{BASE_URL}/latest?from={from_currency}&to={to_currency}&amount={amount}"
    status_code, response_text = get_url(url)
    if status_code == 200:
        try:
            data = json.loads(response_text)
            rates = data.get("rates", {})
            rate = rates.get(to_currency)
            return rate
        except json.JSONDecodeError:
            return None
    else:
        return None


    

def get_historical_rate(from_currency, to_currency, from_date, amount):
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the conversion rate for the given currencies and date
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the conversion rate and return it.
    Otherwise it will return the value None.

    Parameters
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    from_date : str
        Date when the conversion rate was recorded

    Returns
    -------
    float
        Latest FX conversion rate or None in case of error
    """
    url = f"{BASE_URL}/{from_date}?from={from_currency}&to={to_currency}&amount={amount}"
    status_code, response_text = get_url(url)
    if status_code == 200:
        try:
            data = json.loads(response_text)
            rates = data.get("rates", {})
            rate = rates.get(to_currency)
            return rate
        except json.JSONDecodeError:
            return None
    else:
        return None


def get_rate_trend(from_currency: str, to_currency: str, years: int) -> dict:
    """
    Fetches historical rates for the past N years on a quarterly basis and returns a dictionary with dates as keys and rates as values.

    Parameters
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    years : int
        Number of years in the past for which to fetch rates

    Returns
    -------
    dict
        Dictionary containing dates and their corresponding rates
    """
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=years * 365)
    url = f"{BASE_URL}/{start_date}..{end_date}?from={from_currency}&to={to_currency}&amount=1"
    status_code, response_text = get_url(url)
    if status_code == 200:
        try:
            data = json.loads(response_text)
            rates = data.get("rates", {})
            trend_data = {date: rate[to_currency] for date, rate in rates.items() if to_currency in rate}
            return trend_data
        except json.JSONDecodeError:
            return {}
    else:
        return {}