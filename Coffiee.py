import plotly.express as px
import csv

with open ("CoffieVsSleep.csv") as csv_File:
    df = csv.DictReader(csv_File)
    fig = px.scatter(df,x="Coffee in ml", y="sleep in hours" , color="week")
    fig.show()