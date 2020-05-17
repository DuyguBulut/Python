#datacamp introduction to python exercises

#method of sort
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]
# Paste together first and second: full
full = first + second
# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)
##############################################################

# string to experiment with: place
place = "poolhouse"
# Use upper() on place: place_up
place_up = place.upper()
# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
z = place.count('o')
print(z)

###################################################
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Print out the index of the element 20.0
print(areas.index(20.0))
# Print out how often 9.50 appears in areas
print(areas.count(9.50))

######################################################3
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
poolhouse = 24.5
garage_size = 15.45

# Use append twice to add poolhouse and garage size
areas.append(poolhouse)
areas.append(garage_size)
# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()
# Print out areas
print(areas)

##########################################3
# Definition of radius
r = 192500

# Import radians function of math package
from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r*radians(12)

# Print out dist
print(dist)






