smokers = {"Avi Ron", "Sara Kim", "Ben Azulay", "Nina Fox"}
ride_bikes = {"Sara Kim", "Tom Green", "Nina Fox"}
ride_motorcycles = {"Avi Ron", "Ben Azulay", "Nina Fox", "Eli Stone"}
likes_skyjump = {"Avi Ron", "Nina Fox", "Dana Wolf"}

Suspects = smokers | ride_bikes ^ ride_motorcycles | likes_skyjump
print('Suspects:', Suspects)
print('Clues:')
print('1) The suspect rides a BIKE or a MOTORCYCLE\n2) The suspect SMOKE\n3) The suspect likes SKYDIVING\n4)The suspect is NOT someone who rides BOTH bike and motorcycle')
print(smokers & likes_skyjump ^ ride_bikes & ride_motorcycles)
