smokers = {"John Smith", "Maya Levi", "Noam Cohen", "Liam Patel"}
ride_bikes = {"Maya Levi", "Omer Halevi", "Liam Patel"}
ride_motorcycles = {"John Smith", "Noam Cohen", "Rina Gold"}
likes_skyjump = {"John Smith", "Rina Gold", "Dina Bar"}

Suspects = smokers | ride_bikes | ride_motorcycles | likes_skyjump
print('Suspects', Suspects)
print('clues:')
print('1) The suspect SMOKES\n2) The suspect likes SKYDIVING\n3) The suspect rides a BIKE or a MOTORCYCLE')
print(smokers & likes_skyjump | ride_bikes & ride_motorcycles)