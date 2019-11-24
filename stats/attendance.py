import pandas as pd
import matplotlib.pyplot as plt
#import games dataframe
from data import games

#select attendance
attendance = games.loc[(games['type'] == 'info') & (games['multi2'] == 'attendance'),['year','multi3']]

#change columns
attendance.columns = ['year','attendance']

#convert to numeric
attendance.loc[:, 'attendance'] = pd.to_numeric(attendance.loc[:, 'attendance'])

#plot graph
attendance.plot(x='year', y='attendance', figsize=(15, 7), kind='bar')

#add labels
plt.xlabel('Year')
plt.ylabel('Attendance')

#draw the mean line
plt.axhline(y=attendance['attendance'].mean(), label='Mean', linestyle='--', color='green')

plt.show()

