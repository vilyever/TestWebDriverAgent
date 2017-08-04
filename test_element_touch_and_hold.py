# encoding: utf-8
from wda_tools import *
import log_element_tool
import time

def test():
    client = wda_client.WDAClient()
    session = client.create_session("com.apple.mobileslideshow")
    print(session)
    time.sleep(1.0)

    element = session.find_element_by_predicate_string("name CONTAINS '屏幕快照' AND visible == true")
    time.sleep(1.0)

    element.wda_touch_and_hold(5)
    time.sleep(1.0)


if __name__ == '__main__':
    test()