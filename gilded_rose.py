# -*- coding: utf-8 -*-

def update_quality_normal(item):
    if item.sell_in >= 0:
        item.quality -= 1
    else:
        item.quality -= 2


def update_quality_cheese(item):
    if item.sell_in < 0:
        item.quality += 2
    else:
        item.quality += 1


def update_quality_tickets(item):
    if item.sell_in <= 1:
        item.quality = 0
    elif item.sell_in <= 5:
        item.quality += 3
    elif item.sell_in <= 10:
        item.quality += 2
    else:
        item.quality += 1


class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.legendary = ['Sulfuras, Hand of Ragnaros']
        self.cheeses = ['Aged Brie']
        self.tickets = ['Backstage passes to a TAFKAL80ETC concert']
        self.conjured = ['Conjured']
        self.maxQuality = 50
        self.minQuality = 0

    def enforce_max_min_quality(self, item):
        if item.quality > self.maxQuality:
            item.quality = self.maxQuality

        if item.quality < self.minQuality:
            item.quality = self.minQuality

    def update_sell_in(self):
        for item in self.items:
            if item.name not in self.legendary:
                item.sell_in -= 1

    def update_quality(self):
        for item in self.items:
            if item.name in self.cheeses:
                update_quality_cheese(item)

            elif item.name in self.tickets:
                update_quality_tickets(item)

            elif item.name in self.legendary:
                continue

            else:
                update_quality_normal(item)

            self.enforce_max_min_quality(item)

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