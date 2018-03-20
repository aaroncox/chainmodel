from chainmodel.models.steem.operation import Operation

class CurationReward(Operation):

    asset_fields = ['reward']
    tx_involves = ['curator']
    tx_originator = 'curator'
