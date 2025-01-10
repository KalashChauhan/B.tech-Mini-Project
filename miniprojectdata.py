import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

# Sample Data
tasks = {'Task 1': ['Activity 1', 'Activity 2', 'Activity 3'],
         'Task 2': ['Activity 1', 'Activity 2', 'Activity 3'],
         'Task 3': ['Activity 1', 'Activity 2', 'Activity 3', 'Activity 4', 'Activity 5']}
start_dates = pd.to_datetime(['2023-03-03', '2023-03-10', '2023-03-17'])
end_dates = pd.to_datetime(['2023-03-14', '2023-03-21', '2023-04-11'])

# Create the Gantt chart
plt.barh(tasks['Task 1'], width=[end-start for start, end in zip(start_dates, end_dates)])
plt.show()