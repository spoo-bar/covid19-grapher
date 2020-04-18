import pandas as pd
import datetime
import json

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
        #Object constructor for the class Location

        self.Name = location
        self.Continent = continent
        try:
            self.Population = int(population)
            LocationClass.world_population += self.Population        
        except:
            self.Population = None
              
    def AddData(self, CasesData, DeathsData):
        #Function to add the output dataset to the location object

        setattr(self, "Cases", CasesData)
        setattr(self, "Deaths", DeathsData)


def evalData(Count_arr):
   #Function to evaluate the output dataset

    tempDate = datetime.datetime(2019, 12, 31)
    result = dict()
    result["DayCount"] = list()
    result["DayCountSinceFirst"] = list()
    result["SevenDayAvg"] = list()
    result["SevenDayAvgSinceFirst"] = list()
    result["Total"] = list()
    result["TotalSinceFirst"] = list()
    found = False
    for count in Count_arr:
        if not count:
            count = 0.0
        if found:               
            result["DayCountSinceFirst"].append(count)
            result["TotalSinceFirst"].append(sum(result["DayCountSinceFirst"]))
            result["SevenDayAvgSinceFirst"].append(result["TotalSinceFirst"][-1]/7)
        else:
            if count:
                found = True
                result["FirstDate"] = tempDate.strftime('%Y-%m-%dT%H:%M:%S')
                result["DayCountSinceFirst"].append(count)
                result["TotalSinceFirst"].append(sum(result["DayCountSinceFirst"]))
                result["SevenDayAvgSinceFirst"].append(result["TotalSinceFirst"][-1]/7)
        result["DayCount"].append(count)
        result["Total"].append(sum(result["DayCount"]))
        result["SevenDayAvg"].append(result["Total"][-1]/7)
        tempDate += datetime.timedelta(days=1)

    return result
            

object_list = list( LocationClass(row.location, row.continent, row.population) for index, row in LocationData.iterrows())
Cases_csv = pd.read_csv("new_cases.csv", index_col=False)
Cases_csv.fillna(0, inplace=True)
Deaths_csv = pd.read_csv("new_deaths.csv", index_col=False)
Deaths_csv.fillna(0, inplace=True)

output = dict()
output["Source"] = "https://ourworldindata.org/coronavirus-source-data"
output["LastUpdateTime"] = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
output["Data"] = list()
for place in object_list:
    location = place.Name
    Cases_arr = [r[location] for i, r in Cases_csv.iterrows()]
    CasesData = evalData(Cases_arr)
    Deaths_arr = [r[location] for i, r in Deaths_csv.iterrows()]
    DeathsData = evalData(Deaths_arr)
    place.AddData(CasesData, DeathsData)
    output["Data"].append(vars(place))



with open('data.json', 'w') as output_file:
    json.dump(output, output_file)
