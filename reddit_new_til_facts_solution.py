# ! python3
# a program to check for new posts in /r/todayilearned and post them on bluesky
# https://alpscode.com/blog/how-to-use-reddit-api/

from time import sleep
import sys
import requests
from api_credentials import username, password, public_key, secret_key, bsky_username, bsky_password
from datetime import datetime, timedelta
from atproto import Client
from atproto import exceptions


# function to get oauth token
def get_oauth_token():
    base_url = "https://www.reddit.com/"
    data = {
        "grant_type": "password",
        "username": username,
        "password": password,
    }
    auth = requests.auth.HTTPBasicAuth(public_key, secret_key)
    url = base_url + "api/v1/access_token"
    headers = {"user-agent": "Karma_comparator_script by Lazy-Long-8140"}
    token = acquire_access_token(url, data, headers, auth)
    return token


def acquire_access_token(url, data, headers, auth):
    # a loop to keep trying for a connection if an exception is raised
    for retry in range(5):
        try:
            request_post = requests.post(url, data=data, headers=headers, auth=auth)
            # if no exception is raised by raise_for_status() we have successfuly gotten a response
            request_post.raise_for_status()
            if request_post.status_code == 200:
                # print(f'access token expires in {request_post.json()['expires_in']} seconds')
                return request_post.json()["access_token"], request_post.json()['expires_in']
        except requests.exceptions.HTTPError as err:
            print(f"Something went wrong with downloading the page: {err}")
            print(err.response.status_code)
            sleep(5)
        except requests.exceptions.ConnectionError as conn_err:
            print(f"something went wrong with connection: {conn_err}")
            print(conn_err.response.status_code)
            sleep(5)
    else:
        print(f"Failed connection after {retry} tries")
        exit()


def check_if_oauth_token_expired(expiry, oauth_token_birth_time):
    oauth_token_expiry = oauth_token_birth_time + timedelta(seconds=expiry)
    # if the token expiry date is in the past
    if oauth_token_expiry < datetime.now():
        return True
    else:
        return False


def get_new_til_fact(oauth_token):
    # construct the token
    token = "Bearer " + oauth_token
    api_url = "https://oauth.reddit.com"
    headers = {
        "Authorization": token,
        "User-Agent": "Karma_comparator_script by Lazy-Long-8140",
        "x-requested-with": "XMLHttpRequest",
    }
    # limit of 1 post
    payload = {
        "limit": 1,
    }
    # a loop to keep trying for a connection if an exception is raised
    for retry in range(5):
        try:
            request_get = requests.get(
                api_url + "/r/todayilearned/new",
                headers=headers,
                params=payload,
            )
            # if no exception is raised by raise_for_status() we have successfuly gotten a response
            request_get.raise_for_status()
            # no exception so break out of for loop
            break
        except requests.exceptions.HTTPError as err:
            print(f"The user does not seem to exist!: {err}")
            # print(err.response.status_code)
            sleep(5)
        except requests.exceptions.ConnectionError as conn_err:
            print(f"something went wrong with connection: {conn_err}")
            # print(conn_err.response.status_code)
            sleep(5)
    else:
        print(f"Failed connection after {retry} tries")
        exit()

    if request_get.status_code == 200:
        facts_dict = {}
        facts_dict['title'] = request_get.json()['data']['children'][0]['data']['title'].split('.')[0]
        facts_dict['link'] = request_get.json()['data']['children'][0]['data']['url']
        return facts_dict


# facts list to keep track of already seen reddit threads
facts = list()
# get the oauth token and its expiry
oauth_token, expiry = get_oauth_token()
# note down the time oauth token was created
oauth_token_birth_time = datetime.now()

while True:
    # check if oauth token is expired or not (Reddit API oauth token lasts for 24h)
    if check_if_oauth_token_expired(expiry, oauth_token_birth_time):
        print('oauth token expired, acquiring new one')
        oauth_token, expiry = get_oauth_token()
        oauth_token_birth_time = datetime.now()
    else:
        pass

    # check for a new fact
    fact = get_new_til_fact(oauth_token)
    if fact not in facts:
        facts.append(fact)
        # open a file and write the fact in the file
        with open('facts.txt', 'a') as facts_file:
            facts_file.write(f'{fact["title"]} + "-" + {fact["link"]} \n')
        # use atproto SDK to make a post on Bluesky with the title and the url of new TIL
        try:
            client = Client()
            client.login(bsky_username, bsky_password)
            client.send_post(text=f'{fact["title"]} - {fact["link"]}')
        except exceptions.BadRequestError as err:
            print(f'connection unsuccessful! {err}')

    print(facts[-1])

    # sleep for 60 seconds as to not DDOS the API
    sleep(60)