Visualizing Spatial Data
===============

There are no fewer than 556 pesticides approved for use in the United States according to the _Pesticide National Synthesis Project_ (and a staggering 17,000 products containing those pesticides for sale according to the _Center for Disease Control and Prevention_). These chemicals span the alphabet from from 2,4-D and Abamectin to Ziram and Zoxamide. Taken together, over __one billion pounds__ of pesticide active ingredient are used annually in the United States. Let's investigate the spatial distribution of these chemicals across the United States. You can check how much is applied near you!

County-level pesticide application data is available from the [Pesticide National Synthesis Project](https://water.usgs.gov/nawqa/pnsp/usage/maps/county-level/). Download tabular data for 2015 (or multiple years!) and create a set of choropleth maps to show pesticide usage across the United States. Experiment with normalizing the data by land area, population or whatever else you think makes the most sense. Also play with color scales. For bonus points, layer-in additional data to create a more powerful narrative.

First we will need to install `Folium`, a package that let's us leverage the power of JavaScript mapping tools inside python:

`$ conda install folium`

Here is a code snippet to help you get started with `Folium`. (Note this uses sample data; you will need to modify the column names according to your data). Geometry files (`us_counties.json` and `us_states.json`) are provided to expedite the process.

```
import pandas as pd
import folium

unemployment = pd.read_csv('data/US_Unemployment_Oct2012.csv')

m = folium.Map([43,-100], zoom_start=4)

m.choropleth(
    geo_data=open('data/us_states.json').read(),
    data=unemployment,
    columns=['State', 'Unemployment'],
    key_on='feature.id',
    fill_color='YlGn',
    )
m


```

Before you begin mapping, explore the pesticide data and gain familiarity with its structure. What are the rows? What are the columns? What are different ways you can slice and dice the data? Is aggregation required? If so, what makes the most sense?

Now that you understand your tabular (pesticide) data, take a look at the JSON (geometry) data. What is its structure? What are its keys? How will you map rows of the pesticide data to features of the geometry data? Hint: What are `FIPS` codes? You will need to combine the state and county FIPS codes in your pesticide data to make a unique identifier that matches the `feature.id` in the JSON. This is easier than you might think, so if you are doing anything super fancy, stop to re-assess.

Once you can map data to a geometry, you are ready to make a map! Modify the code snippet above to work with your data. Get it running first and then iterate.

Good luck, and remember, google is your friend.
