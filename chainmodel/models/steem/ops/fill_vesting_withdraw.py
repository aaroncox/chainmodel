from chainmodel.models.steem.operation import Operation

class FillVestingWithdraw(Operation):

    asset_fields = ['deposited', 'withdrawn']
    tx_involves = ['from_account', 'to_account']
    tx_originator = 'from_account'
