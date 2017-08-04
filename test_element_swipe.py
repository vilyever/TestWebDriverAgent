# encoding: utf-8
from wda_tools import *
import log_element_tool
import time

def test():
    client = wda_client.WDAClient()
    session = client.create_session("com.apple.mobilecal")
    print(session)
    time.sleep(1.0)

    element = session.find_element_by_id("周")
    time.sleep(1.0)

    element.click()
    time.sleep(1.0)

    element = session.find_element_by_class_name("XCUIElementTypeScrollView")
    time.sleep(1.0)

    element.wda_swipe("up")
    time.sleep(1.0)

    element.wda_swipe("left")
    time.sleep(1.0)

    element.wda_swipe("down")
    time.sleep(1.0)

    element.wda_swipe("right")
    time.sleep(1.0)


if __name__ == '__main__':
    test()