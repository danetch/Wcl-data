# get token
import datetime
import os.path
import json
import requests
from requests.auth import HTTPBasicAuth

def read_key(filename):
    if not os.path.isfile(filename):
        print(filename+" doesn't exist")
    f = open(filename, "rt")
    data = json.loads(f.readline())
    return data

def get_token():
    credentials = read_key("wcl.key")
    currentDate = datetime.datetime.today()
    file_exists = os.path.isfile("token.trk")
    token = ""
    if file_exists:
        print("found a token file")
        f = open("token.trk", "rt")
        data = json.loads(f.readline())
        expiryTimeStamp = data['expires']
        token = data['token']
        f.close()
        print("currentDate time stamp is ", currentDate.timestamp(), "expiry time stamp is ", expiryTimeStamp)
    if not file_exists or float(expiryTimeStamp) - currentDate.timestamp() < 0:
        print("token not there or expired, trying to retrieve a new one")
        oauth = requests.post("https://www.warcraftlogs.com/oauth/token",
                              auth=HTTPBasicAuth(credentials['key'],
                                                 credentials['secret']),
                              data={'grant_type': 'client_credentials'})
        token = "Bearer " + oauth.json()['access_token']
        delta = datetime.timedelta(seconds=oauth.json()["expires_in"] - 1000)
        trackingToken = {"token": token, "expires": str((currentDate + delta).timestamp())}
        f = open("token.trk", "wt")
        f.write(json.dumps(trackingToken))
        f.close()
    return token


def get_btoken():
    credentials = read_key("blizzard.key")
    currentDate = datetime.datetime.today()
    file_exists = os.path.isfile("btoken.trk")
    token = ""
    credentials = read_key("blizzard.key")
    if file_exists:
        print("found a blizzard token file")
        f = open("btoken.trk", "rt")
        data = json.loads(f.readline())
        expiryTimeStamp = data['expires']
        token = data['token']
        f.close()
        print("currentDate time stamp is ", currentDate.timestamp(), "expiry time stamp is ", expiryTimeStamp)
    if not file_exists or float(expiryTimeStamp) - currentDate.timestamp() < 0:
        print("btoken not there or expired, trying to retrieve a new one")
        oauth = requests.post("https://us.battle.net/oauth/token",
                              auth=HTTPBasicAuth(credentials['key'],
                                                 credentials['secret']),
                              data={'grant_type': 'client_credentials'})
        token = "Bearer " + oauth.json()['access_token']
        delta = datetime.timedelta(seconds=oauth.json()["expires_in"] - 100)
        trackingToken = {"token": token, "expires": str((currentDate + delta).timestamp())}
        f = open("btoken.trk", "wt")
        f.write(json.dumps(trackingToken))
        f.close()
    return token


