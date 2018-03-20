from chainmodel.models.base import Operation as BaseOperation
from chainmodel.models.base import OperationIndex as BaseOperationIndex

class Operation(BaseOperation):

    asset_ids = {
        '@@000000013': 'SBD',
        '@@000000021': 'STEEM',
        '@@000000037': 'VESTS',
    }

    def __init__(self, opData):
        super().__init__(opData)
        asset_fields = getattr(self, "asset_fields", None)
        if asset_fields:
            for field in asset_fields:
                fieldData = self.dotpath(opData, field)
                if isinstance(fieldData, list):
                    raw_amount = int(self.dotpath(opData, field)[0])
                    precision = int(self.dotpath(opData, field)[1])
                    asset_id = self.dotpath(opData, field)[2]
                    self.opData = self.setdotpath(opData, field, {
                        'amount': float("%.{}f".format(precision) % (raw_amount / (10 ** precision))),
                        'asset': self.asset_ids[asset_id]
                    })
                if isinstance(fieldData, str):
                    amount, asset = self.dotpath(opData, field).split(" ")
                    precision = 3
                    if asset == 'VESTS':
                        precision = 6
                    self.opData = self.setdotpath(opData, field, {
                        'amount': float("%.{}f".format(precision) % float(amount)),
                        'asset': asset
                    })


class OperationIndex(BaseOperationIndex):
    def __init__(self, opData):
        super().__init__(opData)
