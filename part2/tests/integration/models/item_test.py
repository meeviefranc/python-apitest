from part2.models.item import ItemModel
from part2.models.store import StoreModel
from part2.tests.integration.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            StoreModel('test').save_to_db() # for postgres this creates the primary key in Store first
            item = ItemModel('test', 19.99, 1)
            self.assertIsNone(ItemModel.find_by_name('test'),
                              "Found an item with name {}, but expected not to.".format(item.name))
            item.save_to_db()
            self.assertIsNotNone(ItemModel.find_by_name('test'))
            item.delete_from_db()
            self.assertIsNone(ItemModel.find_by_name('test'))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test_store')
            item = ItemModel('test', 19.99, 1)
            store.save_to_db()
            item.save_to_db()
            self.assertEqual(item.store.name, 'test_store')
