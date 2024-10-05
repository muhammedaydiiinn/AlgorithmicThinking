doors = [False] * 101 # we will pass the index 0

for i in range(1,101):# Loop through doors numbered from 1 to 100
    for  j in range(i,101,i): # Loop through multiples of i
        doors[j] = not doors[j]  # Toggle the state of the door

for i in range(1,101):
    if doors[i] is True:
        print(i, end= ", ")