from boat.utils.dao import *
from boat.utils.database import *
from boat.utils.dict import *
from boat.utils.expression import *
from boat.utils.field import *
from boat.utils.fieldset import *
from boat.utils.model import *
from boat.utils.query import *
from boat.utils.raw import *

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
