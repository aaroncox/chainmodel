from chainmodel.models.steem.operation import Operation

class TransferFromSavings(Operation):

    asset_fields = ['amount']
    tx_involves = ['from', 'to']
    tx_originator = 'from'
