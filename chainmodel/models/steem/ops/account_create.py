from chainmodel.models.steem.operation import Operation

class AccountCreate(Operation):

    asset_fields = ['fee']
    tx_involves = ['creator', 'new_account_name']
    tx_originator = 'creator'
