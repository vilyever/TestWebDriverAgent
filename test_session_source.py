# encoding: utf-8

from wda_tools import *
import time

def test():
    client = wda_client.WDAClient()

    session = client.create_session("com.apple.Preferences")
    print(session)
    time.sleep(1.0)

    value = session.source()
    print(value)
    time.sleep(1.0)

    value = client.source()
    print(value)
    time.sleep(1.0)


    value = session.wda_accessible_source()
    print(value)
    time.sleep(1.0)

    value = client.wda_accessible_source()
    print(value)
    time.sleep(1.0)

if __name__ == '__main__':
    test()