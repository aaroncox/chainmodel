from chainmodel.models.steem.operation import Operation

class AccountUpdate(Operation):

    tx_involves = ['account']
    tx_originator = 'account'
