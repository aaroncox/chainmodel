import json
import hashlib

def nested_set(dic, keys, value):
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value

class Operation():

    indexes = False

    def __getitem__(self, name):
        return self.dotpath(self.opData, name)

    def __init__(self, opData):

        self.clean_op = opData

        # Load any fields that are strings but contain JSON data
        json_string_fields = ['json', 'json_metadata']
        for field in json_string_fields:
            if field in opData:
                try:
                    opData[field] = json.loads(opData[field])
                except:
                    pass

        # field_map allows the renaming of fields and moving of data on the model
        # The field_map should be a dict, where the key is the new field name and the value is the path to the value
        #
        # Example:
        #
        # field_map = {
        #     'app': 'json_metadata.app',
        #     'tags': 'json_metadata.tags'
        # }
        #
        field_map = getattr(self, "field_map", None)
        if field_map:
            for newField, oldField in self.field_map.items():
                opData[newField] = self.dotpath(opData, oldField)

        # tx_originator is a designated single field for the account name that originated this operation
        # Defaults to false
        # If `tx_originator` is set on the child - add it to the model
        tx_originator = getattr(self, "tx_originator", None)
        if tx_originator:
            if isinstance(tx_originator, list):
                for field in tx_originator:
                    if self.dotpath(opData, field):
                        opData['tx_originator'] = self.dotpath(opData, field)
                        break
            elif isinstance(tx_originator, str):
                opData['tx_originator'] = self.dotpath(opData, tx_originator)
            else:
                opData['tx_originator'] = None

        # tx_involves is a list of account names who are involved in this transaction
        # Defaults to empty list
        # If `tx_involves` is set on the child - add it to the model
        tx_involves = getattr(self, "tx_involves", None)
        opData['tx_involves'] = [self.dotpath(opData, field) for field in tx_involves if self.dotpath(opData, field)] if tx_involves else []

        # Finally, remove any fields specified in the blacklist
        blacklist = getattr(self, "blacklist", None)
        if blacklist:
            for prop in self.blacklist:
                if prop in opData:
                    opData.pop(prop)

        # Set the opData for this operation
        self.opData = opData

        # If this is a virtual_op, we need some sort of unique ID
        if self.opData['transaction_id'] == '0000000000000000000000000000000000000000':
            # Create a repeatable unique identifier for this virtual operation
            opJSON = json.dumps(self.clean_op, sort_keys=True, default=str)
            self.opData['vop_hex_id'] = hashlib.sha1(opJSON.encode('utf-8')).hexdigest()

        # If a custom modify method is specified, run it
        modify = getattr(self, "modify", None)
        if callable(modify):
            self.modify()

        # If a custom modify method is specified, run it
        beforeSave = getattr(self, "beforeSave", None)
        if callable(beforeSave):
            self.beforeSave()


    def query(self):
        query = {
            'block_num': self.opData['block_num'] if 'block_num' in self.opData else None,
            'transaction_id': self.opData['transaction_id'] if 'transaction_id' in self.opData else None,
        }
        # If this is a virtual_op, we need some sort of unique ID
        if self.opData['transaction_id'] == '0000000000000000000000000000000000000000':
            # Remove the normal transaction_id portion of the query
            query.pop('transaction_id', None)
            # Query this field instead
            query['vop_hex_id'] = self.opData['vop_hex_id']
        return query

    def data(self):
        return self.opData.copy()

    def dotpath(self, opData, path):
        try:
            current = opData
            for part in path.split("."):
                try:
                    current = current[int(part)]
                except ValueError:
                    current = current[part]
                    pass
            return current
        except:
            return None
            pass

    def setdotpath(self, opData, path, value):
        nested_set(opData, path.split("."), value)
        return opData

class OperationIndex(Operation):
    def __init__(self, opModel):
        self.opData = { key:opModel[key] for key in ['block_num', 'operation_type', 'transaction_id', 'tx_originator', 'tx_involves' , 'vop_hex_id'] }
