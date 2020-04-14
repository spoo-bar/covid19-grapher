import pandas as pd

"""
locations_url = "https://covid.ourworldindata.org/data/ecdc/locations.csv"
try:
    LocationData = pd.read_csv("locations.csv", index_col=False, usecols=['location', 'continent', 'population'])
except BaseException as err:
    print(f'Downloading {locations_url} failed: {str(err)}')
    exit
"""

LocationData = pd.read_csv("locations.csv", index_col=False, usecols=['location', 'continent', 'population'])
LocationData.drop_duplicates(subset='location', inplace=True)
temp_row = pd.Series({'location':"International", 'continent':None, 'population':None})
temp_df = pd.DataFrame([temp_row])
temp_df2 = pd.concat([LocationData, temp_df], ignore_index=True)
temp_df2.sort_values(by=['location'], inplace=True)
temp_row = pd.Series({'location':"World", 'continent':None, 'population':None})
temp_df = pd.DataFrame([temp_row])
LocationData = pd.concat([temp_df, temp_df2], ignore_index=True)


class LocationClass:        
    #Object class of each country in the locations.csv file
      
    world_population = 0

    def __init__(self, location, continent, population):
        #Object constructor for the class

        self.Name = location
        self.Continent = continent
        try:
            self.Population = int(population)
            LocationClass.world_population += self.Population        
        except:
            self.Population = None
            
    
    def create_attribute(self, label):
        setattr(self, label, {})
        #self.lable["DayCountSinceFirstOccurrence"] =
        #self.lable["DayCount"] =
        #self.lable["SevenDayAvgSinceFirstOccurrence"] =
        #self.lable["SevenDayAvg"] =


class DataClass:
    #Object class for the data elements (DayCount, DayCountSinceFirstOccurrence, SevenDayAvg, SevenDayAvgSinceFirstOccurrence)

    def __init__(self, DayCount):
        self.DayCount = DayCount


object_list = list( LocationClass(row.location, row.continent, row.population) for index, row in LocationData.iterrows())
newCases = pd.read_csv("new_cases.csv", index_col=False)

for index, row in LocationData.iterrows():
    location = row.location
    print(location)
    temp_arr = [r[location] for i, r in newCases.iterrows()]
    daycount = DataClass(temp_arr)

print(vars(daycount))
