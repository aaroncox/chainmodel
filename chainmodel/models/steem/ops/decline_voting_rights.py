from chainmodel.models.steem.operation import Operation

class DeclineVotingRights(Operation):

    tx_involves = ['account']
    tx_originator = ['account']
