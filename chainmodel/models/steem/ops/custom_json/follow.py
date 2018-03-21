from chainmodel.models.steem.ops import Operation

class Follow(Operation):

    field_map = {
        'custom_json_id': 'id',
    }

    tx_involves = ['json.1.follower', 'json.1.following']
    tx_originator = 'json.1.follower'
