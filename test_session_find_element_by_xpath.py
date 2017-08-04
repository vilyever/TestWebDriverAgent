# encoding: utf-8
from wda_tools import *
import log_element_tool
import time

def test():
    client = wda_client.WDAClient()
    session = client.create_session("com.apple.Preferences")
    print(session)
    time.sleep(1.0)

    element = session.find_element_by_xpath("//XCUIElementTypeStaticText[@name='飞行模式']")
    log_element_tool.log_element(element)
    time.sleep(1.0)

    elements = session.find_elements_by_xpath("//XCUIElementTypeTable//XCUIElementTypeStaticText[@value='飞行模式']")
    for element in elements:
        log_element_tool.log_element(element)
        time.sleep(1.0)

    elements = session.find_elements_by_xpath("//XCUIElementTypeCell[@name='飞行模式']/XCUIElementTypeStaticText")
    for element in elements:
        log_element_tool.log_element(element)
        time.sleep(1.0)

if __name__ == '__main__':
    test()