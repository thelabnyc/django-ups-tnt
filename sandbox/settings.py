import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
SECRET_KEY = "si0$-gnv)76g$yf7p@(cg-^_q7j6df5cx$o-gsef5hd68phj!4"

ROOT_URLCONF = "sandbox.urls"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "ups_tnt",
    "rest_framework",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    },
]

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        "LOCATION": "testing-sandbox",
    }
}

STATIC_URL = "/static/"

UPS_USERNAME = "nothing"
UPS_PASSWORD = "nothing"
UPS_ACCESS_LICENSE_NUMBER = "nothing"
UPS_BUFFER_DAYS = 1

UPS_DEFAULT_SHIP_FROM = {"Address": {"CountryCode": "US", "PostalCode": "38827"}}
UPS_DEFAULT_SHIPMENT_WEIGHT = {
    "UnitOfMeasurement": {"Code": "LBS", "Description": "Pounds"},
    "Weight": "90",
}
UPS_DEFAULT_INVOICE = {"CurrencyCode": "USD", "MonetaryValue": "800"}
