class Inventory:
    count_id = 0

    def __init__(self):
        Inventory.count_id += 1
        self.__id = Inventory.count_id

    def get_id(self):
        return self.__id


class Supplier(Inventory):
    def __init__(
            self,
            supplier_name,
            name,
            phone,
            address,
            email,
            remarks):
        super().__init__()
        self.__supplier_name = supplier_name
        self.__name = name
        self.__phone = phone
        self.__address = address
        self.__email = email
        self.__remarks = remarks


    def set_supplier_name(self, supplier_name):
        self.__supplier_name = supplier_name

    def set_name(self, name):
        self.__name = name

    def set_phone(self, phone):
        self.__phone = phone

    def set_address(self, address):
        self.__address = address

    def set_email(self, email):
        self.__email = email

    def set_remarks(self, remarks):
        self.__remarks = remarks

    def get_supplier_name(self):
        return self.__supplier_name

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_address(self):
        return self.__address

    def get_email(self):
        return self.__email

    def get_remarks(self):
        return self.__remarks

class Order(Inventory):
    def __init__(
            self,
            date,
            purchase_order,
            supplier,
            delivery_date,
            amount):
        super().__init__()
        self.__date = date
        self.__purchase_order = purchase_order
        self.__supplier = supplier
        self.__delivery_date = delivery_date
        self.__order_status = 'Active'
        self.__amount = amount

    def set_date(self, date):
        self.__date = date

    def set_purchase_order(self, purchase_order):
        self.__purchase_order = purchase_order

    def set_supplier(self, supplier):
        self.__supplier = supplier

    def set_delivery_date(self, delivery_date):
        self.__delivery_date = delivery_date

    def set_order_status(self, order_status):
        self.__order_status = order_status

    def set_amount(self, amount):
        self.__amount = amount

    def get_date(self):
        return self.__date

    def get_purchase_order(self):
        return self.__purchase_order

    def get_supplier(self):
        return self.__supplier

    def get_delivery_date(self):
        return self.__delivery_date

    def get_order_status(self):
        return self.__order_status

    def get_amount(self):
        return self.__amount
