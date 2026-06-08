
def calculate_daily_city_rainfall_from_stations(city:str, dataset, s1:str, s2:str, total_stations:int):
    
    city_col = "IMD_"+city

    # NCDEX defined formula for city rainfall calc. (average of the stations)
    dataset[city_col] = (dataset[s1]+dataset[s2])/total_stations

    return dataset

### update the function ###
# city should calculate the total no. of stations based on the no. of columns that are stations.
 # stations start with "IMD_" and then area name. So we can filter columns based on that.