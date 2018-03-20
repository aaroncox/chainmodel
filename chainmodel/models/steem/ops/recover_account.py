from chainmodel.models.steem.operation import Operation

class RecoverAccount(Operation):

    tx_involves = ['account_to_recover']
    tx_originator = 'account_to_recover'
