# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.legendary = ['Sulfuras, Hand of Ragnaros']
        self.cheeses = ['Aged Brie']
        self.tickets = ['Backstage passes to a TAFKAL80ETC concert']
        self.conjured = ['Conjured']
        self.maxQuality = 50


    def update_sell_in(self):
        for item in self.items:
            if item.name not in self.legendary:
                item.sell_in -= 1


    def update_quality(self):
        for item in self.items:
            if item.name in self.cheeses:
                if item.quality < self.maxQuality:
                    if item.sell_in <= 0:
                        item.quality += 2
                    else:
                        item.quality += 1

            elif item.name in self.tickets:
                if item.quality < self.maxQuality:
                    if item.sell_in <= 1:
                        item.quality = 0
                    elif item.sell_in <= 5:
                        item.quality += 3
                    elif item.sell_in <= 10:
                        item.quality += 2
                    else:
                        item.quality += 1

            elif item.name in self.legendary:
                continue

            else:
                if item.sell_in > 0:
                    item.quality -= 1
                else:
                    item.quality -= 2




        self.update_sell_in()
            # if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
            #     if item.quality > 0:
            #         if item.name != "Sulfuras, Hand of Ragnaros":
            #             item.quality = item.quality - 1
            # else:
            #     if item.quality < 50:
            #         item.quality = item.quality + 1
            #         if item.name == "Backstage passes to a TAFKAL80ETC concert":
            #             if item.sell_in < 11:
            #                 if item.quality < 50:
            #                     item.quality = item.quality + 1
            #             if item.sell_in < 6:
            #                 if item.quality < 50:
            #                     item.quality = item.quality + 1
            # if item.sell_in < 0:
            #     if item.name != "Aged Brie":
            #         if item.name != "Backstage passes to a TAFKAL80ETC concert":
            #             if item.quality > 0:
            #                 if item.name != "Sulfuras, Hand of Ragnaros":
            #                     item.quality = item.quality - 1
            #         else:
            #             item.quality = item.quality - item.quality
            #     else:
            #         if item.quality < 50:
            #             item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)