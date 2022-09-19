from part1.models.item import ItemModel
from part1.tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('test', 19.99)
            self.assertIsNone(ItemModel.find_by_name('test'),
                              f"Found an item with name {item.name}, but expected not to.")
            item.save_to_db()
            self.assertIsNotNone(ItemModel.find_by_name('test'),
                                 f"Did not find an item with name {item.name}.")
            item.delete_from_db()
            self.assertIsNone(ItemModel.find_by_name('test'),
                              f"Found an item with name {item.name} after attempt to delete it.")