Environmental Data
===============

There are no fewer than 556 pesticides approved for use in the United States according to the Pesticide National Synthesis Project (and a staggering 17,000 products containing those pesticides for sale according to the Center for Disease Control and Prevention). These chemicals span the alphabet from from 2,4-D and Abamectin to Ziram and Zoxamide. Taken together, over __one billion pounds__ of pesticide active ingredient are used annually in the United States. Let's investigate how much is applied near where you live...

County-level pesticide application data is available from the [Pesticide National Synthesis Project](https://water.usgs.gov/nawqa/pnsp/usage/maps/county-level/). Download data for 2015 (or multiple years!) and create a set of choropleth maps to show pesticide usage across the United States. Experiment with normalizing the data by land area, population or whatever else you think makes the most sense. Also play with color scales. For bonus points, layer-in additional data to create a more powerful narrative.

First we will need to install Folium _(use conda)_, a package that let's us leverage the power of JavaScript mapping tools inside python:

`$ conda install folium`

Here is a code snippet to help you get started. (Note this uses sample data; you may have to clean or augment your data to make it all work).

```
import pandas as pd
import folium

unemployment = pd.read_csv('data/US_Unemployment_Oct2012.csv')

m = folium.Map([43,-100], zoom_start=4)

m.choropleth(
    geo_data=open('data/us-states.json').read(),
    data=unemployment,
    columns=['State', 'Unemployment'],
    key_on='feature.id',
    fill_color='YlGn',
    )
m
```
