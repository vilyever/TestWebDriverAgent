# encoding: utf-8
from wda_tools import *
import log_element_tool
import time

def test():
    client = wda_client.WDAClient()
    session = client.create_session("com.apple.mobileslideshow")
    print(session)
    time.sleep(1.0)

    element = session.find_element_by_class_name("XCUIElementTypeCollectionView")
    time.sleep(1.0)

    element.wda_scroll_to_child_by_child_name("屏幕快照, 竖排, 5月23日 08:09")
    time.sleep(1.0)

    element.wda_scroll('up', 1.0)
    time.sleep(1.0)

    element.wda_scroll_to_child_by_predicate_string("name CONTAINS '5月09日'")
    time.sleep(1.0)

    element = session.find_element_by_predicate_string("type == 'XCUIElementTypeCell' AND visible == false")
    time.sleep(1.0)

    element.wda_scroll_to_self_visible()
    time.sleep(1.0)


if __name__ == '__main__':
    test()