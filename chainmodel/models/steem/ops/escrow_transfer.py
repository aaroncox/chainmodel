from chainmodel.models.steem.operation import Operation

class EscrowTransfer(Operation):

    asset_fields = ['sbd_amount', 'steem_amount', 'fee']
    datetime_fields = ['ratification_deadline', 'escrow_expiration']
    tx_involves = ['from', 'to', 'agent', 'who']
    tx_originator = ['who']
