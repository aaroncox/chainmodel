from chainmodel.models.steem.operation import Operation

class LimitOrderCreate(Operation):

    asset_fields = ['amount_to_sell', 'min_to_receive']
    tx_involves = ['owner']
    tx_originator = 'owner'
