from chainmodel import ChainModel
from chainmodel.models.steem.schema import Schema

from chainsync import ChainSync
from chainsync.adapters.steem import SteemAdapter

import unittest

instances_of_ops = {
	'account_create_with_delegation': 10630429,
	'account_create': 160790,
	'account_update': 424299,
	'account_witness_proxy': 298793,
	'account_witness_vote': 123368,
	'author_reward': 2889020,
	'cancel_transfer_from_savings': 5157726,
	'change_recovery_account': 3291975,
	'claim_reward_balance': 10635691,
	'comment_benefactor_reward': 10885060,
	'comment_options': 4010816,
	'comment': 174444,
	'convert': 2889449,
	'curation_reward': 2889020,
	'custom_json': 2022313,
	'custom': 1297952,
	'decline_voting_rights': 15279127,
	'delegate_vesting_shares': 10630195,
	'delete_comment': 2109364,
	'escrow_approve': 9536540,
	'escrow_dispute': 9543384,
	'escrow_release': 9544320,
	'escrow_transfer': 9284729,
	'feed_publish': 416620,
	'fill_convert_request': 3089792,
	'fill_order': 2889051,
	'fill_transfer_from_savings': 5233388,
	'fill_vesting_withdraw': 479660,
	'interest': 2889234,
	'limit_order_cancel': 1643177,
	'limit_order_create': 1643058,
	'limit_order_create2': 11875326,
	'liquidity_reward': 2889600,
	'pow': 1092,
	'pow2': 4105733,
	'producer_reward': 1,
	'recover_account': 3290230,
	'request_account_recovery': 3287913,
	'return_vesting_delegation': 10832926,
	'set_withdraw_vesting_route': 2804517,
	'shutdown_witness': 5137644,
	'transfer_from_savings': 5147607,
	'transfer_to_savings': 5147555,
	'transfer_to_vesting': 28361,
	'transfer': 25502,
	'vote': 176493,
	'withdraw_vesting': 202807,
	'witness_update': 615462,
}

class chainmodelInitTestCase(unittest.TestCase):
	def setUp(self):
		adapter = SteemAdapter(endpoints=['https://api.steemit.com/'])
		self.chainsync = ChainSync(adapter)
		self.chainmodel = ChainModel(schema=Schema())

	def test_entire_schema_live(self):
		classes = self.chainmodel.schema.models['ops']
		for opData in self.chainsync.get_ops_in_blocks(list(instances_of_ops.values())):
			model = self.chainmodel.get(opData)
			opType = opData['operation_type']
			opSubtype = self.chainmodel.getSubtype(opData)
			if opSubtype:
				print("{} - {} {}".format(opData['block_num'], opData['operation_type'], opSubtype, model))
				self.assertIsInstance(model, classes[opSubtype])
			else:
				print("{} - {} {}".format(opData['block_num'], opData['operation_type'], model))
				self.assertIsInstance(model, classes[opData['operation_type']])
