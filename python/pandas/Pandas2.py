# missing values

import pandas as pd

dataframe = pd.read_csv('file.csv')
#new_df = dataframe.fillna(0)
new_df = dataframe.fillna({
    'Area':0,
    "Distance":0,
    'Crime Rate':0,
    'Gender' : 'not available',
    'Price': 0
    })

new_df = dataframe.fillna(method='ffill') # previous value, #bfill
new_df = dataframe.interpolate() # mean between front&back. if not exists, nan
new_df = dataframe.dropna(row='all') # all

new_df = dataframe.set_index('Gender')
#gender = new_df.loc['Male','Area']
gender = new_df.loc['Male',['Area','Distance','Crime Rate']]

city = dataframe.groupby('City')
print(city)

maxi = city.max()
zurich = city.get_group('Zurich')
maxi_zurich = zurich.max() # zurich.mean()
desc = zurich.describe()


for city, city_df in city:
    print(city)
    print(city_df)


