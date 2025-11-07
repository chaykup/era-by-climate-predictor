import pandas as pd
import os

base_directory = '/Users/jacobsii/Repos/pitcher-performance-by-climate/etl'
cities_data_path = os.path.join(base_directory, 'archive','cities.csv')
countries_data_path = os.path.join(base_directory, 'archive','countries.csv')
daily_weather_data_path = os.path.join(base_directory, 'archive','daily_weather.parquet')

cities = pd.read_csv(cities_data_path)
countries = pd.read_csv(countries_data_path)
daily_weather = pd.read_parquet(daily_weather_data_path)

pd.set_option('display.max_columns', None)

filtered_columns = ['city_name', 'date', 'avg_temp_c', 'precipitation_mm', 'avg_wind_speed_kmh', 'avg_sea_level_pres_hpa']
filtered_daily_weather = daily_weather[filtered_columns]

filtered_dates = filtered_daily_weather['date'].between('2020-03-01', '2025-10-31')
filtered_daily_weather = filtered_daily_weather[filtered_dates == True]

# print(f"\n {cities.head()} \n")
# print(f"\n {countries.head()} \n")
print(f"\n {filtered_daily_weather.head()} \n")