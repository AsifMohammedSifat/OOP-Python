# UML (Unified Modeling Language) Diagram:

<img width="953" height="629" alt="image" src="https://github.com/user-attachments/assets/b3b9c6ac-3f11-4ec3-bbc2-9bbe623f9162" />



Code:
```py
from abc import ABC, abstractmethod

# -------------------------
# Item Class
# -------------------------
class Item:
    def __init__(self, name, price, shipping_weight):
        self.name = name
        self.price = price
        self.shipping_weight = shipping_weight

    def get_price_for_quantity(self, qty):
        return self.price * qty

    def get_tax(self):
        return self.price * 0.1  # example tax

    def in_stock(self):
        return True


# -------------------------
# OrderDetail (Line Item)
# -------------------------
class OrderDetail:
    def __init__(self, item: Item, quantity, tax_status="taxable"):
        self.item = item
        self.quantity = quantity
        self.tax_status = tax_status

    def calc_subtotal(self):
        return self.item.get_price_for_quantity(self.quantity)

    def calc_weight(self):
        return self.item.shipping_weight * self.quantity

    def calc_tax(self):
        if self.tax_status == "taxable":
            return self.calc_subtotal() * 0.1
        return 0


# -------------------------
# Order (Composition with OrderDetail)
# -------------------------
class Order:
    def __init__(self, date, status):
        self.date = date
        self.status = status
        self.order_details = []  # composition

    def add_item(self, order_detail: OrderDetail):
        self.order_details.append(order_detail)

    def calc_subtotal(self):
        return sum(od.calc_subtotal() for od in self.order_details)

    def calc_tax(self):
        return sum(od.calc_tax() for od in self.order_details)

    def calc_total(self):
        return self.calc_subtotal() + self.calc_tax()

    def calc_total_weight(self):
        return sum(od.calc_weight() for od in self.order_details)


# -------------------------
# Customer
# -------------------------
class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.orders = []

    def create_order(self, order: Order):
        self.orders.append(order)


# -------------------------
# Payment (Abstract Class)
# -------------------------
class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def authorized(self):
        pass


class Cash(Payment):
    def __init__(self, amount, cash_tendered):
        super().__init__(amount)
        self.cash_tendered = cash_tendered

    def authorized(self):
        return self.cash_tendered >= self.amount


class Check(Payment):
    def __init__(self, amount, bank_id):
        super().__init__(amount)
        self.bank_id = bank_id

    def authorized(self):
        return True  # assume always valid for demo


class Credit(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def authorized(self):
        return len(self.card_number) == 16


# -------------------------
# DEMO SYSTEM (Controller)
# -------------------------
class ShoppingSystem:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def show_order_summary(self, order: Order):
        print("---- ORDER SUMMARY ----")
        print("Subtotal:", order.calc_subtotal())
        print("Tax:", order.calc_tax())
        print("Total:", order.calc_total())
        print("Weight:", order.calc_total_weight())


# -------------------------
# RUNNING THE SYSTEM
# -------------------------
if __name__ == "__main__":

    system = ShoppingSystem()

    # Customer
    customer = Customer("Rahim", "Dhaka")
    system.add_customer(customer)

    # Items
    item1 = Item("Laptop", 1000, 2)
    item2 = Item("Mouse", 50, 0.2)

    # Order
    order = Order("2026-04-27", "processing")

    # OrderDetails (Line Items)
    od1 = OrderDetail(item1, 1)
    od2 = OrderDetail(item2, 2)

    order.add_item(od1)
    order.add_item(od2)

    # Attach order to customer
    customer.create_order(order)

    # Payment
    payment = Credit(order.calc_total(), "1234567812345678")

    print("Payment Authorized:", payment.authorized())

    # Show system output
    system.show_order_summary(order)

```
