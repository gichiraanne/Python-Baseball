import pandas as pd
import matplotlib.pyplot as plt
#import games dataframe
from data import games

#select attendance
#attendance = games.loc[:,['year' == 'info','multi3' == 'attendance']]
attendance = games.loc[:, ['year','multi3']]

#change columns
attendance.columns = ['year','attendance']

#convert to numeric
#attendance.loc[:, 'column'] = pd.to_numeric(attendance.loc[:, 'column'])

#plot graph
#attendance.plot(x='year', y='attendance', figsize=(15, 7), kind='bar')

#add labels
#plt.xlabel('Year')
#plt.ylabel('Attendance')

#plt.show()

#draw the mean line
#plt.axhline(attendance['attendance'].mean()): 'Mean', 'dashed', 'green'