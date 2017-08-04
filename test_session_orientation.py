# encoding: utf-8

from wda_tools import *
import time

def test():
    client = wda_client.WDAClient()
    session = client.create_session("com.apple.Preferences")
    print(session)
    time.sleep(1.0)

    value = session.get_orientation()
    print(value)
    time.sleep(1.0)

    value = session.get_rotation()
    print(value)
    time.sleep(1.0)

    value = session.set_orientation("LANDSCAPE")
    print(session)
    time.sleep(10.0)

    value = session.get_orientation()
    print(value)
    time.sleep(1.0)

    value = session.get_rotation()
    print(value)
    time.sleep(1.0)

    value = session.set_orientation("PORTRAIT")
    print(value)
    time.sleep(1.0)

if __name__ == '__main__':
    test()