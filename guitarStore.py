from guitar import *


class guitarStore:

    def __init__(self):
        self.total_guitars = []
        self.all_guitars = []
        self.num_of_guitars = 0

    def add_new_guitar(self, guitar_to_add):
        if not isinstance(guitar_to_add, guitar):
            print("This is not a guitar!")
            return

        self.total_guitars.append(guitar_to_add)
        self.all_guitars.append(guitar_to_add)
        self.num_of_guitars += 1

    def sell_a_guitar(self, guitar_id):
        if self.num_of_guitars < 5:
            print("Not enough guitars in store, cant sell. ")
            return

        for i in range(len(self.total_guitars)):
            if self.total_guitars[i].get_id() == guitar_id:
                self.total_guitars[i].set_sold()
                self.total_guitars.pop(i)
                self.num_of_guitars -= 1
                print("Guitar {} has succsessfully been sold! ".format(guitar_id))
                return

        print("No guitar was found with the id of {}.".format(guitar_id))

    def show_guitars(self):
        choice = 0
        while choice > 4 or choice < 1:
            choice = int(input("Choose which guitars you want to see:\n"
                               "  1 - electric\n"
                               "  2 - classic\n"
                               "  3 - acoustic\n"
                               "  4 - all\n"))

        if choice == 1:
            electric_guitars = [guitar for guitar in self.total_guitars if guitar.get_type() == "electric"]
            for electric in electric_guitars:
                print(electric)
        elif choice == 2:
            classic_guitars = [guitar for guitar in self.total_guitars if guitar.get_type() == "classic"]
            for classic in classic_guitars:
                print(classic)
        elif choice == 3:
            acoustic_guitars = [guitar for guitar in self.total_guitars if guitar.get_type() == "acoustic"]
            for acoustic in acoustic_guitars:
                print(acoustic)
        else:
            for guitar in self.total_guitars:
                print(guitar)

    def show_all_guitars(self):
        for guitar in self.all_guitars:
            if guitar.get_sold():
                print("{} -> sold".format(guitar))
            else:
                print("{} -> not sold".format(guitar))
        print("total guitars sold: {}".format(len(self.all_guitars) - self.num_of_guitars))
