from chainmodel.models.steem.operation import Operation

class ReturnVestingDelegation(Operation):

    asset_fields = ['vesting_shares']
    tx_involves = ['account_to_recover', 'recovery_account']
    tx_originator = 'account_to_recover'
