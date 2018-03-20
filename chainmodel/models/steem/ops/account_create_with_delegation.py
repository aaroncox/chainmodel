from chainmodel.models.steem.operation import Operation

class AccountCreateWithDelegation(Operation):

    asset_fields = ['delegation', 'fee']
    tx_involves = ['creator', 'new_account_name']
    tx_originator = 'creator'
