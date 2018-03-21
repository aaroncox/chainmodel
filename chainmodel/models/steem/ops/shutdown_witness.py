from chainmodel.models.steem.operation import Operation

class ShutdownWitness(Operation):

    tx_involves = ['owner']
    tx_originator = 'owner'
