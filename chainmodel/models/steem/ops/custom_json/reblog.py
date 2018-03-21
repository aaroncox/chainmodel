from chainmodel.models.steem.operation import Operation

class Reblog(Operation):

    field_map = {
        'custom_json_id': 'id',
    }

    tx_involves = ['required_posting_auths.0', 'json.1.author']
    tx_originator = 'required_posting_auths.0'
