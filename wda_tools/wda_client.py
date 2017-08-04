# encoding: utf-8

import os
import json
import wda_requests
import wda_session


class WDAClient:
    def __init__(self, server_url='http://127.0.0.1:8100/'):
        self._server_url = server_url

    @property
    def server_url(self):
        return self._server_url

    def _request(self, command, method='GET', data=None, using_wda=False):
        url = self._server_url
        if command:
            if using_wda:
                url = wda_requests.make_url(url, "wda", command)
            else:
                url = wda_requests.make_url(url, command)
        return wda_requests.send_request(url, method, data)

    def status(self):
        response_value = self._request("status", 'GET')
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

    def wda_press_home(self):
        response_value = self._request("homescreen", 'POST', using_wda=True)
        return response_value

    def screen_shot(self, filename=None):
        import base64
        import errno
        response_value = self._request("screenshot", 'GET')
        if filename:

            if not os.path.exists(os.path.dirname(filename)):
                try:
                    os.makedirs(os.path.dirname(filename))
                except OSError as exc:  # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise

            with open(filename, 'w') as f:
                value = base64.b64decode(response_value)
                f.write(value)
                f.close()

        return response_value

    # def wda_health_check(self):
    #     response_value = self._request("healthcheck", 'GET', using_wda=True)
    #     return response_value

    def create_session(self, bundle_id):
        data = json.dumps({'desiredCapabilities': {'bundleId': bundle_id}})
        response_value = self._request("session", 'POST', data)

        session = wda_session.WDASession(self, response_value["sessionId"])

        return session
