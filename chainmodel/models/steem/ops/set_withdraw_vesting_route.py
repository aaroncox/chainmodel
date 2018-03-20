from chainmodel.models.steem.operation import Operation

class SetWithdrawVestingRoute(Operation):

    tx_involves = ['from_account', 'to_account']
    tx_originator = 'from_account'
