from blockmodel.models.steem.operation import Operation

class CancelTransferFromSavings(Operation):

    tx_involves = ['from']
    tx_originator = 'from'
