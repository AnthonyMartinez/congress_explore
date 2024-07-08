import requests
import pandas as pd
from google.cloud import bigquery
import os
import json 

# api_key = os.environ['CONGRESS_API_KEY']
api_key = 'dTE9VbIr4rqhy502hUejkZ25yh3i3hMIwbyoMCsD' 
url = 'https://api.congress.gov/v3/bill'
def get_items(url, limit, key, obj_key):

    # set counter for logging
    times = 0
    bills = []

    # set params
    params = { 'api_key': key }

    r = requests.get(url, params=params)
    times += 1

    results = r.json()
    bills = bills + results[obj_key]

    while (len(bills) < limit):
        r = requests.get(results['pagination']['next'], params=params)
        times +=1 
        
        results = r.json()
        bills = bills + results[obj_key]
    
        # log out every 100 bills
        if times % 5 == 0:
            print(f"iteration: {times}, {len(bills)} {obj_key} loaded so far.")
    return(bills)

test = get_items(url, 1000, api_key, 'bills')

# flatten results and prepare for dataframe
data = []

for line in test:
    data.append({
        'congress': line['congress'],
        'latestAction_actionDate': line['latestAction']['actionDate'],
        'latestAction_text': line['latestAction']['text'],
        'number': line['number'],
        'originChamber': line['originChamber'],
        'originChamberCode': line['originChamberCode'],
        'title': line['title'],
        'type': line['type'],
        'updateDate': line['updateDate'],
        'updateDateIncludingText': line['updateDateIncludingText'],
        'url': line['url'],
    })



with open('bills.jsonl', 'w') as f:
    for line in data:
        f.write(json.dumps(line)+'\n')