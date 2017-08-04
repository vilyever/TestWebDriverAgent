# encoding: utf-8
from wda_tools import *
import log_element_tool
import time

def test():
    client = wda_client.WDAClient()
    session = client.create_session("com.apple.reminders")
    print(session)
    time.sleep(1.0)

    element = session.find_element_by_id("新建提醒事项")
    time.sleep(1.0)

    element.set_value("test abc")
    time.sleep(1.0)

    element.clear()
    time.sleep(1.0)


if __name__ == '__main__':
    test()