# Auto initiate fraction AI bot
import time
import requests
from datetime import datetime
import math

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
            agent = response.json()
            if response.status_code == 401:
                token = input('Token Expired, please input new token: ')
            elif response.status_code == 400:
                print(agent.get('error'))
            elif response.status_code != 200:
                print(f'Error {response.status_code}, run bot again')
                break
            elif response.status_code == 200:
                print('Success get agent!!!')
                
                if not agent:
                    userid = input('No agent found, please input new user ID: ')
                    token = input('No agent found, please input new token: ')
                else:
                    sumAgent = len(agent)
                    timePerAgent = math.ceil(1200 / sumAgent)
                    sleepTime = 1210
                    print(f"You have {sumAgent} agent.")
                    print(f"Start run initiation every {timePerAgent} seconds.")
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
                            resp = initiate.json()
                            if initiate.status_code == 200:
                                print("-----------------------------")
                                print(f"+ Initiate agent ID {data.get('id')} success")
                                print(f"+ Matchmaking ID: {resp.get('matchmakingId')}")
                                print(f"+ Matchmaking Status: {resp.get('matchmakingStatus')}")
                                currentTime = datetime.now()
                                formattedTime = currentTime.strftime("%Y-%m-%d %H:%M:%S")
                                print(f"+ Initiate date : {formattedTime}")
                                sleepTime = sleepTime - timePerAgent
                                print(f"Waiting {timePerAgent} second...")
                                time.sleep(timePerAgent)
                            else:
                                print("-----------------------------")
                                print(f"Agent ID   : {data.get('id')}")
                                print(f"Agent Name : {data.get('name')}")
                                print(f'Message    : {resp}')
                        else:
                            print("-----------------------------")
                            print(f"Agent {data.get('name')} is already automated, skipping....")

                    print('All initiate complete.')
                    print(f'Wait for {sleepTime} second')
                    waitTimes = math.ceil(sleepTime / 5)
                    for m in range(sleepTime, 0, -(waitTimes)):
                        print(f"{m} second left")
                        time.sleep(waitTimes)

        except Exception as e:
            print(f"Error occurred, stop running bot: {e}")

def checkUserId(sessionId):
    url = f"https://dapp-backend-large.fractionai.xyz/api2/session-messages/session/{sessionId}"
    header = {
        'Accept': 'application/json',
        'Origin': 'https://dapp.fractionai.xyz',
        'Referer': 'https://dapp.fractionai.xyz/'
    }

    response = requests.get(url, headers=header)
    res = response.json()
    usr = res.get('participantScores')
    for user in usr:
        print("-----------------------------")
        print(f"+ Agent ID   : {user.get('agentId')}")
        print(f"+ User ID    : {user.get('userId')}")
        print(f"+ Agent Name : {user.get('agentName')}")
        print(f"+ Score      : {user.get('score')}")
        print(f"+ Rank       : {user.get('rank')}")
