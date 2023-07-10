import Instrument


class Guitar(Instrument.Insturment):
    def __init__(self, guitar_type, company, price):
        super().__init__(company, price)
        while guitar_type not in ["electric", "classic", "acoustic"]:
            guitar_type = input("Type must be electric, classic, or acoustic: ")
        self.guitar_type = guitar_type

    def get_type(self):
        return self.guitar_type

    def __str__(self):
        return f"Guitar: id: {self.id} | type: {self.guitar_type} | company: {self.company} | price: {self.price}$"
