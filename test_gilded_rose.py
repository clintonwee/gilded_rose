# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_aged_brie_before_exp(self):
        items = [Item("Aged Brie", 1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(21, items[0].quality)

    def test_aged_brie_after_exp(self):
        items = [Item("Aged Brie", 1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(23, items[0].quality)

    def test_aged_brie_less_than_50(self):
        items = [Item("Aged Brie", 0, 50), Item("Aged Brie", 2, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()

        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(-2, items[0].sell_in)
        self.assertLessEqual(50, items[0].quality)

        self.assertEqual("Aged Brie", items[1].name)
        self.assertEqual(0, items[1].sell_in)
        self.assertLessEqual(50, items[1].quality)

    def test_boring_carrot_before_exp(self):
        items = [Item("Boring Carrot", 1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual("Boring Carrot", items[0].name)
        self.assertEqual(19, items[0].quality)

    def test_boring_carrot_after_exp(self):
        items = [Item("Boring Carrot", 1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual("Boring Carrot", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(17, items[0].quality)

    def test_boring_carrot_not_negative(self):
        items = [Item("Boring Carrot", 0, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual("Boring Carrot", items[0].name)
        self.assertEqual(-2, items[0].sell_in)
        self.assertLessEqual(0, items[0].quality)

    def test_backstage_passes_before_exp(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 12, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(11, items[0].sell_in)
        self.assertEqual(21, items[0].quality)

    def test_backstage_passes_10_days_before(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(22, items[0].quality)

    def test_backstage_passes_5_days_before(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(23, items[0].quality)

    def test_backstage_passes_after_exp(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_backstage_passes_less_than_50(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 48)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(3, items[0].sell_in)
        self.assertLessEqual(50, items[0].quality)

    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEqual(5, items[0].sell_in)
        self.assertEqual(20, items[0].quality)



if __name__ == '__main__':
    unittest.main()