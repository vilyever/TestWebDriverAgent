# encoding: utf-8

import os
import json
import requests


def send_request(url, method='GET', data=None):
    print("\n****************************************************")
    print("send_request [%s] [%s]" % (url, method))
    if data:
        try:
            json_content = '{}'.format(data)
            print(json_content)
        except:
            pass

    response = requests.request(method, url, params=None, data=data)

    print("")
    print(response)
    print(response.url)
    print("\nresponse.content")
    print(response.content)
    print("****************************************************\n")

    content = json.loads(response.content)
    return content["value"]


def make_url(*urls):
    from requests.compat import urljoin
    return reduce(urljoin, [u.strip('/') + '/' for u in urls if u.strip('/')], '').rstrip('/')