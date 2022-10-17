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
print(df.head())

# Test to convert null cells to values
# Prints row 10 in current state
print()
print()
print()
print("HERE IS THE FIRST ROW IN A DOME")
print()
print(df.iloc[19,:])

# Converts the null valuems in column 'temperature' to '0'
df['temperature'] = df['temperature'].fillna(0)

# Prints row 20 with new values, temperatiure should now be 0
print()
print()
print()
print("HERE IS THE FIRST ROW IN A DOME WITHOUT NULL TEMP")
print(df.iloc[19,:])

# creating a list of column names by calling the .columns
list_of_column_names = list(df.columns)

# displaying the list of column names
print()
print("LIST OF COLUMN NAMES:")
print(list_of_column_names)
print()
print()

total_games = 2405
games_with_fgs = df[['season', 'week', 'stadium']].drop_duplicates().shape[0]
games_with_no_fgs = total_games - games_with_fgs

print()
print("There were {} games from 2012-2020.".format(total_games))
print()
print()

#
# # IS ONE OF THESE METHODS BETTER THAN THE OTHER
# 
print()
print("There are", df[['season', 'week', 'stadium']].drop_duplicates().shape[0], "games in our data set.")
print()
print()
print()
print("There are", len(df[['season', 'week', 'stadium']].drop_duplicates()), "games in our data set.")
print()
print()
print()

print("This means there were {} games with no field goals or field goal attempts.".format(games_with_no_fgs))
print()
print()
print()
print("There were field goal attempts in {} percentage of the games and no field goal attempts in {} percentage of the games.".format(games_with_fgs/total_games, games_with_no_fgs/total_games))
print()
print()
print()

number_of_fg_attempts = df.made.value_counts()
fg_percent = df.made.value_counts(1)
fg_per_game = df.shape[0] / total_games
years = df['season'].unique()
weeks = df['week'].unique()
stadiums = df['stadium'].unique()
kickers = df['kicker'].unique()
teams = df['off'].unique()

#method to print specific data from the data file
def print_df_info(description, variable):
    print()
    print(description + ":")
    print()
    print(variable)
    print()

#print the data
print_df_info("NUMBER OF MADE FIELD GOALS:", number_of_fg_attempts)
print_df_info("PERCENTAGE OF MADE FIELD GOALS:", fg_percent)
print_df_info("NUMBER OF FIELD GOALS PER GAME:", fg_per_game)
print_df_info("Here is a list of years where game data was recorded:", years)
print_df_info("Here is a list of weeks where game data was recorded:", weeks)
print_df_info("Here is a list of Stadiums where games have been played:", stadiums)
print_df_info("Here is a list of Kickers who attempted a field goal:", kickers)

#method to compare fg data within specified criteria ranges
def compare(criteria_to_evaluate, description):
    print()
    print("Number of field goals attempted, ", description, ":", df.query(criteria_to_evaluate).shape[0])
    print("Number of field goals made, ", description, ":", df.query(criteria_to_evaluate + "& made == 1").shape[0])
    print("Number of field goals missed, ", description, ":", df.query(criteria_to_evaluate + "& made == 0").shape[0])
    print("Percentage of field goals made, ", description, ":", (df.query(criteria_to_evaluate + "& made == 1").shape[0] / df.query(criteria_to_evaluate).shape[0]))
    print("Percentage of field goals missed, ", description, ":", (df.query(criteria_to_evaluate + "& made == 0").shape[0] / df.query(criteria_to_evaluate).shape[0]))
    #
    #fg_attempts_per_game_in_search = df.query(criteria_to_evaluate + df[['season', 'week', 'stadium']].drop_duplicates().shape[0]).shape[0]
    #print("Number of field goals attempted per game, ", description, ":", fg_attempts_per_game_in_search)
    #print("Number of expected field goals made per game, ", description, ":", fg_attempts_per_game_in_search * fg_percent)
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

for i in stadiums:
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
for i in kickers:
    compare('kicker == "{}"'.format(i), i)
    #break down by year - fix grammar

for i in teams:
    compare('off == "{}"'.format(i), i)
    #break down by year - fix grammar

#
# add against teams
#

dict_for_years = {}
for i in years:
    dict_for_years["df_year_" + str(i)] = df[(df.season == i)].copy()
locals().update(dict_for_years)

print(df_year_2012)
print(df_year_2016)
print(dict_for_years)

for y in years:
    dict_for_years["df_year_" + str(y)]
    for k in kickers:
        compare('kicker == "{}"'.format(k), k)


#df_kicker_by_year = df[["season", "kicker"]].copy()
#print(df_kicker_by_year.head())