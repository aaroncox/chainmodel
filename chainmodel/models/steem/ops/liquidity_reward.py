from chainmodel.models.steem.operation import Operation

class LiquidityReward(Operation):

    asset_fields = ['payout']
    tx_involves = ['owner']
