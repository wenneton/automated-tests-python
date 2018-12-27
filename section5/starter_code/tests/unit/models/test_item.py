from unittest import TestCase

from models.item import ItemModel

class ItemTest(TestCase):
    def test_create_item(self):
        item = ItemModel('test', 19.99)

        self.assertEqual('test', item.name,
                         "The name of the item does not match")
        self.assertEqual(19.99, item.price,
                         "The price of the item does not match")

    def test_item_json(self):
        item = ItemModel('test', 20.31)
        expected_dict = {'name': 'test',
                         'price': 20.31}

        self.assertDictEqual(expected_dict, item.json(),
                            "The JSON method doesn't match. Received {}, expected {}".format(item.json(),
                                                                                             expected_dict))