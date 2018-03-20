import datetime
from pprint import pprint

from chainmodel import ChainModel
from chainmodel.models.steem.schema import Schema

# Setup ChainModel + Schema
ChainModel = ChainModel(schema=Schema())

opData = {
    'voter': 'hrabiamaurycy',
    'author': 'deemarshall',
    'permlink': 'artstorm-contest-15-day-1-theme-today-sunflowers',
    'weight': 10000,
    'timestamp': "2018-03-20T01-05-06",
    'block_num': 20826984,
    'operation_type': 'vote',
    'transaction_id': '39a7ba77b55867249538122f8ae672a2dd829cf5'
}

model = ChainModel.get(opData)

print("\noriginal opData")
pprint(opData)

print("\nunique id for this model")
pprint(model.query())

print("\ndata to save for this model")
pprint(model.data())

index = ChainModel.index(model)

print("\nunique id for this index")
pprint(index.query())

print("\ndata to save for this index")
pprint(index.data())
