from pynamodb.attributes import UnicodeAttribute
from pynamodb.models import Model


class MyPynamodb(Model):
    class Meta(object):
        table_name = "MyPynamodb"
        read_capacity_units = 5
        write_capacity_units = 5

    uuid = UnicodeAttribute(hash_key=True)
