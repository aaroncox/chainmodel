import datetime

from chainsync import ChainSync
from chainsync.adapters.steem import SteemAdapter

from chainmodel import ChainModel
from chainmodel.models.steem.schema import Schema

# Setup ChainModel + Schema
ChainModel = ChainModel(schema=Schema())

adapter = SteemAdapter(endpoints=['https://api.steemit.com/'])
chainsync = ChainSync(adapter)

for opData in chainsync.get_ops_in_block(block_num=20826984):

	# Display the original opData
	#
	# {
	# 	'voter': 'hrabiamaurycy',
	# 	'author': 'deemarshall',
	# 	'permlink': 'artstorm-contest-15-day-1-theme-today-sunflowers',
	# 	'weight': 10000,
	# 	'block_num': 20826984,
	# 	'operation_type': 'vote',
	# 	'timestamp': '2018-03-20T01:05:06',
	# 	'transaction_id': '39a7ba77b55867249538122f8ae672a2dd829cf5'
	# }

	print("\n----------")
	print("\noriginal opData")
	print(opData)

	# Create the model based on the opData
	model = ChainModel.get(opData)

	# Get the unique query for this model
	#
	# {
	# 	'block_num': 20826984,
	# 	'transaction_id': '39a7ba77b55867249538122f8ae672a2dd829cf5'
	# }

	print("\nunique query for this model")
	print(model.query())

	# Get the data for this model
	#
	# {
	# 	'author': 'deemarshall',
	# 	'block_num': 20826984,
	# 	'operation_type': 'vote',
	# 	'permlink': 'artstorm-contest-15-day-1-theme-today-sunflowers',
	# 	'timestamp': datetime.datetime(2018, 3, 20, 1, 5, 6),
	# 	'transaction_id': '39a7ba77b55867249538122f8ae672a2dd829cf5',
	# 	'tx_involves': ['hrabiamaurycy', 'deemarshall'],
	# 	'tx_originator': 'hrabiamaurycy',
	# 	'voter': 'hrabiamaurycy',
	# 	'weight': 10000
	# }

	print("\ndata to save for this model")
	print(model.data())

	# Get the index information for this model
	index = ChainModel.index(model)

	# Get the unique query for this index
	#
	# {
	# 	'block_num': 20826984,
	# 	'transaction_id': '39a7ba77b55867249538122f8ae672a2dd829cf5'
	# }

	print("\nunique query for this index")
	print(index.query())

	# Get the data for this index
	#
	# {
	# 	'block_num': 20826984,
	# 	'operation_type': 'vote',
	# 	'transaction_id': '39a7ba77b55867249538122f8ae672a2dd829cf5',
	# 	'tx_involves': ['hrabiamaurycy', 'deemarshall'],
	# 	'tx_originator': 'hrabiamaurycy',
	# 	'vop_hex_id': None
	# }

	print("\ndata to save for this index")
	print(index.data())
