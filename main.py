from guitar import *
from guitarStore import *

shop = guitarStore()

g1 = guitar("electric", "Yamaha", 1234)
g2 = guitar("acoustic", "Fender", 2500)
g3 = guitar("classic", "Gibson", 5000)
g4 = guitar("electric", "Ibanez", 1800)
g5 = guitar("acoustic", "Taylor", 3000)
g6 = guitar("classic", "Martin", 4000)


shop.add_new_guitar(g1)
shop.add_new_guitar(g2)
shop.add_new_guitar(g3)
shop.add_new_guitar(g4)
shop.add_new_guitar(g5)
shop.add_new_guitar(g6)

shop.sell_a_guitar(1003)
shop.show_guitars()
shop.show_all_guitars()