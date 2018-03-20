from blockmodel.models.steem.operation import Operation

class Vote(Operation):

    tx_involves = ['voter', 'author']
    tx_originator = 'voter'
