import requests
import random
from flask import Flask, request

TOKEN = "8602608228:AAE9aaUNGtH7jKmpxusQwdYtFPUjUMa-g7g"

app = Flask(__name__)

@app.route("/", methods=["POST"])

def webhook():

    data = request.json

    if "message" in data:

        chat_id = data["message"]["chat"]["id"]

        text = data["message"].get("text","")

        if text == "/start":

            gold = requests.get(
                "https://api.gold-api.com/price/XAU"
            ).json()

            harga = gold["price"]

            signal = random.choice(["BUY","SELL"])

            if signal == "BUY":
                tp = harga + 15
                sl = harga - 10
            else:
                tp = harga - 15
                sl = harga + 10

            pesan = f"""
🔥 XAUUSD LIVE SIGNAL 🔥

SIGNAL : {signal}

ENTRY : {harga}

TP : {round(tp,2)}

SL : {round(sl,2)}
"""

            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

            requests.post(url, data={
                "chat_id": chat_id,
                "text": pesan
            })

    return "ok"

app.run(host="0.0.0.0", port=3000)
