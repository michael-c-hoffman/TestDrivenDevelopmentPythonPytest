from uuid import uuid4

import pytest
from moto import mock_dynamodb2

from pynamoMoto.mypynamodb import MyPynamodb


class TestMyPynamodb:
    @staticmethod
    def test_insert():
        with mock_dynamodb2():
            MyPynamodb.create_table()
            entry = MyPynamodb(str(uuid4()))
            entry.save()
            assert MyPynamodb.count() == 1
