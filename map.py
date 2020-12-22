import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt

fp = "lpr_000b16a_e.shp"
map_df = gpd.read_file(fp)
# check the GeoDataframe
print(map_df.head())
map_df.plot()


province = pd.read_csv("1710000901-eng.csv", sep=",")
print(province.head())

# join the geodataframe with the csv dataframe
merged = map_df.merge(province, how='left', left_on="PRENAME", right_on="Geography")
merged = merged[['PRENAME', 'geometry', 'Q4 2020']]
print(merged.head())

# set the value column that will be visualised
variable = 'Q4 2020'
# set the range for the choropleth values
vmin, vmax = 0, 50
# create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(9, 5))

# remove the axis
ax.axis('off')
merged.plot(column=variable, cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8')
fig.savefig('map.png', dpi=300)
