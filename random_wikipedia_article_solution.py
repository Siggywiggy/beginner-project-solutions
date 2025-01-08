#! python3
# a program to get random wikipedia articles,
# allow the user to open webbrowser to read the article
# or continue to the next random wikipedia article

# get the random wikipedia article title and url from the API


# Accept-Encoding: gzip - reduce bandidth usage
# user agent header - "random wikipedia article retrieval script"
# api endmpoint - https://en.wikipedia.org/w/api.php
# https://www.mediawiki.org/wiki/API:Random
# rnlimit = 1
# https://www.mediawiki.org/w/api.php?action=query&format=json&list=random&formatversion=2&rnnamespace=0&rnlimit=1
# https://en.wikipedia.org/wiki/Special:Random?action=render
# ask the user wether to open the url or continue