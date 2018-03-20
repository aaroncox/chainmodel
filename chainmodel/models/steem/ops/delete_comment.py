from chainmodel.models.steem.operation import Operation

class DeleteComment(Operation):

    tx_involves = ['author']
    tx_originator = 'author'
