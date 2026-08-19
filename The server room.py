night_shift = {"Alex", "Jordan", "Taylor", "Casey"}
access_server_room = {"Jordan", "Casey", "Morgan", "Riley"}
hardware_expert = {"Taylor", "Riley", "Casey", "Alex",}
management_role = {"Jordan", "Morgan"}
print('1) The suspect was on the NIGHT SHIFT\n2) The suspect has access to the SERVER ROOM\n3) The suspect is a HARDWARE EXPERT\n4) The suspect is NOT in a MANAGEMENT ROLE')
guilty = night_shift & access_server_room & hardware_expert - management_role
print(guilty)
night_shift = {"Alex", "Jordan", "Taylor", "Casey"}
print(len(guilty))
print(guilty <= night_shift)