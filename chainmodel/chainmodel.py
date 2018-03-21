class ChainModel():

    def __init__(self, schema=None):
        if not schema:
            raise Exception('valid_schema_required')
        self.schema = schema

    def block(self, blockData):
        return self.schema.models['block'](blockData)

    def index(self, opData):
        return self.schema.models['index'](opData)

    def getSubtype(self, opData):
        if opData['operation_type'] == 'custom_json' and 'id' in opData:
            return '.'.join([opData['operation_type'], opData['id']])
        return None

    def get(self, opData):
        opType = opData['operation_type']
        opSubtype = self.getSubtype(opData)
        models = self.schema.models

        if opSubtype and opSubtype in models['ops']:
            op = models['ops'][opSubtype](opData)

        # otherwise if a model is defined, use that
        elif opType in models['ops']:
            op = models['ops'][opType](opData)

        # otherwise encapsulate in a generic operation model
        else:
            print('{} - {}'.format(opData['block_num'], opType))
            # pprint(opData)
            op = models['op'](opData)

        return op
