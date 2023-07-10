from Drums import *
from Guitar import *
from Piano import *


class insturmentStore:

    def __init__(self):
        self.total_instruments = []
        self.all_instruments = []
        self.num_of_instruments = 0

    def add_new_instrument(self, instrument_to_add):

        self.total_instruments.append(instrument_to_add)
        self.all_instruments.append(instrument_to_add)
        self.num_of_instruments += 1

    def sell_an_insturment(self, instrument_id):
        if self.num_of_instruments < 5:
            print("Not enough insturments in store, cant sell. ")
            return

        for i in range(len(self.total_instruments)):
            if self.total_instruments[i].get_id() == instrument_id:
                self.total_instruments[i].set_sold()
                self.total_instruments.pop(i)
                self.total_instruments -= 1
                print("Instrument {} has successfully been sold! ".format(instrument_id))
                return

        print("No instrument was found with the id of {}.".format(instrument_id))

    def show_insruments(self):
        choice = 0
        while choice > 4 or choice < 1:
            choice = int(input("Choose which insturment you want to see:\n"
                               "  1 - guitars\n"
                               "  2 - pianos\n"
                               "  3 - drums\n"
                               "  4 - all\n"))

        if choice == 1:
            guitars = [guitar for guitar in self.total_instruments if isinstance(guitar, Guitar)]
            self.show_guitars(guitars)
        elif choice == 2:
            pianos = [piano for piano in self.total_instruments if isinstance(piano, Piano)]
            self.show_pianos(pianos)
        elif choice == 3:
            drums = [drum for drum in self.total_instruments if isinstance(drum, Drums)]
            self.show_drums(drums)
        else:
            for insturment in self.total_instruments:
                print(insturment)

    def show_guitars(self, total_guitars):
        choice = 0
        while choice > 4 or choice < 1:
            choice = int(input("Choose which guitars you want to see:\n"
                               "  1 - electric\n"
                               "  2 - classic\n"
                               "  3 - acoustic\n"
                               "  4 - all\n"))

        if choice == 1:
            electric_guitars = [guitar for guitar in total_guitars if guitar.get_type() == "electric"]
            for electric in electric_guitars:
                print(electric)
        elif choice == 2:
            classic_guitars = [guitar for guitar in total_guitars if guitar.get_type() == "classic"]
            for classic in classic_guitars:
                print(classic)
        elif choice == 3:
            acoustic_guitars = [guitar for guitar in total_guitars if guitar.get_type() == "acoustic"]
            for acoustic in acoustic_guitars:
                print(acoustic)
        else:
            for guitar in total_guitars:
                print(guitar)

    def show_pianos(self, total_pianos):
        choice = 0
        while choice > 4 or choice < 1:
            choice = int(input("Choose which pianos you want to see:\n"
                               "  1 - 3-octaves\n"
                               "  2 - 5-octaves\n"
                               "  3 - 7-octaves\n"
                               "  4 - all\n"))

        if choice == 1:
            octaves_3 = [piano for piano in total_pianos if piano.get_type() == "3-octaves"]
            for octave in octaves_3:
                print(octave)
        elif choice == 2:
            octaves_5 = [piano for piano in total_pianos if piano.get_type() == "5-octaves"]
            for octave in octaves_5:
                print(octave)
        elif choice == 3:
            octaves_7 = [piano for piano in total_pianos if piano.get_type() == "7-octaves"]
            for octave in octaves_7:
                print(octave)
        else:
            for piano in total_pianos:
                print(piano)

    def show_drums(self, total_drums):
        choice = 0
        while choice > 4 or choice < 1:
            choice = int(input("Choose which drums you want to see:\n"
                               "  1 - 7-piece\n"
                               "  2 - 9-piece\n"
                               "  3 - 11-piece\n"
                               "  4 - all\n"))

        if choice == 1:
            piece_7 = [drum for drum in total_drums if drum.get_type() == "7-piece"]
            for piece7 in piece_7:
                print(piece7)
        elif choice == 2:
            piece_9 = [drum for drum in total_drums if drum.get_type() == "9-piece"]
            for piece9 in piece_9:
                print(piece9)
        elif choice == 3:
            piece_11 = [drum for drum in total_drums if drum.get_type() == "11-piece"]
            for piece11 in piece_11:
                print(piece11)
        else:
            for drum in total_drums:
                print(drum)

    def show_all_instruments(self):
        for instrument in self.all_instruments:
            if instrument.get_sold():
                print("{} -> sold".format(instrument))
            else:
                print("{} -> not sold".format(instrument))
        print("total Instruments sold: {}".format(len(self.all_instruments) - self.num_of_instruments))
