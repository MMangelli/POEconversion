#////////////////////////////
#2nd Attempt pulling based off user input,  I would rather grab a list though
#May come back to using this specifically for wearOS idea
#////////////////////////////
# import requests

# def scrape_currency(currency_type):
#     url = f"https://poe.ninja/api/data/currencyoverview?league=Necropolis&type=Currency"
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         data = response.json()
#         for currency in data['lines']:
#             if currency['currencyTypeName'] == currency_type:
                
#                 #Grab Chaos Value
#                 receive_value = currency['receive']['value']
#                 #Grab 7 Day Change
#                 week_trend = int(currency['receiveSparkLine']['totalChange'])
               
#                 print(f"Currency: {currency_type}\nChaos Orbs: {receive_value}\n7 Week Trend: {week_trend}%\n")
#                 return
#         print(f"{currency_type} not found in the data.")
#     else:
#         print("Failed to fetch data.")

# if __name__ == "__main__":
#     currency_type = input("Enter the currency type (e.g., Divine Orb): ")
#     scrape_currency(currency_type)

import requests

def get_currency_types():
    url = "https://poe.ninja/api/data/currencyoverview?league=Necropolis&type=Currency"
    response = requests.get(url)
    currency_types = []
    
    if response.status_code == 200:
        data = response.json()
        for currency in data['lines']:
            currency_types.append(currency['currencyTypeName'])
    else:
        print("Failed to fetch currency types.")
    
    return currency_types

def scrape_currency(currency_type):
    url = f"https://poe.ninja/api/data/currencyoverview?league=Necropolis&type=Currency"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        for currency in data['lines']:
            if currency['currencyTypeName'] == currency_type:
                
                # Grab Chaos Value
                receive_value = round(currency['receive']['value'],2)
                
                # Grab 7 Day Change
                week_trend = int(currency['receiveSparkLine']['totalChange'])
               
                print(f"Currency: {currency_type}\nChaos Orbs: {receive_value}\n7 Week Trend: {week_trend}%\n")
                return
        print(f"{currency_type} not found in the data.")
    else:
        print("Failed to fetch data.")

if __name__ == "__main__":
    currency_types = get_currency_types()
    
    print("Available currency types:")
    for index, currency_type in enumerate(currency_types, start=1):
        print(f"{index}. {currency_type}")
    
    choice = input("Select a currency type by entering its number: ")
    try:
        choice_index = int(choice) - 1
        if 0 <= choice_index < len(currency_types):
            selected_currency = currency_types[choice_index]
            scrape_currency(selected_currency)
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")
