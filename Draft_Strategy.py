from contextlib import nullcontext
import pandas as pd
import os

# read the csv file / import the data
# if it were a direct path, instead of a relative path, 'r' before the path string addresses any special characters in the path, such as '\'
absolute_path = os.path.dirname(__file__)
relative_path = "data/historical_field_goal_data.csv"
full_path = os.path.join(absolute_path, relative_path)

df = pd.read_csv(full_path)

# print a sample of the data
print("HERE IS A SAMPLE OF THE DATA:")
print()
print(df)

# Test to convert null cells to values
# Prints row 10 in current state
print("\n\n\n HERE IS THE FIRST ROW IN A DOME \n", df.iloc[19,:])

# Converts the null valuems in column 'temperature' to '0'
df['temperature'] = df['temperature'].fillna(0)

# Prints row 20 with new values, temperatiure should now be 0
print("\n\n\n HERE IS THE FIRST ROW IN A DOME WITHOUT NULL TEMP \n", df.iloc[19,:])

# creating a list of column names by
# calling the .columns
list_of_column_names = list(df.columns)

# displaying the list of column names

#
# Is it better to put \n in the quote or in a seperate section
#
print("\nLIST OF COLUMN NAMES:", "\n",  list_of_column_names)
print()
print()

#
# # Is len.df better than shape()?
#   
total_games = 2405
games_with_fgs = df[['season', 'week', 'stadium']].drop_duplicates().shape[0]
games_with_no_fgs = total_games - games_with_fgs

print("\nThere were {} games from 2012-2020.".format(total_games))
print()
print()

#
# # IS ONE OF THESE METHODS BETTER THAN THE OTHER
# 
print("\nThere are", df[['season', 'week', 'stadium']].drop_duplicates().shape[0], "games in our data set.")
print()
print()
print("\nThere are", len(df[['season', 'week', 'stadium']].drop_duplicates()), "games in our data set.")
print()
print()

print("\nThis means there were {} games with no field goals or field goal attempts.".format(games_with_no_fgs))
print()
print()
print("\nThere were field goal attempts in {} percentage of the games and no field goal attempts in {} percentage of the games.".format(games_with_fgs/total_games, games_with_no_fgs/total_games))
print()
print()

number_of_fg_attempts = df.made.value_counts()
print("\nNUMBER OF MADE FIELD GOALS:\n", number_of_fg_attempts)

fg_percent = df.made.value_counts(1)
print("\nPERCENTAGE OF MADE FIELD GOALS:\n", fg_percent)

fg_per_game = df.shape[0] / total_games
print("\nNUMBER OF FIELD GOALS PER GAME:", fg_per_game)
print()
print()

Stadiums = df['stadium'].unique()
print("\nHere is a list of Stadiums where games have been played:\n", Stadiums)

Years = df['season'].unique()
print("\nHere is a list of years where game data was recorded:\n", Years)

Weeks = df['week'].unique()
print("\nHere is a list of weeks where game data was recorded:\n", Weeks)


def compare(var1, name):
    print()
    print("Number of field goals attempted in", name, ":", df.query(var1).shape[0])
    print("Number of field goals made in", name, ":", df.query(var1 + "& made == 1").shape[0])
    print("Number of field goals missed in", name, ":", df.query(var1 + "& made == 0").shape[0])
    print("Percentage of field goals made in", name, ":", (df.query(var1 + "& made == 1").shape[0] / df.query(var1).shape[0]))
    print("Percentage of field goals missed in", name, ":", (df.query(var1 + "& made == 0").shape[0] / df.query(var1).shape[0]))
    #
    #print("Number of field goals attempted per game in", name, ":", df[['season', 'week', var1]].drop_duplicates().shape[0])
    #print("Number of expected field goals made per game in", name, ":", df[['season', 'week', var1]].drop_duplicates().shape[0] * fg_percent))
    #
    print()
    print()


compare("temperature == 0", "a dome")
compare("temperature > 0 & temperature < 32", "below freezing temperature")
compare("temperature > 0 & temperature < 55", "the cold (32f-55f)")
compare("temperature > 80", "the heat (over 80f)")
compare("wind_speed < 5", "low win(under 5 mph)")
compare("wind_speed > 5 & wind_speed < 10", "medium wind (5-10 mph)")
compare("wind_speed > 10", "high wind (over 10mph)")
compare("ou < 40", "games with over/under below 40")
compare("ou > 40 & ou < 45", "games with over/under between 40 and 45")
compare("ou > 45 & ou < 50", "games with over/under between 45 and 50")
compare("ou > 50", "games with over under over 50")
compare("ou < 40", "games with over/under below 40")
compare("home == off", "home games")
compare("away == off", "away games")

for i in Stadiums:
    compare('stadium == "{}"'.format(i), i)
    #add home at stadium vs away at stadium

#
# below code is using every stadium, not just stadiums where games were played that week
#

"""
for y in Years:
    for w in Weeks:
        for i in Stadiums:
            print("In {}, week {}, there was a game at {}".format(y, w, i))
"""

# fgs per stadium % and amount
# fgs by team % and amount (yearly)
# fgs by kicker % and amount (yearly)