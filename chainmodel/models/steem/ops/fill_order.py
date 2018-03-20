from chainmodel.models.steem.operation import Operation

class FillOrder(Operation):

    asset_fields = ['current_pays', 'open_pays']
    tx_involves = ['open_owner', 'current_owner']
    tx_originator = 'current_owner'
