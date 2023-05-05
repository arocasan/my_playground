from arosecrets import arosecrets
import json
import logging
from datetime import datetime
import re
import requests
import csv
import pandas as pd
import getpass

today = datetime.today()
today = today.strftime("%Y-%m-%d")

CGRE = "\33[92m"
CEND = "\33[0m"
CRED = "\33[91m"
CBLU = "\33[34m"
CBLU2 = "\33[94m"
CYELL = "\33[93m"
CBOLD = "\33[1m"


api_token = arosecrets.PAT
org_id= arosecrets.ORG_ID
org_token = arosecrets.ORG_TOKEN
user_email = arosecrets.USER_EMAIL
site_url = arosecrets.SITE_URL

def cloud_auth():
    failed_auth = 0

    while failed_auth < 5:

        s = requests.Session()
        s.auth = (user_email,api_token)
        s.headers = {
            "Accept" : "application/json",
            "content-type" : "application/json"  
        }

        s_r = s.get(f"{site_url}/rest/api/3/myself")

        if s_r.status_code == 200:
            s_r = s.get(f"{site_url}/rest/api/3/myself")
            user_details = s_r.json()
            a_display_name = user_details["displayName"]
            print(f"Greetings {CBOLD}{CBLU2}{a_display_name}{CEND}! Have fun fetching issues on {site_url}!")

            break

            f_n = a_display_name.split()
            a_display_name = f_n[0]
        elif s_r.status_code == 401:
            failed_auth += 1

            print(f"{CRED}Unauthorized for:{CEND} {CBLU2}{site_url}{CEND}, check your credentials.")
        elif s_r.status_code == 404:
            print(f"Couldn't find the site: {CBLU2}{site_url}{CEND}, check your spelling.")
            failed_auth += 1

            print(failed_auth)
        if failed_auth == 3:
            print(f"{CYELL}Maximum tries ({failed_auth}) reached\n Exiting...")
            s.close()
            exit(f"{CYELL}Maximum tries ({failed_auth}) reached\nExiting...")


cloud_auth()




