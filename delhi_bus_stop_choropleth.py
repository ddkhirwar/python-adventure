#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 17:39:16 2019

@author: imox
"""

import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import matplotlib.pyplot as plt
from geopandas.tools import sjoin

#fp = "/Users/imox/Downloads/Delhi/Districts.shp"

fp = "/Users/imox/Downloads/Delhi_Wards-SHP/Delhi_Wards.shp"
map_df = gpd.read_file(fp)
# map_df.plot()

#m=map_df[map_df.Ward_No=='209']

df = pd.read_csv('log.csv', delimiter=',')
bust_stop_tuples = [tuple(x) for x in df.values]
mapper={}

one_record = bust_stop_tuples[0]

bus_stop_lat_long = [list([elem[3],elem[4]]) for elem in bust_stop_tuples]
bus_stop_lat_long_dict = {}

lat_list = []
long_list = []

for one_bus_stop_lat_long in bus_stop_lat_long:
    lat_list.append(one_bus_stop_lat_long[0])
    long_list.append(one_bus_stop_lat_long[1])
    
bus_stop_lat_long_dict={"lon":long_list,"lat":lat_list}

bus_stop_points = pd.DataFrame(data=bus_stop_lat_long_dict)
bus_stop_points = bus_stop_points[['lon', 'lat']].apply(lambda row:
              Point(row["lon"], row["lat"]), axis=1)

geo_bus_stop = gpd.GeoDataFrame({"geometry": bus_stop_points})
geo_bus_stop.crs = {'init': 'epsg:4326'}

map_df["no_of_stops"]=0

      

# set the range for the choropleth
vmin, vmax = 1, 58
#earlier colorbar was showing small font, using below to increase global font

plt.rcParams.update({'font.size': 40})
fig, ax = plt.subplots(1, figsize=(30,30))
# remove the axis
ax.axis('off')

# add a title
ax.set_title('DTC bus stops in delhi', fontdict={'fontsize': '75', 'fontweight' : '6'})
# create an annotation for the data source
ax.annotate('Source: Open Transit Data | Delhi',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=50, color='#555555')

# Create colorbar as a legend
sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
cbar = fig.colorbar(sm)


pointInPolys = sjoin(geo_bus_stop, map_df, how='left')
for index, row in pointInPolys.iterrows():
    ward = row['Ward_No']
    print(ward)
    if ward in mapper:
        mapper[ward] = mapper[ward]+1
    else:
        mapper[ward] = 1

for index, row in map_df.iterrows():
    ward = row['Ward_No']
    if ward in mapper:
        map_df.at[index, 'no_of_stops'] = mapper[ward]
        
grouped = pointInPolys.groupby('index_right')

print(grouped.groups)
variable = 'no_of_stops'
base = map_df.plot(column=variable, ax=ax, cmap='Blues', alpha=0.6,edgecolor='dodgerblue')

geo_bus_stop.plot(ax=base, color='black', alpha=0, marker="*", markersize=10)

#fig.savefig('testmap.png', dpi=300)

