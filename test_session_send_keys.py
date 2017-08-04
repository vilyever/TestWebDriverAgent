# encoding: utf-8
from wda_tools import *
import time

def test():
    client = wda_client.WDAClient()
    session = client.create_session("com.apple.reminders")
    print(session)
    time.sleep(1.0)

    value = session.wda_tap(400, 120)
    print(value)
    time.sleep(1.0)

    value = session.wda_send_keys("haha test")
    print(value)
    time.sleep(1.0)

    value = session.wda_send_keys("我是谁？？lk ！@#￥￥")
    print(value)
    time.sleep(1.0)

    # value = session.wda_dismiss_keyboard()
    # wda_tools.log_response(response)
    # time.sleep(1.0)

if __name__ == '__main__':
    test()