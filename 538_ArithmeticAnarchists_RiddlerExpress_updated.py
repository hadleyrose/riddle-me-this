# for next 100 years
# activity occurs whenever year = month * date
# 1) how many attacks between 01/2001 and 12/2099?
# 2) which year has most activity?
# 3) which year has least activity?
# 4) what is longest gap between attacks?

import pandas as pd
import datetime
beginning = datetime.date(2001, 1, 1)
end = datetime.date(2099, 12, 31)
date_range = pd.date_range(beginning, end).to_list()
years = [year for year in range(2001, 2100)]
activity_dict_by_yr = dict()
activity_list = list()


for year in years:
    activity_dict_by_yr[year] = 0
for date in date_range:
    specific_year = int(date.year)
    if (date.month * date.day) == (specific_year % 100): # % 100 returns last two digits
        activity_dict_by_yr[specific_year] += 1
        activity_list.append(date)


number_of_activities = sum(activity_dict_by_yr.values())

most_active = [key for key, value in activity_dict_by_yr.items() if value == max(activity_dict_by_yr.values())]

least_active = [key for key, value in activity_dict_by_yr.items() if value == min(activity_dict_by_yr.values())]


delta = 0
longest_gap = 0
index_of_gap_date = 0
longest_gap = max([(activity_list[i+1] - activity_list[i]) for i in range(0, len(activity_list) - 1)])
for i in range(0, len(activity_list) - 1):
    delta = (activity_list[i+1] - activity_list[i])
    index_of_gap_date = i
    if delta > longest_gap:
        longest_gap = delta

print(f'The total number of activities is: {number_of_activities}')
print(f' The most active year is {"".join([str(year) for year in most_active])} with {max(activity_dict_by_yr.values())} attacks.')
print(f'The least active year is {", ".join([str(year) for year in least_active])} with {min(activity_dict_by_yr.values())}.')
print(f'The longest gap is {longest_gap}, and it occurs between {activity_list[index_of_gap_date]} and {activity_list[index_of_gap_date + 1]}.')
