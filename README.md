# FantasyFootballKickers

## Description
- This project analyze data from the 2015 to 2022 NFL seasons and compares the number of field goal attempts and made field goal percentage when different conitions are applied.  For example, what is the  number of field goal attempts and made field goal percentage per game in freezing temperatures, or in high wind, or in a dome.  The goal is to provide fantasy football players with additonal information to consider when choosing a kicker each week.

## Technologies:

- Python
- SQL
- Jupyter Notebook
- import pandas as pd
- import os
- import csv
- from contextlib import nullcontext
- from matplotlib.cm import get_cmap

## Getting Started:

1. Clone `https://github.com/MJL502/draft_strategy`
2. Make sure you have pandas installed on your machine
3. Make sure you have Jupyter Notebook installed on your machine
4. Make sure the data file has the 'historical_field_goal_data' .csv
5. Open draft_strategy.ipynb

## Features:

- [ ] 1. Reads data in from a csv file (the historical_field_goal_data.csv in the data file)
- [ ] 1. Creates dictionaries (for each year)
- [ ] 2. Uses functions to remove Null values (specifically to remove null values from the temperature column and replace them with a value of 0)
- [ ] 3. Uses custom functions to analye data (an example is the compare_single_criteria function)
- [ ] 4. Uses ____________ to create two graphs (graphs showing the most and least advantagous conditions when predicting field goals)
- [ ] 5. Data is interpreted in the read me file (see Description above and Results below)

## RESULTS:

- The average number of field goal attempts per game is ___, the average percentage of made field goals is ____, and the average number of made field goals per game is _____.  Of the factors we analyed the highest number of expected field goals per game came in __________. The lowest number of expected field goals per game came in ______.


## TODO:

- [ ] Add data analysis for home vs away games
- [ ] Add data analysis for home vs away games at each stadium



## LICENSE:

- None