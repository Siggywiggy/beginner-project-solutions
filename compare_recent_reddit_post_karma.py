#! python3

# https://alpscode.com/blog/how-to-use-reddit-api/

import requests
from time import sleep

base_url = "https://www.reddit.com/"
data = {
    "grant_type": "password",
    "username": "",
    "password": "",
}

auth = requests.auth.HTTPBasicAuth("public key", "secret")

request_access_token = requests.post(
    base_url + "api/v1/access_token",
    data=data,
    headers={"user-agent": "karma_comparator_script by Lazy-Long-8140"},
    auth=auth,
)

request_access_token.raise_for_status()
downloaded_data = request_access_token.json()
print(downloaded_data["access_token"])

token = "Bearer " + downloaded_data["access_token"]

api_url = "https://oauth.reddit.com"

headers = {
    "Authorization": token,
    "User-Agent": "Karma_comparator_script by Lazy-Long-8140",
    "x-requested-with": "XMLHttpRequest",
}

# search for subreddits matching with query "puppies", limit search to 5

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
# retry block in case of connectivity issues
"""
for retry in range(5):
    response = requests.get(url)
    try:
        response.raise_for_status()  # if raise_for_status does not raise an exception we have successfully recieved reply
        break
    except requests.exceptions.HTTPError as err:
        print(f"Error {err}, retrying after 5 seconds")
        sleep(5)

else:
    print(f"Failed connection to {url} after {retry} tries")
    exit()

data = response.json()
"""

#################

# user input two names

# if username does not exist print out an error message saying so

# GET /user/username/about

# Display the amount of upvotes and downvotes on the last post
