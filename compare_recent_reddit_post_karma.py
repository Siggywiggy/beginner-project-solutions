#! python3
from pkgutil import resolve_name

# https://alpscode.com/blog/how-to-use-reddit-api/

import requests
from time import sleep


# function to get oauth token
def get_oauth_token():
    base_url = "https://www.reddit.com/"
    data = {
        "grant_type": "password",
        "username": "",
        "password": "",
    }
    auth = requests.auth.HTTPBasicAuth("g", "")
    url = base_url + "api/v1/access_token"
    headers = {'user-agent': 'Karma_comparator_script by Lazy-Long-8140'}
    token = try_connection(url, data, headers, auth)
    return token


def try_connection(url, data, headers, auth):
    # a loop to keep trying for a connection if an exception is raised
    for retry in range(5):
        try:
            r = requests.post(url, data=data, headers=headers, auth=auth)
            # if no exception is raised by raise_for_status() we have successfuly gotten a response
            r.raise_for_status()
            print(r.status_code)
            print(r.text)
            # return downloaded_data["access_token"]
        except requests.exceptions.HTTPError as err:
            print(f"Error {err}, retrying after 5 seconds")
            sleep(5)
    else:
        print(f"Failed connection after {retry} tries")
        exit()


def get_last_user_post(access_token, user_name):
    # construct the token
    token = "Bearer " + access_token
    api_url = "https://oauth.reddit.com"
    headers = {
        "Authorization": token,
        "User-Agent": "Karma_comparator_script by Lazy-Long-8140",
        "x-requested-with": "XMLHttpRequest",
    }

    payload = {'limit': 1, }
    response = requests.get(api_url + '/user/' + user_name + '/comments', headers=headers, params=payload)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"Something went wrong with downloading the page: {err}")
        print(err.response.status_code)
    except requests.exceptions.ConnectionError as conn_err:
        print(f"something went wrong with connecting: {conn_err}")

    if response.status_code == 200:
        print(response.txt)
        user_post = response.json()


print(get_oauth_token())

# search for subreddits matching with query "puppies", limit search to 5
'''
payload = {"q": "puppies", "limit": 5, "sort": "relevance"}
response = requests.get(api_url + "/subreddits/search", headers=headers, params=payload)
print(response.url)
response.raise_for_status()
print(response.status_code)
values = response.json()
# print(response.text)
for i in range(len(values["data"]["children"])):
    print(values["data"]["children"][i]["data"]["display_name"])

response = requests.get(api_url + "/user/No-Comfort1251/about", headers=headers)
response.raise_for_status()
print(response.url)


if response.status_code == 200:
    print(
        response.json()["data"]["name"],
        response.json()["data"]["link_karma"],
        response.json()["data"]["comment_karma"],
    )

response = requests.get(api_url + "/api/v1/me", headers=headers)

response.raise_for_status()
print(response.url)

if response.status_code == 200:
    print(response.json()["name"], response.json()["comment_karma"])
'''