from chainmodel.models.steem.operation import Operation

class AccountWitnessVote(Operation):

    tx_involves = ['account', 'witness']
    tx_originator = 'account'
