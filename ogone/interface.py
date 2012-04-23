from security import OgoneSignature

import settings
import requests

import xml.dom.minidom


__all__ = ['Ogone', ]


class Ogone(object):
    """
    Implementation of Ogone.com DirectLink service.
    """
    @staticmethod
    def do_request(data, request_type='payment'):
        assert 'ORDERID' in data, 'Please specify ORDERID'
        assert 'AMOUNT' in data, 'Please specify AMOUNT'

        data['PSPID'] = settings.PSPID
        data['USERID'] = settings.USERID
        data['PSWD'] = settings.PSWD
        data['CURRENCY'] = settings.CURRENCY
        data['SHASIGN'] = OgoneSignature(data,
            hash_method=settings.HASH_METHOD,
            secret=settings.SHA_IN_SECRET
        ).signature()

        response = requests.post(
            settings.ACTION_URLS[request_type][settings.MODE], data=data
        )
        doc = xml.dom.minidom.parseString(response.text)
        attrs = doc.documentElement.attributes

        return dict(
            [(attrs.item(i).name, attrs.item(i).value)
                for i in range(attrs.length)]
        )
