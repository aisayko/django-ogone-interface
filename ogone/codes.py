__all__ = ['STATUS_CODES', 'OPERATION_CODES']


STATUS_CODES = (
    ('0', 'Incomplete or invalid'),
    ('1', 'Cancelled by client'),
    ('2', 'Authorization refused'),
    ('4', 'Order stored'),
    ('41', 'Waiting client payment'),
    ('5', 'Authorized'),
    ('51', 'Authorization waiting'),
    ('52', 'Authorization not known'),
    ('59', 'Author. to get manually'),
    ('6', 'Authorized and canceled'),
    ('61', 'Author. deletion waiting'),
    ('62', 'Author. deletion uncertain'),
    ('63', 'Author. deletion refused'),
    ('7', 'Payment deleted'),
    ('71', 'Payment deletion pending'),
    ('72', 'Payment deletion uncertain'),
    ('73', 'Payment deletion refused'),
    ('74', 'Payment deleted (not accepted)'),
    ('75', 'Deletion processed by merchant'),
    ('8', 'Refund'),
    ('81', 'Refund pending'),
    ('82', 'Refund uncertain'),
    ('83', 'Refund refused'),
    ('84', 'Payment declined by the acquirer (will be debited)'),
    ('85', 'Refund processed by merchant'),
    ('9', 'Payment requested'),
    ('91', 'Payment processing'),
    ('92', 'Payment uncertain'),
    ('93', 'Payment refused'),
    ('94', 'Refund declined by the acquirer'),
    ('95', 'Payment processed by merchant'),
    ('97', 'Being processed (intermediate technical status)'),
    ('98', 'Being processed (intermediate technical status)'),
    ('99', 'Being processed (intermediate technical status)'),
)

OPERATION_CODES = (
    ('0', 'RES'),
    ('1', 'SAL'),
    ('2', 'RFD without existed transaction'),
    ('3', 'REN'),
    ('4', 'DEL'),
    ('5', 'DES'),
    ('6', 'SAL'),
    ('7', 'SAS'),
    ('8', 'RFD'),
    ('9', 'RFS')
)
