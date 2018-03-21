from chainmodel.models.steem.operation import Operation

class ProducerReward(Operation):

    asset_fields = ['vesting_shares']
    tx_involves = ['producer']
