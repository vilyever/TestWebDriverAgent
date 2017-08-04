# encoding: utf-8

from wda_tools import *
import time

def test():
    client = wda_client.WDAClient()
    session = client.create_session("com.apple.Preferences")
    print(session)
    time.sleep(1.0)

    session.wda_deactivate(5.5)
    time.sleep(10.0)

    value = session.close()
    print(value)
    time.sleep(1.0)

if __name__ == '__main__':
    test()