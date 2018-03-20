from chainmodel.models.steem.operation import Operation

class Convert(Operation):

    asset_fields = ['amount']
    tx_involves = ['owner']
    tx_originator = 'owner'
