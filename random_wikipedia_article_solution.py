#! python3
# a program to get random wikipedia articles,
# allow the user to open webbrowser to read the article
# or continue to the next random wikipedia article

import requests
import bs4

# import lxml
import sys
import webbrowser

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0"
}

while True:
    try:
        article = requests.get("https://en.wikipedia.org/wiki/Special:Random", headers)
    except requests.exceptions.HTTPError as err:
        print(f"Something went wrong with downloading a page: {err}")
        print(err.response.status_code)

    soup_object = bs4.BeautifulSoup(article.content, "lxml")

    # title = soup_object.find_all("#firstHeading", href=True)
    title = soup_object.select(".mw-page-title-main")
    url = soup_object.select(".printfooter")
    # print(article.text)
    # https://www.tutorialspoint.com/beautiful_soup/beautiful_soup_find_element_using_css_selectors.htm

    print(title)
    print(url)
    split_url = (str(url)).split('"')
    webbrowser.open(split_url[8])

    user_input = input(
        " type *exit* to exit the program or press Enter to choose another random article: \n"
    )
    if user_input == "exit":
        sys.exit()
    elif user_input == "":
        continue
