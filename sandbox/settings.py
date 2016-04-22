import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
SECRET_KEY = 'si0$-gnv)76g$yf7p@(cg-^_q7j6df5cx$o-gsef5hd68phj!4'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        'LOCATION': 'testing-sandbox',
    }
}

UPS_USERNAME = 'nothing'
UPS_PASSWORD = 'nothing'
UPS_ACCESS_LICENSE_NUMBER = 'nothing'
UPS_BUFFER_DAYS = 1

UPS_DEFAULT_SHIP_FROM = {
    "Address": {
        "CountryCode": "US",
        "PostalCode": "38827"
    }
}
UPS_DEFAULT_SHIPMENT_WEIGHT = {
    "UnitOfMeasurement": {
        "Code": "LBS",
        "Description": "Pounds"
    },
    "Weight": "90"
}
UPS_DEFAULT_INVOICE = {
    "CurrencyCode": "USD",
    "MonetaryValue": "800"
}


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ups_tnt',
    'rest_framework',
)

ROOT_URLCONF = 'sandbox.urls'

STATIC_URL = '/static/'
