from chainmodel.models.steem.operation import Operation

class LimitOrderCreate2(Operation):

    asset_fields = ['amount_to_sell', 'exchange_rate.base', 'exchange_rate.quote']
    datetime_fields = ['expiration']
    tx_involves = ['owner']
    tx_originator = 'owner'
