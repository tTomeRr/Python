import Instrument


class Piano(Instrument.Insturment):
    def __init__(self, piano_type, company, price):
        super().__init__(company, price)
        while piano_type not in ["3-octaves", "5-octaves", "7-octaves"]:
            piano_type = input("Type must be 3-octaves, 5-octaves or 7-octaves: ")
        self.piano_type = piano_type

    def get_type(self):
        return self.piano_type

    def __str__(self):
        return f"Piano: id: {self.id} | type: {self.piano_type} | company: {self.company} | price: {self.price}$"
