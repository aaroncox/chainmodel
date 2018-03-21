from chainmodel.models.steem.operation import Operation

class ChangeRecoveryAccount(Operation):

    tx_involves = ['account_to_recover', 'new_recovery_account']
    tx_originator = 'account_to_recover'
