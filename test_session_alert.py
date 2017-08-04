# encoding: utf-8
from wda_tools import *
import time

def test():
    client = wda_client.WDAClient()
    session = client.create_session("com.apple.Preferences")
    print(session)
    time.sleep(1.0)

    value = session.wda_tap(70, 100)
    print(value)
    time.sleep(1.0)

    value = session.get_alert_text()
    print(value)
    time.sleep(1.0)

    value = session.wda_get_alert_buttons()
    print(value)
    time.sleep(1.0)

    value = session.accept_alert("好")
    print(value)
    time.sleep(1.0)

    value = session.accept_alert("取消")
    print(value)
    time.sleep(1.0)

if __name__ == '__main__':
    test()