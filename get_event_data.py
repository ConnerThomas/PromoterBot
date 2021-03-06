import requests
import re

# Sample usage:
#
# print(get_event_data("https://www.facebook.com/events/2817360921721103"))


def get_event_data(url):

    headers = {'accept': 'text/html'}
    r = requests.get(url, headers=headers)

    title = re.search(
        r'id="pageTitle">(.*)</title>', r.text, flags=re.M | re.DOTALL).group(1)

    time = re.search(
        r'id="title_subtitle"><span aria-label="([^"]*)', r.text, flags=re.M | re.DOTALL).group(
        1)

    # regularPatternImage = re.search(
    #    r'class="scaledImageFitHeight img" src="([^"]+)"', r.text, flags=re.M | re.DOTALL)

    imageURL = re.search(
        r'class="scaledImageFitHeight img" src="([^"]+)"', r.text, flags=re.M | re.DOTALL).group(1).replace("&amp;", "&")

  #  print(title, time, imageURL)
    return {'title': title, 'time': time, 'imageURL': imageURL}
