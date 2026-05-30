import requests

url = "https://catfact.ninja/fact"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("\n🐱 RANDOM CAT FACT")
    print("-" * 40)
    print("Fact :", data["fact"])
    print("Length :", data["length"])

else:
    print("Failed to fetch data.")s