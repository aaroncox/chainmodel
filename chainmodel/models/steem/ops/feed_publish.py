from chainmodel.models.steem.operation import Operation

class FeedPublish(Operation):

    asset_fields = ['exchange_rate.base', 'exchange_rate.quote']
    tx_involves = ['publisher']
    tx_originator = 'publisher'
