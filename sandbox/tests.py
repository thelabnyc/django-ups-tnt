from django.test import override_settings
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from ups_tnt import settings
from ups_tnt.tnt import ups_url
from .test_responses import SUCCESS_RESPONSE, BAD_AUTH_RESPONSE
from contextlib import contextmanager
import responses
import datetime


@contextmanager
def patch_settings(**kwargs):
    orig = {}
    for key, new_value in kwargs.items():
        orig[key] = getattr(settings, key)
        setattr(settings, key, new_value)

    yield

    for key, old_value in orig.items():
        setattr(settings, key, old_value)


def setting(**patches):
    def wrap(fn):
        def wrapped(*args, **kwargs):
            with patch_settings(**patches):
                ret = fn(*args, **kwargs)
            return ret
        return wrapped
    return wrap


class CallException(Exception):
    pass


def get_buffer():
    raise CallException


class UPSTests(APITestCase):
    @responses.activate
    def test_time_in_transit(self):
        if settings.UPS_TEST_LIVE is False:
            responses.add(responses.POST, ups_url, body=SUCCESS_RESPONSE, status=200, content_type='application/json')
        url = reverse('time-in-transit')
        data = {
            "ship_to": {
                "postal_code": "10031",
            }
        }
        res = self.client.post(url, data, format='json')
        self.assertEqual(res.status_code, 200)
        arrives_on = res.data['ServiceSummary'][0]['EstimatedArrival']['DateTime'][:10]
        arrives_on = datetime.datetime.strptime(arrives_on, '%Y-%m-%d')
        self.assertIsInstance(arrives_on, datetime.datetime)

        # Test required fields
        res = self.client.post(url, {'ship_to': []}, format='json')
        self.assertEqual(res.status_code, 400)

        data = {'ship_to': {"city": "New York"}}
        res = self.client.post(url, data, format='json')
        self.assertEqual(res.status_code, 400)

        data = {
            "ship_to": {
                "city": "New York",
                "state_province_code": "NY",
            }
        }
        res = self.client.post(url, data, format='json')
        self.assertEqual(res.status_code, 400)

        data = {
            "ship_to": {
                "city": "New York",
                "state_province_code": "NY",
                "postal_code": "10031",
            }
        }
        res = self.client.post(url, data, format='json')
        self.assertEqual(res.status_code, 200)

        # Test invalid data
        data = {
            "ship_to": {
                "postal_code": "99999999999999",
            }
        }
        res = self.client.post(url, data, format='json')
        self.assertEqual(res.status_code, 400)

        data = {
            "ship_to": {
                "postal_code": "",
            }
        }
        res = self.client.post(url, data, format='json')
        self.assertEqual(res.status_code, 400)

    @setting(UPS_BUFFER_DAYS=get_buffer)
    def test_callable_buffer_time(self):
        url = reverse('time-in-transit')
        data = {
            "ship_to": {
                "postal_code": "10031",
            }
        }
        with self.assertRaises(CallException):
            res = self.client.post(url, data, format='json')

    @setting(UPS_USERNAME="fail")
    @responses.activate
    def test_auth_fail(self):
        responses.add(responses.POST, ups_url, body=BAD_AUTH_RESPONSE, status=200, content_type='application/json')
        url = reverse('time-in-transit')
        data = {
            "ship_to": {
                "postal_code": "10031",
            }
        }
        res = self.client.post(url, data, format='json')
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data['detail'], "Invalid Access License number")
