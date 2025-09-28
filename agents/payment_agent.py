import requests

class PaymentAgent:
    def make_payment(self, amount):
        r = requests.post("http://localhost:8006/pay", json={"amount": amount})
        return r.json()
