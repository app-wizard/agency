# pylint: disable=no-member
import requests
from django.conf import settings

def get_access_token():
    """
    Retrieves an access token for the PayPal API using the client credentials grant type.

    Returns:
        str: The access token for the PayPal API.
    """
    data = {
        "grant_type": "client_credentials",
        # "client_id": "Aer6-5735-4553-4565-8573",
        # "client_secret": "<KEY>"
    }

    headers = {
        "Accept": "application/json",
        "Accept-Language": "en_US",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    client_id = settings.CLIENT_ID
    client_secret = settings.CLIENT_SECRET
    url = "https://api.sandbox.paypal.com/v1/oauth2/token"

    r = requests.post(
        url, auth=(client_id, client_secret), data=data, headers=headers, timeout=10
    ).json()
    access_token = r["access_token"]
    return access_token


def cancel_subscription_paypal(access_token, sub_id):
    """
    Cancels the specified subscription in PayPal.

    Args:
        access_token (str): The access token for the PayPal API.
        sub_id (str): The ID of the subscription to cancel.

    Returns:
        None
    """
    bearer_token = "Bearer " + access_token
    headers = {"Authorization": bearer_token, "Content-Type": "application/json"}

    url = (
        "https://api.sandbox.paypal.com/v1/billing/subscriptions/" + sub_id + "/cancel"
    )

    r = requests.post(url, headers=headers, timeout=10)
    print(r.status_code)

def get_curent_subscription_paypal(access_token, sub_id):
    """
    Retrieves the current subscription plan ID for the specified subscription ID.
    
    Args:
        access_token (str): The access token for the PayPal API.
        sub_id (str): The ID of the subscription to retrieve.
    
    Returns:
        str: The ID of the current subscription plan, or None if the request fails.
    """
    bearer_token = 'Bearer '+ access_token
    headers = {
        "Authorization": bearer_token,
        "Content-Type": "application/json"
    }

    url = f'https://api.sandbox.paypal.com/v1/billing/subscriptions/{sub_id}'
    r = requests.get(url, headers=headers, timeout=10)

    if r.status_code == 200:
        subscription_data = r.json()
        curent_plan_id = subscription_data.get("plan_id")
        return curent_plan_id
    else:
        print("Fail to get subscription")
        return None

