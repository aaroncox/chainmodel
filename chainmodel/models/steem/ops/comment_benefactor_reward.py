from chainmodel.models.steem.operation import Operation

class CommentBenefactorReward(Operation):

    asset_fields = ['reward']
    tx_involves = ['benefactor']
    tx_originator = 'benefactor'
