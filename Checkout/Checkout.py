from math import floor


class Checkout:
    class Discount:
        def __init__(self, number_of_items, price):
            self.number_of_items = number_of_items
            self.price = price

    def __init__(self):
        self.prices = {}
        self.total = 0
        self.discounts = {}
        self.items = {}

    def add_discount(self, item, number_of_items, price):
        discount = self.Discount(number_of_items, price)
        self.discounts[item] = discount

    def add_item_price(self, item, price):
        self.prices[item] = price

    def add_item(self, item):
        if item not in self.prices:
            raise Exception("Bad item")

        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculate_total(self):
        total = 0
        for item, cnt in self.items.items():
            total = self.calculate_item_total(cnt, item, total)
        return total

    def calculate_item_total(self, cnt, item, total):
        if item in self.discounts:
            discount = self.discounts[item]
            print("\ndiscount.number_of_items object for item is " + str(discount.number_of_items))
            print("\ndiscount.price object for item is " + str(discount.price))
            if cnt >= discount.number_of_items:
                print("\ncnt is " + str(cnt) + " discount.number_of_items is " + str(discount.number_of_items))
                total = self.calculate_item_discounted_total(cnt, discount, item)
            else:
                total += self.prices[item] * cnt
        else:
            total += self.prices[item] * cnt
        return total

    def calculate_item_discounted_total(self, cnt, discount, item):
        number_of_discounts = floor(cnt / discount.number_of_items)
        print("\nnumber_of_discounts is " + str(number_of_discounts))
        total = number_of_discounts * discount.price
        print("total is " + str(total))
        remaining = cnt % discount.number_of_items
        print("remaining is " + str(remaining))
        total += remaining * self.prices[item]
        return total
