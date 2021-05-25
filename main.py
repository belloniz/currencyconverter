import requests
from flask import Flask
from flask import jsonify 

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
        "current_usd": response_data["USDBRL"]["ask"],
        "current_eur": response_data["EURBRL"]["ask"]
    }

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/convertemoeda/<amountInReal>',methods=['GET'])
def convertCurrency(amountInReal):
    currency_data = get_usd_and_eur_currency()
    amountInReal = round(float(amountInReal), 2)
    amountInUSD = round(float(currency_data["current_usd"])*float(amountInReal), 2)
    amountInEUR = round(float(currency_data["current_eur"])*float(amountInReal), 2)

    return jsonify({
        "conversao": {
            "real": amountInReal,
            "dolar": amountInUSD,
            "euro": amountInEUR,
            }
        })

if __name__ == "__main__":
    app.run()