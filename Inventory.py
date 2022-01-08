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
            first_name,
            last_name,
            remarks,
            membership,
            gender):
        super().__init__()
        self.__first_name = first_name
        self.__last_name = last_name
        self.__remarks = remarks
        self.__membership = membership
        self.__gender = gender

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_remarks(self, remarks):
        self.__remarks = remarks

    def set_membership(self, membership):
        self.__membership = membership

    def set_gender(self, gender):
        self.__gender = gender

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_remarks(self):
        return self.__remarks

    def get_membership(self):
        return self.__membership

    def get_gender(self):
        return self.__gender


class Order(Inventory):
    def __init__(
            self,
            email,
            date_joined,
            address):
        super().__init__()
        self.__email = email
        self.__date_joined = date_joined
        self.__address = address

    def set_email(self, email):
        self.__email = email

    def set_date_joined(self, date_joined):
        self.__date_joined = date_joined

    def set_address(self, address):
        self.__address = address

    def get_email(self):
        return self.__email

    def get_date_joined(self):
        return self.__date_joined

    def get_address(self):
        return self.__address
