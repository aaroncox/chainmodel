# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

from chainmodel import ChainModel
from chainmodel.models.steem.schema import Schema

# pylint: disable=unused-import,unused-variable
def test_import():
    _ = ChainModel(schema=Schema)

if __name__ == "__main__":
    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "SomeTest.testSomething" ).setLevel( logging.DEBUG )
    unittest.main()
