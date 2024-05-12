import requests
import json 

from django.conf import settings

from . models import Subscription

def get_access_token():
    data = {
        "grant_type": "client_credentials",
        # "client_id": "Aer6-5735-4553-4565-8573",
        # "client_secret": "<KEY>"
    }

    headers = {
        "Accept": "application/json",
        "Accept-Language": "en_US",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    client_id = settings.CLIENT_ID
    client_secret = settings.CLIENT_SECRET
    url = 'https://api.sandbox.paypal.com/v1/oauth2/token'

    r = requests.post(url, auth=(client_id,client_secret), data=data, headers=headers).json()
    access_token = r['access_token']
    return access_token

def cancel_subscription_paypal(access_token,subID):
    bearer_token = 'Bearer '+ access_token
    headers = {
        "Authorization": bearer_token,
        "Content-Type": "application/json"
    }

    url = 'https://api.sandbox.paypal.com/v1/billing/subscriptions/'+subID+'/cancel'

    r = requests.post(url, headers=headers)
    print(r.status_code)

def update_subscription_paypal(access_token,subID):
    bearer_token = 'Bearer '+ access_token
    headers = {
        "Authorization": bearer_token,
        "Content-Type": "application/json"
    }

    subDetails = Subscription.objects.get(paypal_subscription_id=subID)
    curent_sub_plan = subDetails.subscription_plan
    if curent_sub_plan == 'Standart':
        new_sub_plan_id = 'P-6HV61277AS102824BMY3JD6Q' # to Premium 
    elif curent_sub_plan == 'Premium':
        new_sub_plan_id = "P-1BJ56547XC2219323MY3JDHA" # to Standart

    url = 'https://api.sandbox.paypal.com/v1/billing/subscriptions/'+subID+'/revise'

    revision_data = {
        "plan_id": new_sub_plan_id
    }

    r = requests.post(url, headers=headers, data=json.dumps(revision_data))
    response_data = r.json()
    print(response_data)
    approve_link = None
    for link in response_data.get('links',[]):
        if link.get('rel') == 'approve':
            approve_link = link.get('href')

    if r.status_code == 200 and approve_link:
        print("OK link: ",approve_link)
        return approve_link
    else:
        print("Error")
        return None
    
def get_curent_subscription_paypal(access_token, subID):
    bearer_token = 'Bearer '+ access_token
    headers = {
        "Authorization": bearer_token,
        "Content-Type": "application/json"
    }

    url = f'https://api.sandbox.paypal.com/v1/billing/subscriptions/{subID}'
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        subscription_data = r.json()
        curent_plan_id = subscription_data.get('plan_id')
        return curent_plan_id
    else:
        print("Fail to get subscription")
        return None

