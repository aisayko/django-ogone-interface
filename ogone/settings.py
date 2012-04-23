"""
The following settings should be defined in your global settings

SHA_PRE and SHA_POST_SECRET have to be set in the ogone admin.
"""

try:
    from django.conf import settings
except ImportError:
    settings = {}


PSPID = getattr(settings, 'OGONE_PSPID', None)
USERID = getattr(settings, 'OGONE_USERID', None)
PSWD = getattr(settings, 'OGONE_PSWD', None)
SHA_IN_SECRET = getattr(settings, 'OGONE_SHA_IN_SECRET', None)
CURRENCY = getattr(settings, 'OGONE_CURRENCY', 'EUR')

# Change this in your ogone admin interface
HASH_METHOD = getattr(settings, 'OGONE_HASH_METHOD', 'sha512')

MODE = 'test' if getattr(settings, 'DEBUG', True) else 'prod'

ACTION_URLS = {
    'payment': {
        'test': 'https://secure.ogone.com/ncol/test/orderdirect.asp',
        'prod': 'https://secure.ogone.com/ncol/prod/orderdirect.asp'
    },
    'maintenance': {
        'test': 'https://secure.ogone.com/ncol/test/maintenancedirect.asp',
        'prod': 'https://secure.ogone.com/ncol/prod/maintenancedirect.asp'
    }
}
