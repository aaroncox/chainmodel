from chainmodel.models.steem.operation import Operation

class CustomJSON(Operation):

    tx_involves = ['required_auths.0', 'required_posting_auths.0']
    tx_originator = ['required_auths.0', 'required_posting_auths.0']
