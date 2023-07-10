from abc import abstractmethod


class Insturment:
    insturment_id = 1000

    def __init__(self, company, price):
        self.id = self.insturment_id
        self.sold = False
        self.company = company
        self.price = price
        Insturment.insturment_id += 1

    def get_id(self):
        return self.id

    @abstractmethod
    def get_type(self):
        pass

    def __str__(self):
        return "id: {} | company: {} | price: {}$".format(self.id, self.company, self.price)

    def get_sold(self):
        return self.sold

    def set_sold(self):
        self.sold = True
