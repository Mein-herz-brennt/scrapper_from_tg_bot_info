import requests


token = "5669125136:AAFztoGGP94HY7aPXqqxMtZWYCO6S5MaK54"
chat_id = -799790633
data1 = {"chat_id": -799790633, "text": "jfsdfsdf"}
requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data=data1)

