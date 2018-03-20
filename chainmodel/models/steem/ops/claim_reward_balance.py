from chainmodel.models.steem.operation import Operation

class ClaimRewardBalance(Operation):

    asset_fields = [
        'reward_sbd',
        'reward_steem',
        'reward_vests',
    ]

    tx_involves = ['account']
    tx_originator = 'account'
