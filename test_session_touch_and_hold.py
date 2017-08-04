# encoding: utf-8

from wda_tools import *
import time

def test():
    client = wda_client.WDAClient()
    session = client.create_session("com.apple.Preferences")
    print(session)
    time.sleep(1.0)

    value = session.wda_touch_and_hold(70, 450, 3)
    print(value)
    time.sleep(1.0)

if __name__ == '__main__':
    test()