import requests

def get_usd_and_eur_currency():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL"

    payload={}
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic Og=='
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    response_data = response.json()

    return {
        "current_usd": format_currency(response_data["USDBRL"]["ask"]),
        "current_eur": format_currency(response_data["EURBRL"]["ask"]),
    }

def format_currency(amount):
    amount = round(float(amount), 2)
    return amount
    