# Auto initiate fraction AI bot
import time
import requests
from datetime import datetime
import math

def sessionCheck(userid):
    sessionCheck = True
    while sessionCheck:
        sessionUrl = f"https://dapp-backend-large.fractionai.xyz/api3/session-types/live-paginated/user/{userid}?pageSize=10&pageNumber=1"
        sessionHeader = {
            'Accept': 'application/json',
            'Origin': 'https://dapp.fractionai.xyz',
            'Referer': 'https://dapp.fractionai.xyz/'
        }

        getSession = requests.get(sessionUrl, headers=sessionHeader)
        if(getSession.status_code == 200):
            respSession = getSession.json()
            statusCounts = respSession.get('statusCounts')
            liveSession = statusCounts.get('live')
            distributing = statusCounts.get('distributing_rewards')
            currentTime = datetime.now()
            formattedTime = currentTime.strftime("%Y-%m-%d %H:%M:%S")
            print("------ Session Status ------")
            print(f"+ Live         : {liveSession}")
            print(f"+ Distributing : {distributing}")
            print(f"+ Time         : {formattedTime}")
            if(liveSession == "0" and distributing == "0"):
                sessionCheck = False
                print(f"Session was free, lets run bot!")
                time.sleep(10)
            else:
                time.sleep(10)
        else:
            print('Get session failed!')
            print('Retrying...')
            time.sleep(10)

def waitCountDown(sleepTime):
    print(f'Wait for {sleepTime} second')
    waitTimes = math.ceil(sleepTime / 10)
    for m in range(sleepTime, 0, -(waitTimes)):
        print(f"{m} second left")
        time.sleep(waitTimes)


def fraction(token, userid):
    while True:
        try:
            # Get user agents
            agentUrl = f"https://dapp-backend-large.fractionai.xyz/api3/agents/user/{userid}"
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
                time.sleep(10)
            elif response.status_code != 200:
                print(f'Error {response.status_code}, run bot again')
                time.sleep(10)
                break
            elif response.status_code == 200:
                print('Success get agent!!!')

                if not agent:
                    userid = input('No agent found, please input new user ID: ')
                    token = input('No agent found, please input new token: ')
                else:
                    sumAgent = len(agent)
                    print(f"You have {sumAgent} agent.")
                    time.sleep(10)
                    for data in agent:
                        if data.get('automationEnabled') == False:
                            # initiate
                            initiateUrl = "https://dapp-backend-large.fractionai.xyz/api3/matchmaking/initiate"
                            initiateHeader = {
                                'Accept': 'application/json',
                                'Authorization': f'Bearer {token}',
                                'Origin': 'https://dapp.fractionai.xyz',
                                'Referer': 'https://dapp.fractionai.xyz/'
                            }
                            initiateBody = {
                                "userId": userid,
                                "agentId": data.get('id'),
                                "entryFees": 0.001,
                                "sessionTypeId": 1
                            }
                            ##############################################
                            err_loop = True
                            while err_loop:
                                initiate = requests.post(initiateUrl, headers=initiateHeader, json=initiateBody)
                                resp = initiate.json()
                                if initiate.status_code == 200:
                                    print("-----------------------------")
                                    print(f"+ Initiate agent {data.get('name')} success")
                                    print(f"+ Matchmaking ID: {resp.get('matchmakingId')}")
                                    print(f"+ Matchmaking Status: {resp.get('matchmakingStatus')}")
                                    currentTime = datetime.now()
                                    formattedTime = currentTime.strftime("%Y-%m-%d %H:%M:%S")
                                    print(f"+ Initiate date : {formattedTime}")
                                    err_loop = False
                                    time.sleep(10)
                                else:
                                    err_msg = resp.get('error', '')
                                    print("-----------------------------")
                                    print(f"Agent ID   : {data.get('id')}")
                                    print(f"Agent Name : {data.get('name')}")
                                    print(f"Status     : {initiate.status_code}")
                                    print(f'Message    : {err_msg}')
                                    if initiate.status_code == 400 and "Agent is in cooldown period" in err_msg:
                                        print("Initiate next agent...")
                                        err_loop = False
                                        time.sleep(10)
                                    elif initiate.status_code == 400 and "please try after 60 minutes" in err_msg:
                                        print(f"Session full, getting session in 10 minutes...")
                                        waitCountDown(600)
                                        sessionCheck(userid=userid)
                                    elif "timeout" in err_msg:
                                        print("Timeout! Retrying to initiate...")
                                        time.sleep(10)
                                    else:
                                        err_loop = False
                                        time.sleep(10)

                        else:
                            print("-----------------------------")
                            print(f"Agent {data.get('name')} is already automated, skipping....")
                            time.sleep(10)
                    
                    print('All agent running complete.')
                    waitCountDown(300)

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
