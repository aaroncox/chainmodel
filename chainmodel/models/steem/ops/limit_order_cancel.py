from chainmodel.models.steem.operation import Operation

class LimitOrderCancel(Operation):

    tx_involves = ['owner']
    tx_originator = 'owner'
