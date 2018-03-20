from chainmodel.models.steem.operation import Operation

class Comment(Operation):

    blacklist = [
        'body',
        'json_metadata',
    ]

    field_map = {
        'app': 'json_metadata.app',
        'tags': 'json_metadata.tags'
    }

    tx_involves = ['author']
    tx_originator = 'author'
