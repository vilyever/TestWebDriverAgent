# encoding: utf-8

from wda_tools import *
import time

def test():
    client = wda_client.WDAClient()
    session = client.create_session("com.apple.Preferences")
    print(session)
    time.sleep(1.0)

    value = session.window_size()
    print(value)
    time.sleep(1.0)

if __name__ == '__main__':
    test()