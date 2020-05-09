import pandas as pd
import datetime
import json
import shutil

temp_folder = "data/tmp"
LocationData = pd.read_csv(temp_folder+"/locations.csv", index_col=False, usecols=['location', 'continent', 'population'])
LocationData.drop_duplicates(subset='location', inplace=True)
LocationData.sort_values(by=['location'], inplace=True)
temp_row = pd.Series({'location':"World", 'continent':None, 'population':None})
temp_df = pd.DataFrame([temp_row])
LocationData = pd.concat([temp_df, LocationData], ignore_index=True)
LocationData.fillna("null", inplace = True)


class LocationClass:        
    #Object class of each country in the locations.csv file
      
    world_population = 0

    def __init__(self, location, continent, population):
        #Object constructor for the class Location

        self.Name = location
        if continent == "null":
            self.Continent = None
        else:
            self.Continent = continent
        try:
            self.Population = int(population)
            LocationClass.world_population += self.Population        
        except:
            self.Population = None
              
    def AddData(self, CasesData, DeathsData, FirstCase, FirstDeath, TotalCases, TotalDeaths):
        #Function to add the output dataset to the location object

        setattr(self, "Cases", CasesData)
        setattr(self, "Deaths", DeathsData)
        self.FirstCaseDate = FirstCase
        self.FirstDeathDate = FirstDeath
        self.TotalCases = TotalCases
        self.TotalDeaths = TotalDeaths


def evalData(Count_arr):
   #Function to evaluate the output dataset

    DateCounter = datetime.datetime(2019, 12, 31)
    result = dict()
    result["DayCount"] = list()   
    result["SevenDayAvg"] = list()  
    result["TotalCount"] = list()
    found = False
    for index, count in enumerate(Count_arr):
        if not count:
            count = 0
        if count and not found:               
            found = True
            FirstDate = DateCounter
        result["DayCount"].append(count)
        result["TotalCount"].append(sum(result["DayCount"]))
        CurrentTotal = result["TotalCount"][-1]
        if index < 7:
            result["SevenDayAvg"].append(round(CurrentTotal/7, 3))
        else:
            result["SevenDayAvg"].append(round(sum(Count_arr[index-6:index+1])/7, 3))
        DateCounter += datetime.timedelta(days=1)
    try:
        DayDifference = (FirstDate -  datetime.datetime(2019, 12, 31)).days
        FirstDate_str = FirstDate.strftime('%Y-%m-%dT%H:%M:%S')
    except:
        DayDifference = -1
        FirstDate_str = None
    result["DayCountSinceFirst"] = result["DayCount"][DayDifference : ]
    result["SevenDayAvgSinceFirst"] = result["SevenDayAvg"][DayDifference : ]
    result["TotalCountSinceFirst"] = result["TotalCount"][DayDifference : ]
    return (FirstDate_str, result, CurrentTotal)
            

object_list = list( LocationClass(row.location, row.continent, row.population) for index, row in LocationData.iterrows())
object_list[0].Population = LocationClass.world_population
Cases_csv = pd.read_csv(temp_folder+"/new_cases.csv", index_col=False)
Cases_csv.fillna(0, inplace=True)
Deaths_csv = pd.read_csv(temp_folder+"/new_deaths.csv", index_col=False)
Deaths_csv.fillna(0, inplace=True)

output = dict()
output["Source"] = "https://ourworldindata.org/coronavirus-source-data"
output["LastUpdateTime"] = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
output["Data"] = list()
for place in object_list:
    location = place.Name
    Cases_arr = [r[location] for i, r in Cases_csv.iterrows()]
    FirstCase, CasesData, TotalCases = evalData(Cases_arr)
    Deaths_arr = [r[location] for i, r in Deaths_csv.iterrows()]
    FirstDeath, DeathsData, TotalDeaths = evalData(Deaths_arr)
    place.AddData(CasesData, DeathsData, FirstCase, FirstDeath, TotalCases, TotalDeaths)
    output["Data"].append(vars(place))

with open('src/assets/data.json', 'w') as output_file:
    json.dump(output, output_file)

try:
    shutil.rmtree(temp_folder)
except OSError:
    print (f"CSV File cleanup failed")
    exit(1)
