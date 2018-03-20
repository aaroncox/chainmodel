from chainmodel.models.steem.operation import Operation

class FillConvertRequest(Operation):

    asset_fields = ['amount_in','amount_out']
    tx_involves = ['owner']
    tx_originator = 'owner'
