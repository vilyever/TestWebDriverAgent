# encoding: utf-8

from wda_tools import *
import time

def test():
    client = wda_client.WDAClient()
    value = client.status()
    print(value)
    time.sleep(1.0)

if __name__ == '__main__':
    test()