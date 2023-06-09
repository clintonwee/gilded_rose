# -*- coding: utf-8 -*-
from update_quality import *


class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.categories = {
            'legendary': ['Sulfuras, Hand of Ragnaros'],
            'cheeses': ['Aged Brie'],
            'tickets': ['Backstage passes to a TAFKAL80ETC concert'],
            'conjured': ['Conjured']
        }
        self.max_quality = 50
        self.min_quality = 0

    def enforce_min_max_quality(self, item):
        if item.quality < self.min_quality:
            item.quality = self.min_quality

        if item.quality > self.max_quality:
            item.quality = self.max_quality

    def update_sell_in(self):
        for item in self.items:
            if item.name not in self.categories['legendary']:
                item.sell_in -= 1

    def update_quality(self):
        for item in self.items:
            if item.name in self.categories['cheeses']:
                update_quality_cheese(item)

            elif item.name in self.categories['tickets']:
                update_quality_tickets(item)

            elif item.name in self.categories['conjured']:
                update_quality_conjured(item)

            elif item.name in self.categories['legendary']:
                continue

            else:
                update_quality_normal(item)

            self.enforce_min_max_quality(item)

    def next_day(self):
        self.update_sell_in()
        self.update_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)