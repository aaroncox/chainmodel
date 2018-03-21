from chainmodel.models.steem.operation import Operation

class EscrowDispute(Operation):

    tx_involves = ['from', 'to', 'agent', 'who']
    tx_originator = ['who']
