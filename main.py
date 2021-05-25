from flask import Flask
from flask import jsonify
from currency_api import get_usd_and_eur_currency

app = Flask(__name__)

@app.route("/")
def hello():
    return "Main page"

@app.route('/convertemoeda/<amountInReal>',methods=['GET'])
def convertCurrency(amountInReal):
    amountInReal = float(amountInReal)
    currency_data = get_usd_and_eur_currency()

    amountInUSD = currency_data["current_usd"]*amountInReal
    amountInEUR = currency_data["current_eur"]*amountInReal

    return jsonify({
        "conversao": {
            "real": amountInReal,
            "dolar": amountInUSD,
            "euro": amountInEUR,
            }
        })

if __name__ == "__main__":
    app.run()