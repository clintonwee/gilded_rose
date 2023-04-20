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


def update_quality_conjured(item):
    if item.sell_in >= 0:
        item.quality -= 2
    else:
        item.quality -= 4