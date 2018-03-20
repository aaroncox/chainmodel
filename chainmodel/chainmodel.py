class ChainModel():

    def __init__(self, schema=None):
        if not schema:
            raise Exception("A valid schema must be supplied.")
        self.schema = schema

    def block(self, blockData):
        return self.schema.models['block'](blockData)

    def index(self, opData):
        return self.schema.models['index'](opData)

    def get(self, opData):
        opType = opData['operation_type']
        opSubtype = "{}_subtypes".format(opType)
        models = self.schema.models
        # custom_json sub models - use a custom model for each custom_json type if it exists
        if opSubtype in models['ops'] and isinstance(models['ops'][opSubtype], dict):
            op = models['op'](opData)
            opData['id'] = op.dotpath(opData, 'json.0')
            if opData['id'] in models['ops'][opSubtype]:
                op = models['ops'][opSubtype][opData['id']](opData)

        # otherwise if a model is defined, use that
        elif opType in models['ops']:
            op = models['ops'][opType](opData)

        # otherwise encapsulate in a generic operation model
        else:
            print("{} - {}".format(opData['block_num'], opType))
            # pprint(opData)
            op = models['op'](opData)

        return op
