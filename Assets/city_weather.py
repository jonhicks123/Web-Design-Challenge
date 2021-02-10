import pandas as pd

df = pd.read_csv('Resources/city_weather.csv')

df.to_html('Assets/data.html', index=False)

weather_table = df.to_html()

print(weather_table)