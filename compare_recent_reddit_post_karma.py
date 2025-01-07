#! python3
from pkgutil import resolve_name

# https://alpscode.com/blog/how-to-use-reddit-api/

import requests
from time import sleep
import sys


# function to get oauth token
def get_oauth_token():
    base_url = "https://www.reddit.com/"
    data = {
        "grant_type": "password",
        "username": "reddit_username",
        "password": "reddit_password",
    }
    auth = requests.auth.HTTPBasicAuth("public key", "secret")
    url = base_url + "api/v1/access_token"
    headers = {"user-agent": "Karma_comparator_script by Lazy-Long-8140"}
    token = try_post_connection(url, data, headers, auth)
    return token


def try_post_connection(url, data, headers, auth):
    # a loop to keep trying for a connection if an exception is raised
    for retry in range(5):
        try:
            request_post = requests.post(url, data=data, headers=headers, auth=auth)
            # if no exception is raised by raise_for_status() we have successfuly gotten a response
            request_post.raise_for_status()
            if request_post.status_code == 200:
                return request_post.json()["access_token"]
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


def try_get_connection(user_name, oauth_token):
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
                api_url + "/user/" + user_name + "/comments",
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
        # return request_get.text
        # return request_get.json()
        # extracting info about the post
        post_info = {}
        post_info["subreddit"] = request_get.json()["data"]["children"][0]["data"][
            "subreddit"
        ]
        post_info["author"] = request_get.json()["data"]["children"][0]["data"][
            "author"
        ]
        post_info["link_title"] = request_get.json()["data"]["children"][0]["data"][
            "link_title"
        ]
        post_info["content"] = request_get.json()["data"]["children"][0]["data"]["body"]
        post_info["upvotes"] = request_get.json()["data"]["children"][0]["data"]["ups"]
        post_info["downvotes"] = request_get.json()["data"]["children"][0]["data"][
            "downs"
        ]
        return post_info


while True:
    username_1 = input(
        "Enter the name of the first user or 'exit' to exit the program:\n"
    )
    if username_1 == "exit":
        sys.exit()

    username_2 = input("Enter the name of the second user:\n")

    oauth_token = get_oauth_token()

    user_1_data = try_get_connection(username_1, oauth_token)
    user_2_data = try_get_connection(username_2, oauth_token)
    print(
        f'User {user_1_data["author"]} got {user_1_data["upvotes"]} upvotes and {user_1_data["downvotes"]} downvotes for posting "{user_1_data["content"]}" in thread called "{user_1_data["link_title"]}" in "{user_1_data["subreddit"]}" subreddit'
    )
    print(
        f'User {user_2_data["author"]} got {user_2_data["upvotes"]} upvotes and {user_2_data["downvotes"]} downvotes for posting "{user_2_data["content"]}" in thread called "{user_2_data["link_title"]}" in "{user_2_data["subreddit"]}" subreddit'
    )

    if user_1_data["upvotes"] > user_2_data["upvotes"]:
        print(f'{user_1_data["author"]} got more upvotes for their last post')
    elif user_1_data["upvotes"] < user_2_data["upvotes"]:
        print(f'{user_2_data["author"]} got more upvotes for their last post')
    else:
        print(
            f'{user_1_data["author"]} and {user_2_data["author"]} posts upvotes were tied'
        )
