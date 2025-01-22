import time
import requests

def mangoFaucet(env, address):
    if(env == "devnet"):
        var_url = 'https://faucet.devnet.mangonetwork.io/gas' # Devnet
    elif(env == "testnet"):
        var_url = 'https://faucet.testnet.mangonetwork.io/gas' # Testnet
    else:
        var_url = 'https://faucet.devnet.mangonetwork.io/gas'

    url = var_url
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,id;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'chrome-extension://jiiigigdinhhgjflhljdkcelcjfmplnd',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }
    data = {
        "FixedAmountRequest": {
            "recipient": address
        }
    }

    while True:
        try:
            response = requests.post(url, headers=headers, json=data)
            print(f"Response Status Code: {response.status_code}")
            print(f"Response Body: {response.text}")
            if(response.status_code != 201):
                print("Faucet error, wait 5 minutes")
                time.sleep(360) # Wait for 5 minutes if timeout / any error code
        except Exception as e:
            print(f"An error occurred: {e}")
        
        # Wait for 1 minute
        time.sleep(60)