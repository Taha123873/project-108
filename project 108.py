import plotly.figure_factory as ff
import pandas as pd 
import csv
df = pd.read_csv("data.csv")
fig = ff.creat_displot([df["Avg Rating"].tolist()], ["Avg Rating"])
fig.show()