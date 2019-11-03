# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
"""This is a docstring."""
# YOUR CODE HERE

#this is like the noun (the class itself)
class LatLon:
    # this is like the attribute below to describe the above class(noun)
    def __init__(self, lat, lon):
        self.lat = lat 
        self.lon = lon

# this overwrites the str (printing the object) and helps to print what we wish. see below:
    def __str__(self):
        # this would be the method, sort of like the verb, which is an action to be carried out. 
        return ', '.join([
        f'{key}: {value}'
        for key, value in self.__dict__.items()])
    lat = int
    lon = int
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon): 
    def __init__(self, lat, lon, name):
        self.name = name
        super(Waypoint, self).__init__(lat, lon)
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
name = str
# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        self.difficulty = difficulty
        self.size = size
        super(Geocache, self).__init__(name, lat, lon)
        
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

# Print it--also make this print more nicely
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
print(geocache)
