# encoding: utf-8

from wda_tools import *
import time

def test():
    client = wda_client.WDAClient()
    session = client.create_session("com.apple.mobilesafari")
    print(session)
    time.sleep(1.0)

    value = session.open_url("weixin://")
    print(value)
    time.sleep(1.0)

if __name__ == '__main__':
    test()