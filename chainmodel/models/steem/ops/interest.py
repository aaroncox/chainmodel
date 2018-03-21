from chainmodel.models.steem.operation import Operation

class Interest(Operation):

    asset_fields = ['interest']
    tx_involves = ['owner']
    tx_originator = 'owner'
