from chainmodel.models.steem.operation import Operation

class WitnessUpdate(Operation):

    asset_fields = ['fee', 'props.account_creation_fee']
    tx_involves = ['owner']
    tx_originator = 'owner'
