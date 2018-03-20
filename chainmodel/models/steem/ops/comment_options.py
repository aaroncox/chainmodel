from chainmodel.models.steem.operation import Operation

class CommentOptions(Operation):

    asset_fields = ['max_accepted_payout']
    tx_involves = ['author']
    tx_originator = 'author'
