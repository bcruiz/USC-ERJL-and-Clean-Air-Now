# USC ERJL and Clean Air Now

Example code pulling purple air monitor data from https://map.purpleair.com/1/mAQI/a60/p604800/cC0#12.13/34.26411/-118.38894
into a database to then be used for exploratory analysis.

## sqlite

Relational database that is open source, free, and can be stored locally.
https://www.sqlite.org/index.html

## Python

Using python to access Purple Air's API https://api.purpleair.com/. As Python is faster and integrates with sqlite.

  - request Purple Air API access key by emailing: `contact@purpleair.com`
  - explore https://api.purpleair.com/ for parameters and different call methods

## R

Using R for exploratory analysis with time series, calendar, and seasonal trends plotting through `ggplot2`.
R is more sophisticated with graphs allowing more customization and can easily connect with sqlite to access stored data.
