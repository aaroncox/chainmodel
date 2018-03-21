from chainmodel.models.steem.operation import Operation

class Custom(Operation):

    tx_involves = ['required_auths.0']
    tx_originator = ['required_auths.0']
