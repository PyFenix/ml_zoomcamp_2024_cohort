import requests

url = "http://localhost:8000/predict"
client = {"job": "student", "duration": 280, "poutcome": "failure"}

response = requests.post(url, json=client)
result = response.json()

probability = result["subscription_probability"]
print(f"The probability that this client will get a subscription is: {probability:.3f}")
