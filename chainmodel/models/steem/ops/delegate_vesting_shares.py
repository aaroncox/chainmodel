from chainmodel.models.steem.operation import Operation

class DelegateVestingShares(Operation):

    asset_fields = ['vesting_shares']
    tx_involves = ['delegator', 'delegatee']
    tx_originator = 'delegator'
