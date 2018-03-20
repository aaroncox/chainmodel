import json

class Block():

    def __init__(self, blockData, pruneTransactions=True):
        # Useful stats for each block
        blockData['tx_count'] = len(blockData['transactions'])
        blockData['op_count'] = sum([len(tx['operations']) for tx in blockData['transactions']])
        # Avoid excess bloat by removing actual transactions + ops
        if pruneTransactions:
            blockData.pop('transactions', None)
        self.blockData = blockData

    def query(self):
        return {
            'block_num': self.blockData['block_num'] if 'block_num' in self.blockData else None
        }

    def data(self):
        return self.blockData.copy()
