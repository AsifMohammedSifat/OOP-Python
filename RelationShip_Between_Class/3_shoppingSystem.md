```py
from abc import ABC, abstractmethod

# ================= CUSTOMER =================
class Customer:
    def __init__(self, cust_id: int, name: str, address: str):
        self.cust_id = cust_id
        self.name = name
        self.address = address
        self.orders = []  # Association: Customer has Orders

    def add_order(self, order):
        self.orders.append(order)

    def __str__(self):
        return f"Customer({self.cust_id}, {self.name})"


# ================= ITEM =================
class Item:
    def __init__(self, name: str, price: float, shipping_weight: float, stock: int = 0):
        self.name = name
        self.price = price
        self.shipping_weight = shipping_weight
        self.stock = stock

    def get_price_for_quantity(self, qty: int):
        return self.price * qty

    def get_tax(self, qty: int):
        return self.get_price_for_quantity(qty) * 0.1

    def in_stock(self, qty: int):
        return self.stock >= qty

    def reduce_stock(self, qty: int):
        if self.in_stock(qty):
            self.stock -= qty
        else:
            raise ValueError("Not enough stock")

    def __str__(self):
        return f"Item({self.name}, price={self.price})"


# ================= ORDER DETAIL =================
class OrderDetail:
    def __init__(self, item: Item, quantity: int, tax_status: str = "standard"):
        self.item = item
        self.quantity = quantity
        self.tax_status = tax_status

    def calc_sub_total(self):
        return self.item.get_price_for_quantity(self.quantity)

    def calc_tax(self):
        if self.tax_status == "exempt":
            return 0
        return self.item.get_tax(self.quantity)

    def calc_weight(self):
        return self.item.shipping_weight * self.quantity

    def __str__(self):
        return f"OrderDetail({self.item.name}, qty={self.quantity})"


# ================= ORDER =================
class Order:
    def __init__(self, order_id: int, customer: Customer):
        self.order_id = order_id
        self.customer = customer
        self.date = None
        self.status = "pending"
        self.order_details = []  # Aggregation: Order has OrderDetails
        self.payments = []

        customer.add_order(self)

    def add_item(self, item: Item, qty: int):
        if item.in_stock(qty):
            item.reduce_stock(qty)
            detail = OrderDetail(item, qty)
            self.order_details.append(detail)
        else:
            raise ValueError("Item not in stock")

    def calc_sub_total(self):
        return sum(d.calc_sub_total() for d in self.order_details)

    def calc_tax(self):
        return sum(d.calc_tax() for d in self.order_details)

    def calc_total(self):
        return self.calc_sub_total() + self.calc_tax()

    def calc_total_weight(self):
        return sum(d.calc_weight() for d in self.order_details)

    def add_payment(self, payment):
        self.payments.append(payment)

    def __str__(self):
        return f"Order({self.order_id}, status={self.status})"


# ================= PAYMENT (ABSTRACT) =================
class Payment(ABC):
    def __init__(self, amount: float):
        self.amount = amount

    @abstractmethod
    def authorized(self):
        pass


# ================= CASH =================
class Cash(Payment):
    def __init__(self, amount: float, cash_tendered: float):
        super().__init__(amount)
        self.cash_tendered = cash_tendered

    def authorized(self):
        return self.cash_tendered >= self.amount


# ================= CHECK =================
class Check(Payment):
    def __init__(self, amount: float, name: str, bank_id: str):
        super().__init__(amount)
        self.name = name
        self.bank_id = bank_id

    def authorized(self):
        return True  # simplified


# ================= CREDIT =================
class Credit(Payment):
    def __init__(self, amount: float, number: str, exp_date: str):
        super().__init__(amount)
        self.number = number
        self.exp_date = exp_date

    def authorized(self):
        return True  # simplified


# ================= DEMO =================
if __name__ == "__main__":
    # Customers
    c1 = Customer(1, "Alice", "Dhaka")

    # Items
    laptop = Item("Laptop", 1000, 2.5, stock=10)
    mouse = Item("Mouse", 50, 0.2, stock=50)

    # Order
    order = Order(101, c1)

    order.add_item(laptop, 1)
    order.add_item(mouse, 2)

    print(order)
    print("Subtotal:", order.calc_sub_total())
    print("Tax:", order.calc_tax())
    print("Total:", order.calc_total())
    print("Weight:", order.calc_total_weight())

    # Payment
    payment = Cash(order.calc_total(), cash_tendered=1200)
    order.add_payment(payment)

    print("Payment Authorized:", payment.authorized())
```
