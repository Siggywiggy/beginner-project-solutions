#! python3
# a program to get random wikipedia articles,
# allow the user to open webbrowser to read the article
# or continue to the next random wikipedia article

import requests
import bs4
import sys
import webbrowser

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0"
}

while True:
    user_input = input(
        "Type *exit* to exit the program or press Enter to choose a random article: \n"
    )
    if user_input == "exit":
        sys.exit()
    elif user_input == "":
        pass
    else:
        print("press Enter or enter *exit* to exit the program")
        continue

    try:
        article = requests.get("https://en.wikipedia.org/wiki/Special:Random", headers)
        # print(article.text)
    except requests.exceptions.HTTPError as err:
        print(f"Something went wrong with downloading a page: {err}")
        print(err.response.status_code)

    soup_object = bs4.BeautifulSoup(article.content, "lxml")

    # title = soup_object.find_all("#firstHeading", href=True)
    title = soup_object.select(".mw-page-title-main")
    url = soup_object.select(".printfooter")
    clean_title = (str(title).split(">"))[1].split("<")[0]
    clean_url = (str(url)).split('"')[8]

    input_open = input(
        f"Would you like to *open* the article about {clean_title} or continue to next random article (press Enter)\n"
    )
    if input_open == "open":
        webbrowser.open(clean_url)
    elif input_open == "":
        continue
