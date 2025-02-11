import requests

#Get Your API key from https://www.exchangerate-api.com
API_KEY = "Place key here"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

def get_exchange_rate(base_currency, target_currency):
    """Fetches exchange rate from API"""
    url = BASE_URL + base_currency
    response = requests.get(url)
    data = response.json()
    
    if response.status_code != 200:
        return None, f"Error: {data.get('error-type', 'Unknown error')}"
    
    rates = data.get("conversion_rates", {})
    return rates.get(target_currency), None

def convert_currency(amount, base_currency, target_currency):
    rate, error = get_exchange_rate(base_currency, target_currency)
    
    if error:
        return None, error
    
    converted_amount = amount * rate
    return converted_amount, None
