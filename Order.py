import Supplier

class Order(Supplier.Supplier):
    count_id = 0
    def __init__(self,first_name,last_name,gender,membership,remarks,email,date_joined,address):
        super().__init__(first_name,last_name,gender,membership,remarks)
        Order.count_id += 1
        self.__order_id = Order.count_id
        self.__email = email
        self.__date_joined = date_joined
        self.__address = address

    def get_order_id(self):
        return self.__order_id

    def get_email(self):
        return self.__email

    def get_date_joined(self):
        return self.__date_joined

    def get_address(self):
        return self.__address

    def set_order_id(self,order_id):
        self.__order_id = order_id

    def set_email(self,email):
        self.__email = email

    def set_date_joined(self,date_joined):
        self.__date_joined = date_joined

    def set_address(self,address):
        self.__address = address


