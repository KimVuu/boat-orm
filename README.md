# Boat ORM


이 프로젝트는 파이썬 ORM 라이브러리 [orator](https://github.com/sdispater/orator) 에서 영감을 받아 개발하게 되었습니다.

Boat ORM은 orator에 QueryBuilder를 재사용 가능한 코드들로 관리하는 ORM 입니다.


### 사용법
```python
import os

from boat.utils.dao import DAO
from boat.utils.database import DatabaseManager, Database
from boat.utils.model import Model
from boat.utils.query import Query


config = {
    'mysql': {
        'driver': 'mysql',
        'host': os.environ.get('DATABASE_HOST'),
        'database': os.environ.get('DATABASE_DATABASE'),
        'user': os.environ.get('DATABASE_USER'),
        'password': os.environ.get('DATABASE_PASSWORD'),
    }
}
db: DatabaseManager = DatabaseManager(config)


class BoatModel(Model):
    __table_name__ = 'boat'


class BoatDAO(DAO):
    __model__ = BoatModel


it = Query()
database = Database(db)

boat_list = (
    database(
        BoatDAO(
            it.select(
                BoatModel.fields['name'],
            ),
        )
    )
    .get()
    .all()
)
```
