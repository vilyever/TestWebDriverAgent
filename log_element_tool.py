# encoding: utf-8
from wda_tools import *
import time

def log_element(element):
    print(element)
    time.sleep(1.0)

    if not element:
        return

    # value = element.enabled()
    # print(value)
    # time.sleep(1.0)

    value = element.rect()
    print(value)
    time.sleep(1.0)

    value = element.text()
    print(value)
    time.sleep(1.0)

    value = element.displayed()
    print(value)
    time.sleep(1.0)

    value = element.class_name()
    print(value)
    time.sleep(1.0)

    # value = element.wda_accessible()
    # print(value)
    # time.sleep(1.0)

    # value = element.wda_accessible_container()
    # print(value)
    # time.sleep(1.0)
