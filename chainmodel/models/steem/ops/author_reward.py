from chainmodel.models.steem.operation import Operation

class AuthorReward(Operation):

    asset_fields = ['sbd_payout', 'steem_payout', 'vesting_payout']
    tx_involves = ['author']
    tx_originator = 'author'
