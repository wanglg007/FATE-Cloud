from db.db_models import AutoTest
from entity.types import TestItem
from operation.db_operator import DBOperator


def insert_test_item(auto_test_data, auto_test_list, test_item_type):
    auto_test_data['test_item'] = TestItem.to_str(test_item_type)
    if not auto_test_list:
        DBOperator.create_entity(AutoTest, auto_test_data)