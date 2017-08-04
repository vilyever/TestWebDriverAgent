# encoding: utf-8

import os
import json
from wda_tools import *


class WDAElement:
    def __init__(self, session, parent_element, element_id):
        self._session = session
        self._parent_element = parent_element
        self._element_id = element_id

    def __str__(self):
        return 'WDAElement (id=%s)' % self._element_id

    @property
    def element_id(self):
        return self._element_id

    def element_url(self, using_wda=False):
        url = wda_requests.make_url(self._session.session_url(using_wda=using_wda), "element", self._element_id)

        return url

    def _request(self, command, method='GET', data=None, using_wda=False):
        url = self.element_url(using_wda=using_wda)
        if command:
            url = wda_requests.make_url(url, command)
        return wda_requests.send_request(url, method, data)

    def enabled(self):
        response_value = self._request("enabled", 'GET')
        return response_value

    def rect(self):
        response_value = self._request("rect", 'GET')
        return response_value

    def text(self):
        response_value = self._request("text", 'GET')
        return response_value

    def displayed(self):
        response_value = self._request("displayed", 'GET')
        return response_value

    # XCUIElementType
    def class_name(self):
        response_value = self._request("name", 'GET')
        return response_value

    def wda_accessible(self):
        response_value = self._request("accessible", 'GET', using_wda=True)
        return response_value

    def wda_accessible_container(self):
        response_value = self._request("accessibilityContainer", 'GET', using_wda=True)
        return response_value

    def set_value(self, value):
        data = json.dumps({'value': value})
        response_value = self._request("value", 'POST', data)
        return response_value

    def click(self):
        response_value = self._request("click", 'POST')
        return response_value

    def clear(self):
        response_value = self._request("clear", 'POST')
        return response_value

    def wda_swipe(self, direction):
        """
        Args:
            - direction(string): up | down | left | right
        """
        data = json.dumps({'direction': direction})
        response_value = self._request("swipe", 'POST', data, using_wda=True)
        return response_value

    # if scale > 1 , velocity should > 0
    # else if scale < 1, velocity should < 0
    def wda_pinch(self, scale, velocity):
        data = json.dumps({'scale': scale, 'velocity': velocity})
        response_value = self._request("pinch", 'POST', data, using_wda=True)
        return response_value

    def wda_double_tap(self):
        response_value = self._request("doubleTap", 'POST', using_wda=True)
        return response_value

    # cannot test, not sure this is work
    # def wda_two_finger_tap(self):
    #     response_value = self._request("twoFingerTap", 'POST', using_wda=True)
    #     return response_value

    def wda_touch_and_hold(self, duration):
        data = json.dumps({'duration': duration})
        response_value = self._request("touchAndHold", 'POST', data, using_wda=True)
        return response_value

    def wda_scroll_to_child_by_child_name(self, child_name):
        data = json.dumps({'name': child_name})
        response_value = self._request("scroll", 'POST', data, using_wda=True)
        return response_value

    def wda_scroll_to_child_by_predicate_string(self, predicate_string):
        data = json.dumps({'predicateString': predicate_string})
        response_value = self._request("scroll", 'POST', data, using_wda=True)
        return response_value

    def wda_scroll(self, direction, distance=1.0):
        """
        Args:
            - direction(string): up | down | left | right
        """
        data = json.dumps({'direction': direction, 'distance': distance})
        response_value = self._request("scroll", 'POST', data, using_wda=True)
        return response_value

    def wda_scroll_to_self_visible(self):
        data = json.dumps({'toVisible': True})
        response_value = self._request("scroll", 'POST', data, using_wda=True)
        return response_value

    def wda_drag_from_to(self, from_x, from_y, to_x, to_y, touch_down_duration = 0.1):
        data = json.dumps({'fromX': from_x, 'fromY': from_y, 'toX': to_x, 'toY': to_y, 'duration': touch_down_duration})
        response_value = self._request("dragfromtoforduration", 'POST', data, using_wda=True)
        return response_value

    def find_element_by_id(self, id):
        elements = self.find_elements_by_id(id)
        element = next(iter(elements or []), None)
        return element

    def find_element_by_link_text(self, name=None, value=None, label=None, is_partial=False):
        elements = self.find_elements_by_link_text(name, value, label, is_partial)
        element = next(iter(elements or []), None)
        return element

    # XCUIElementType
    def find_element_by_class_name(self, class_name):
        elements = self.find_elements_by_class_name(class_name)
        element = next(iter(elements or []), None)
        return element

    # XCUIElementType
    def find_element_by_class_chain(self, class_chain):
        elements = self.find_elements_by_class_chain(class_chain)
        element = next(iter(elements or []), None)
        return element

    # XCUIElementType
    def find_element_by_xpath(self, xpath):
        elements = self.find_elements_by_xpath(xpath)
        element = next(iter(elements or []), None)
        return element

    def find_element_by_predicate_string(self, predicate_string):
        elements = self.find_elements_by_predicate_string(predicate_string)
        element = next(iter(elements or []), None)
        return element

    def find_elements_by_id(self, id):
        elements = self.find_elements('id', id)
        return elements

    def find_elements_by_link_text(self, name=None, value=None, label=None, is_partial=False):
        if is_partial:
            json_using = "partial link text"
        else:
            json_using = "link text"

        if name:
            json_value = "name=%s" % name
        elif value:
            json_value = "value=%s" % value
        elif label:
            json_value = "label=%s" % label
        else:
            return None

        elements = self.find_elements(json_using, json_value)
        return elements

    # XCUIElementType
    def find_elements_by_class_name(self, class_name):
        elements = self.find_elements('class name', class_name)
        return elements

    # XCUIElementType
    def find_elements_by_class_chain(self, class_chain):
        elements = self.find_elements('class chain', class_chain)
        return elements

    # XCUIElementType
    def find_elements_by_xpath(self, xpath):
        elements = self.find_elements('xpath', xpath)
        return elements

    def find_elements_by_predicate_string(self, predicate_string):
        elements = self.find_elements('predicate string', predicate_string)
        return elements

    def find_elements(self, using, value):
        data = json.dumps({'using': using, 'value': value})
        response_value = self._request("elements", 'POST', data)

        return self._elements_with_value(response_value)

    def _elements_with_value(self, value):
        elements = []

        if not isinstance(value, list):
            return elements

        for item in value:
            if item.has_key("ELEMENT"):
                element = WDAElement(self._session, self, item["ELEMENT"])
                elements.append(element)

        return elements
