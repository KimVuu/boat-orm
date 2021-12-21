from boat.utils.dao import DAO
from boat.utils.database import DatabaseManager, Database, Transaction
from boat.utils.dict import FieldDict, FieldDictDecorator
from boat.utils.expression import RawSQL, OuterRef
from boat.utils.field import Field
from boat.utils.fieldset import Q, And, Or, Not
from boat.utils.model import Model
from boat.utils.query import Query
from boat.utils.raw import SqlValue, Raw, Function

config = {
    'mysql': {
        'driver': 'mysql',
        'host': '127.0.0.1',
        'database': 'boat',
        'user': 'root',
        'password': 'password',
    }
}
db: DatabaseManager = DatabaseManager(config)
