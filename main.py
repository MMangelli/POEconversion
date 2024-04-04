# import requests

# def scrape_divine_orb():
#     url = "https://poe.ninja/api/data/currencyoverview?league=Necropolis&type=Currency"
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         data = response.json()
#         for currency in data['lines']:
#             if currency['currencyTypeName'] == 'Divine Orb':
#                 receive_value = currency['receive']['value']
#                 print(f"Currency: Divine Orb\nChaos Price: {receive_value}\n")
#                 break
#         else:
#             print("Divine Orb not found in the data.")
#     else:
#         print("Failed to fetch data.")

# if __name__ == "__main__":
#     scrape_divine_orb()



import requests

def scrape_currency(currency_type):
    url = f"https://poe.ninja/api/data/currencyoverview?league=Necropolis&type=Currency"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        for currency in data['lines']:
            if currency['currencyTypeName'] == currency_type:
                receive_value = currency['receive']['value']
                print(f"Currency: {currency_type}\nChaos Orbs: {receive_value}\n")
                return
        print(f"{currency_type} not found in the data.")
    else:
        print("Failed to fetch data.")

if __name__ == "__main__":
    currency_type = input("Enter the currency type (e.g., Divine Orb): ")
    scrape_currency(currency_type)