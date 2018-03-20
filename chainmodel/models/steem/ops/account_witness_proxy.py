from chainmodel.models.steem.operation import Operation

class AccountWitnessProxy(Operation):

    tx_involves = ['account', 'proxy']
    tx_originator = 'account'
