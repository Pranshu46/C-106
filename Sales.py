import plotly.express as px
import csv

with open ("IceCreamdata.csv") as csv_File:
    df = csv.DictReader(csv_File)
    fig = px.scatter(df,x="Temperature", y="Ice-cream Sales( ₹ )")
    fig.show()