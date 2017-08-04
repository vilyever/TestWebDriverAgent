# encoding: utf-8
from wda_tools import *
import log_element_tool
import time

def test():
    client = wda_client.WDAClient()
    session = client.create_session("com.apple.Preferences")
    print(session)
    time.sleep(1.0)

    element = session.find_element_by_predicate_string("type CONTAINS 'Table'")
    log_element_tool.log_element(element)
    time.sleep(1.0)

    element = element.find_element_by_predicate_string("name == '蓝牙' AND type CONTAINS 'Cell'")
    log_element_tool.log_element(element)
    time.sleep(1.0)

    element = element.find_element_by_predicate_string("type CONTAINS 'StaticText'")
    log_element_tool.log_element(element)
    time.sleep(1.0)

if __name__ == '__main__':
    test()