from chainmodel.models.steem.operation import Operation

class WithdrawVesting(Operation):

    asset_fields = ['vesting_shares']
    tx_involves = ['account']
    tx_originator = 'account'
