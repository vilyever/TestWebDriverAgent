# encoding: utf-8

import os
import json
import wda_requests
import wda_client
import wda_element

class WDASession:
    def __init__(self, client, session_id):
        self._client = client
        self._session_id = session_id

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __str__(self):
        return 'WDASession (id=%s)' % self._session_id

    @property
    def session_id(self):
        return self._session_id

    def session_url(self, using_wda=False):
        if using_wda:
            url = wda_requests.make_url(self._client.server_url, "session", self._session_id, "wda")
        else:
            url = wda_requests.make_url(self._client.server_url, "session", self._session_id)
        return url

    def _request(self, command, method='GET', data=None, using_wda=False):
        url = self.session_url(using_wda=using_wda)
        if command:
            url = wda_requests.make_url(url, command)
        return wda_requests.send_request(url, method, data)

    def close(self):
        response_value = self._request(None, 'DELETE')
        return response_value

    # def open_url(self, url):
    #     # always failed, maybe this function is not support
    #     data = json.dumps({'url': url})
    #     response_value = self._request("url", 'POST', data)
    #     return response_value

    # check app is exist and has any element
    # check home button can press
    # def wda_deactivate(self, duration):
    #     data = json.dumps({'duration': duration})
    #     response_value = self._request("deactivateApp", 'POST', data, using_wda=True)
    #     return response_value

    def wda_tap(self, x, y, element_id='0'):
        data = json.dumps({'x': x, 'y': y})
        response_value = self._request("tap/" + element_id, 'POST', data, using_wda=True)
        return response_value

    def wda_double_tap(self, x, y):
        data = json.dumps({'x': x, 'y': y})
        response_value = self._request("doubleTap", 'POST', data, using_wda=True)
        return response_value

    def wda_touch_and_hold(self, x, y, duration):
        data = json.dumps({'x': x, 'y': y, 'duration': duration})
        response_value = self._request("touchAndHold", 'POST', data, using_wda=True)
        return response_value

    def wda_drag_from_to(self, from_x, from_y, to_x, to_y, touch_down_duration = 0.1):
        data = json.dumps({'fromX': from_x, 'fromY': from_y, 'toX': to_x, 'toY': to_y, 'duration': touch_down_duration})
        response_value = self._request("dragfromtoforduration", 'POST', data, using_wda=True)
        return response_value

    def source(self, format='xml'):
        """
        Args:
            - format(string): xml | json
        """
        data = json.dumps({'desiredCapabilities': {'format': format}})
        response_value = self._request("source", 'GET', data)
        return response_value

    def wda_accessible_source(self):
        response_value = self._request("accessibleSource", 'GET', using_wda=True)
        return response_value

    # def get_orientation(self):
    #     response_value = self._request("orientation", 'GET')
    #     return response_value

    # def set_orientation(self, orientation):
    #     """
    #     Args:
    #         - orientation(string): LANDSCAPE | PORTRAIT | UIA_DEVICE_ORIENTATION_LANDSCAPERIGHT |
    #                 UIA_DEVICE_ORIENTATION_PORTRAIT_UPSIDEDOWN
    #     """
    #     data = json.dumps({'orientation': orientation})
    #     response_value = self._request("orientation", 'POST', data)
    #     return response_value

    # def get_rotation(self):
    #     response_value = self._request("rotation", 'GET')
    #     return response_value

    # def set_rotation(self, x, y, z):
    #     data = json.dumps({'x': x, 'y': y, 'z': z})
    #     response_value = self._request("rotation", 'POST', data)
    #     return response_value

    def window_size(self):
        response_value = self._request("window/size", 'GET')
        return response_value

    def wda_send_keys(self, value):
        data = json.dumps({'value': [value]})
        response_value = self._request("keys", 'POST', data, using_wda=True)
        return response_value

    # def wda_dismiss_keyboard(self):
    #     print("for iPad mini, crash on [XCUIApplication dismissKeyboard]")
    #     response_value = self._request("keyboard/dismiss", 'POST', using_wda=True)
    #     return response_value

    # def get_alert_text(self):
    #     response_value = self._request("alert/text", 'GET')
    #     return response_value

    # def wda_get_alert_buttons(self):
    #     response_value = self._request("alert/buttons", 'GET', using_wda=True)
    #     return response_value

    # def accept_alert(self, button_name=None):
    #     data = json.dumps({'name': button_name})
    #     response_value = self._request("alert/accept", 'POST', data)
    #     return response_value

    # def dismiss_alert(self, button_name=None):
    #     data = json.dumps({'name': button_name})
    #     response_value = self._request("alert/dismiss", 'POST', data)
    #     return response_value

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

        return self._elements_with_response_value(response_value)

    def _elements_with_response_value(self, response_value):
        elements = []

        if not isinstance(response_value, list):
            return elements

        for item in response_value:
            if item.has_key("ELEMENT"):
                element = wda_element.WDAElement(self, None, item["ELEMENT"])
                elements.append(element)

        return elements