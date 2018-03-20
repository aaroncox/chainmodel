from chainmodel.models.steem.operation import Operation

class Pow(Operation):

    tx_involves = ['worker_account']
    tx_originator = 'worker_account'
