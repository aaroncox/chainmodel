from chainmodel import ChainModel
from chainmodel.models.steem.schema import Schema

import unittest

class chainmodelInitTestCase(unittest.TestCase):
    def setUp(self):
        self.chainmodel = ChainModel(schema=Schema())

    def test_init_no_schema_exception(self):
        with self.assertRaises(Exception) as context:
            chainmodel = ChainModel()
        self.assertTrue('valid_schema_required', context.exception)
