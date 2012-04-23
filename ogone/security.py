import hashlib


__all__ = ['OgoneSignature', ]


class OgoneSignature(object):
    """
    Signs the ogone parameters
    """
    def __init__(self, data, hash_method, secret, encoding='utf8'):
        assert hash_method in ['sha1', 'sha256', 'sha512']
        assert str(secret)

        self.data = data.copy()
        self.hash_method = hash_method
        self.secret = secret
        self.encoding = encoding

    def _sort_data(self, data):
        sorted_data = [(k.upper(), v) for k, v in data.items() \
                       if self._filter_data(k.upper(), v)]
        sorted_data.sort(key=lambda x: x, reverse=False)
        return sorted_data

    def _filter_data(self, k, v):
        valid = True
        if v == '' or v is None:
            valid = False
        if k == 'SHASIGN':
            valid = False
        return valid

    def _merge_data(self, data):
        pairs = ['%s=%s' % (k, v) for k, v in data]
        pre_sign_string = self.secret.join(pairs) + self.secret
        return pre_sign_string.encode(self.encoding)

    def _sign_string(self, pre_sign_string):
        hashmethod = getattr(hashlib, self.hash_method)
        signed = hashmethod(pre_sign_string).hexdigest().upper()
        return signed

    def signature(self):
        sorted_data = self._sort_data(self.data)
        pre_sign_string = self._merge_data(sorted_data)
        signed = self._sign_string(pre_sign_string)
        return signed

    def __unicode__(self):
        return self.signature()
