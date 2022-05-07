import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv('Mobile_Rating.csv')
rating = df['Avg Rating'].tolist()

fig = ff.create_distplot([rating],['Average Rating'])
fig.show()
