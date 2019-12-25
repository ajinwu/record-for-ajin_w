from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple("Customer", "name fidelity")

class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
    
    def total(self):
        return self.price * self.quantity

class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        if not hasattr(self, "__total"):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total
    
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount
    def __repr__(self):
        fmt = "<{}order total:{:.2f} deu:{:.2f}>"
        return fmt.format(self.customer.name, self.total(), self.due())
    

class Promotion(ABC):
    @abstractmethod
    def discount(self, Order):
        """返回折扣"""

class FidelityPromo(Promotion):
    def discount(self, Order):
        return Order.total() * .05 if Order.customer.fidelity >= 1000 else 0

class BulkItemPromo(Promotion):
    def discount(self, Order):
        discount = 0
        for item in Order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount

class LargeOrderPromo(Promotion):
    def discount(self, Order):
        discount_items = {item.product for item in Order.cart}
        if len(discount_items) >= 10:
            return Order.total() * .07
        return 0


class order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, "__total"):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total
    
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount
    def __repr__(self):
        fmt = "<{}order total:{:.2f} deu:{:.2f}>"
        return fmt.format(self.customer.name, self.total(), self.due())

def fidelityPromo(Order):
    return Order.total() * .05 if Order.customer.fidelity >= 1000 else 0

def bulkItemPromo(Order):
    discount = 0
    for item in Order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

def largeOrderPromo(Order):
    discount_items = {item.product for item in Order.cart}
    if len(discount_items) >= 10:
        return Order.total() * .07
    return 0


promos = [fidelityPromo, bulkItemPromo, largeOrderPromo]
def best_promo(order):
    return max(promo(order) for promo in promos)


joe = Customer("john Doe", 0)
ann = Customer("ann smith", 1100)

cart = [LineItem("banana", 4, .5), LineItem("apple", 10, 1.5), LineItem("watermellon", 5, 5.0)]
# print(Order(joe, cart, FidelityPromo()))
# print(Order(ann, cart, FidelityPromo()))
print(order(ann, cart, best_promo))