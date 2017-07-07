import requests
import pprint

url = "http://interia.pl"

words = ["Trump", "Atak", "Polska"]

dict = {}

def count_words_on_website(url,words):

    response = requests.get(url)

    for w in words:
        count = response.text.count(w)
        print(f"Word {w} occurs {count} times")
        dict[w]=count

    pprint.pprint(dict)


count_words_on_website(url,words)







