
def round_rate(rate):
    """
    Function that will round an input float to 4 decimals places.

    Parameters
    ----------
    rate: float
        Rate to be rounded

    Returns
    -------
    float
        Rounded rate
    """
    return round(rate, 4)

    

def reverse_rate(rate):
    """
    Function that will calculate the inverse rate from the provided input rate.
    It will check if the provided input rate is not equal to zero.
    If it not the case, it will calculate the inverse rate and round it to 4 decimal places.
    Otherwise it will return zero.

    Parameters
    ----------
    rate: float
        FX conversion rate to be inverted

    Returns
    -------
    float
        Inverse of input FX conversion rate
    """
    if rate != 0:
        return round(1 / rate, 4)
    else:
        return 0.0
    
    
def format_output(date, from_currency, to_currency, rate, amount):
    """
    Function that will format the text to be displayed in the Streamlit app.

    Parameters
    ----------
    date: str
        Date of the conversion rate
    from_currency: str
        Origin currency code
    to_currency: str
        Destination currency code
    rate: float
        Conversion rate
    amount: float
        Amount to be converted

    Returns
    -------
    str
        Formatted text for display
    """
    converted_amount = round_rate(rate * amount)
    inverse_rate = reverse_rate(rate)
    output = (
        f"Date: {date}\n"
        f"Latest Rate ({from_currency} → {to_currency}): {round_rate(rate)}\n"
        f"Converted Amount: {converted_amount} {to_currency}\n"
        f"Inverse Rate ({to_currency} → {from_currency}): {inverse_rate}"
    )
    return output
   