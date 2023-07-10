class guitar:
    guitar_id = 1000

    def __init__(self, guitar_type, company, price):
        self.id = self.guitar_id
        self.sold = False
        while guitar_type not in ["electric", "classic", "acoustic"]:
            guitar_type = input("type must be electric, classic or acoustic: ")
        self.guitar_type = guitar_type
        self.company = company
        self.price = price
        guitar.guitar_id += 1

    def get_id(self):
        return self.id

    def get_type(self):
        return self.guitar_type

    def __str__(self):
        return "id: {} | type: {} | company: {} | price: {}$".format(self.id, self.guitar_type, self.company, self.price)

    def get_sold(self):
        return self.sold

    def set_sold(self):
        self.sold = True