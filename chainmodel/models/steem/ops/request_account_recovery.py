from chainmodel.models.steem.operation import Operation

class RequestAccountRecovery(Operation):

    tx_involves = ['account_to_recover', 'recovery_account']
    tx_originator = 'account_to_recover'
