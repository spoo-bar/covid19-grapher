
import csv
import uuid
import json

places_added = dict()
object_map = dict()

class Location_class:
    """
    Object definition of each country in the locations.csv file
    """
    world_population = 0

    def __init__(self, name, continent):
        """
        Object constructor for the class
        """
        self.name = name
        self.continent = continent
                
    def __repr__ (self):
        """
        Representation of the class object
        """
        return {"Name":self.name,"Continent":self.continent,"Population":self.population}

    def set_population(self, population):
        """
        Set population for countries with same location entry in the file 
        """
        try:
            self.population = int(population)           
        except ValueError:
            self.population = 0
        Location_class.world_population += self.population

    def update_population(self, additional):
        """
        Update population for countries with same location entry in the file 
        """
        try:
            self.population += int(additional)
        except ValueError:
            pass
        else:
            Location_class.world_population += int(additional)


with open ("locations.csv", 'r') as locations_csv:
    csv_reader = csv.reader(locations_csv)
    next(csv_reader)
    for line in csv_reader:
        if (line[1] in places_added.keys()):
            object_map[places_added[line[1]]].update_population(line[4])
        else:
            object_id = str(uuid.uuid4())
            places_added[line[1]] = object_id
            location = Location_class(line[1],line[2])
            location.set_population(line[4])
            object_map[object_id] = location

object_id = str(uuid.uuid4())
places_added["World"] = object_id
location = Location_class("World", None)
location.population = Location_class.world_population
object_map[object_id] = location

for key in object_map.keys():
    print(object_map[key].__repr__())

            

            



