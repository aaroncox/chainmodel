from chainmodel.models.steem.operation import Operation

class EscrowRelease(Operation):

    asset_fields = ['sbd_amount', 'steem_amount']
    tx_involves = ['from', 'to', 'agent', 'who']
    tx_originator = ['who']
