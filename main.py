import csv
import pandas as pd
import plotly.express as px
import math

with open('data.csv') as f:
    reader = csv.reader(f)
    file_data = list(reader)
data = file_data[0]
total=0
length=len(data)
for i in data:
    total+=int(i)
mean = total/length
squared_list = []
for t in data:
    a = int(t) - mean
    a=a**2
    squared_list.append(a)
sum = 0
for x in squared_list:
    sum = sum+x
div = sum/length
sr = math.sqrt(div)
print(sr)