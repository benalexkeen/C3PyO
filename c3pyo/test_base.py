import datetime

# from c3pyo import C3Chart, LineChart, SplineChart, StepChart, BarChart, ScatterChart
import c3pyo as c3
# import pandas as pd

### Line Chart

# chart = c3.LineChart(legend_position='inset', area=True)
#
dates = [datetime.date(2015, 3, x) for x in [1,2,3,4,5]]
datetimes = [datetime.datetime(2015, 3, 5, x) for x in [10,11,12,13,14]]

# chart.set_data([[1, 2, 3, 4, 5], [5, 10, 15, 20, 25]])
# chart.set_data([[1, 2, 3, 4, 5], [5, 10, 15, 20, 25], [3, 6, 9, 12, 15], [10, 20, 30, 40, 50]])
# chart.set_data({
#     'data1': {
#         'x': [1, 2, 3, 4, 5], 
#         'y': [3, 6, 9, 12, 15]
#     },
#     'data2': {
#         'x': [1.5, 2.5, 3.5, 4.5, 5.5], 
#         'y': [5, 10, 15, 20, 25]
#     },
# })
# df = pd.DataFrame([{'a': 1, 'b': 2}, {'a': 2, 'b': 4}, {'a': 3, 'b': 6}, {'a': 4, 'b': 8}])
# df = pd.Series([1,2,3,4,5,6,7,8,100])
# chart.set_data(df)
# chart.plot()

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [380.2, 543.3, 1875.9, 2862.5, 5979.6, 10289.7, 14958.3]
plt = c3.ScatterChart()
plt.plot(years, gdp, color='green', marker='o', label='gdp for year')
plt.xlabel("years")
plt.ylabel("Billions of $")
plt.gridlines(x=True)
plt.area(True)
plt.show()



### Bar Chart

# chart = c3.BarChart()
# chart.set_data({"a": 5, "b": 10, "c": 15, "d": 20})
# chart.plot()

# chart = c3.BarChart()
# data = pd.Series([1, 2, 3, 4, 5, 6, 7])
# chart.set_data(data)
# chart.plot()

# chart = c3.BarChart()
# data = [1, 2, 3, 4, 5, 6, 7]
# chart.set_data(data)
# chart.plot()

# chart = c3.BarChart()
# data = pd.DataFrame([{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 5, 'b': 6}])
# chart.set_data(data)
# chart.plot()

### Scatter Chart

# chart = c3.ScatterChart()
# chart.set_data(
#         {
#         "Dataset_1": [[1,2,3,4,5], [6,7,8,9,10]],
#         "Dataset_2": [[1.5, 2.5, 3.5, 4.5, 5.5], [5,6,7,8,9]]
#         }
#     )
# chart.plot()

# chart = ScatterChart()
# chart.set_data(
        # [[1,2,3,4,5], [6,7,8,9,10], [1.5, 2.5, 3.5, 4.5, 5.5], [5,6,7,8,9]]
    # )
# chart.plot()

### Pie Chart

# chart = c3.PieChart()
# chart.set_data([1, 2, 3, 4, 5])
# chart.plot()

# chart = c3.PieChart()
# chart.set_data({"hello": 1, "world": 2, "foo": 4, "bar": 17})
# chart.plot()

# chart = c3.PieChart()
# chart.set_data(pd.Series([1,2,3,4,5,6,7,8,100]))
# chart.plot()

### Donut Chart

# chart = c3.DonutChart()
# chart.set_data([1, 2, 3, 4, 5])
# chart.plot()

# chart = c3.PieChart()
# chart.set_data({"hello": 1, "world": 2, "foo": 4, "bar": 17})
# chart.plot()

### Multi-bar chart
# stacked_status = False
# chart = c3.MultiBarChart(stacked=stacked_status)
# chart.set_data({"a": [5, 10, 15], "b": [6, 12, 18], "c": [3, 6, 9]})
# chart.set_x_labels(['cat1', 'cat2', 'cat3'])
# chart.plot()