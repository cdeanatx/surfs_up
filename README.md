# Surf's Up Analysis

This project is meant to determine the viability of opening a Surf and Ice Cream shop in Oahu.



## Overview of Analysis

The most important aspect of both a surf shop and an ice cream shop's viability is the weather. Therefore, when the two ideas are combined into a single business plan, the importance of the weather is of the utmost importance. The goal of this analysis is to analyze temperature and precipitation trends, thereby determining the viability of this business model and location.



## Results of Analysis

In order to determine the viability of the Surf and Ice Cream shop from a temperature perspective, temperature statistics were calculated for the months of June and December. The tables below will used for the below analysis.

| ![June Stats](https://github.com/cdeanatx/surfs_up/blob/main/Resources/june_temp_stats.png) | ![December Stats](https://github.com/cdeanatx/surfs_up/blob/main/Resources/december_temp_stats.png) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

- The amount of data available (count) for both months gives confidence in the data's ability to provide accurate and insightful analysis. 
- For both June and December, the median and mean temperatures are within a tenth of a degree. This means that the temperatures are uniformly distributed between the max and min temperatures.
- As expected, the temperatures in December are lower overall than those in June. However, the difference is not as large as might be expected. The average temperature of 71 degrees in December is still in the range of "Ice cream and surfing" weather.

## Summary of Analysis

While the results discussed in the section above are promising, there are still several unknowns which should be explored before committing to this business plan. Below are a couple additional queries which could be run for these two months in order to flush out more information to be used in the decision-making process.

1. Query the precipitation values for June and December as captured by the weather station **nearest the proposed location of the shop**.

```
june_prcp = session.query(Measurement.prcp).\
			filter(extract('month', Measurement.date) == 6).\
			filter(Measurement.station == 'USC00519281').all()

december_prcp = session.query(Measurement.prcp).\
			filter(extract('month', Measurement.date) == 12).\
			filter(Measurement.station == 'USC00519281').all()
```

2. Filter the temperature queries to only show those captured by the nearest weather station to the proposed location of the shop – Oahu's a big place!

```
june_temps = session.query(Measurement.tobs).\
			filter(extract('month', Measurement.date) == 6).\
			filter(Measurement.station == 'USC00519281').all()

december_prcp = session.query(Measurement.tobs).\
			filter(extract('month', Measurement.date) == 12).\
			filter(Measurement.station == 'USC00519281').all()
```

