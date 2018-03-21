from chainmodel.models.steem.operation import Operation

class Pow2(Operation):

    tx_involves = ['work.1.input.worker_account']
    tx_originator = 'work.1.input.worker_account'
