# Auto initiate fraction AI bot
import time
import requests

def fraction(token, userid):
    while True:
        try:
            # Get user agents
            agentUrl = f"https://dapp-backend-large.fractionai.xyz/api2/agents/user/{userid}"
            agentHeaders = {
                'Accept': 'application/json',
                'Authorization': f'Bearer {token}',
                'Origin': 'https://dapp.fractionai.xyz',
                'Referer': 'https://dapp.fractionai.xyz/'
            }
            ##############################################
            print("Getting agent.....")
            response = requests.get(agentUrl, headers=agentHeaders)
            if response.status_code == 403:
                userid = input('Token Expired, please input new user ID: ')
                token = input('Token Expired, please input new token: ')
            elif response.status_code != 200:
                print(f'Error {response.status_code}, run bot again')
                break
            elif response.status_code == 200:
                print('Success get agent!!!')
                agent = response.json()
                
                if not agent:
                    userid = input('No agent found, please input new user ID: ')
                    token = input('No agent found, please input new token: ')
                else:
                    for data in agent:
                        if data.get('automationEnabled') == False:
                            # initiate
                            initiateUrl = "https://dapp-backend-large.fractionai.xyz/api2/matchmaking/initiate"
                            initiateHeader = {
                                'Accept': 'application/json',
                                'Authorization': f'Bearer {token}',
                                'Origin': 'https://dapp.fractionai.xyz',
                                'Referer': 'https://dapp.fractionai.xyz/'
                            }
                            initiateBody = {
                                "userId": userid,
                                "agentId": data.get('id'),
                                "entryFees": 0.0001,
                                "sessionTypeId": 1
                            }
                            ##############################################

                            initiate = requests.post(initiateUrl, headers=initiateHeader, json=initiateBody)
                            if initiate.status_code == 200:
                                resp = initiate.json()
                                print(f"Initiate agent ID {data.get('id')} success")
                                print(f"Matchmaking ID: {resp.get('matchmakingId')}")
                                print(f"Matchmaking Status: {resp.get('matchmakingStatus')}")
                            else:
                                print(f"Error initiating agent ID {data.get('id')}, skipping to the next one.")
                        else:
                            print(f"Agent ID {data.get('id')} is already automated, skipping.")

                    print('All complete, sleeping for 21 minutes...')
                    
                    for m in range(21, 0, -1):
                        print(f"{m} minute left")
                        time.sleep(60)
        except Exception as e:
            print(f"Error occurred, restarting bot: {e}")