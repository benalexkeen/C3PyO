import datetime

# from c3pyo import C3Chart, LineChart, SplineChart, StepChart, BarChart, ScatterChart
import c3pyo as c3
# import pandas as pd

### Line Chart

# chart = c3.LineChart(legend_position='inset', area=True)
#
# dates = [datetime.date(2015, 3, x) for x in [1,2,3,4,5]]
# datetimes = [datetime.datetime(2015, 3, 5, x) for x in [10,11,12,13,14]]

# years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
# gdp = [380.2, 543.3, 1875.9, 2862.5, 5979.6, 10289.7, 14958.3]
# plt = c3.ScatterChart()
# plt.plot(years, gdp, color='green', marker='o', label='gdp for year')
# plt.xlabel("years")
# plt.ylabel("Billions of $")
# plt.gridlines(x=True)
# plt.area(True)
# plt.show()


### Spline Chart

# import datetime
# dts = [datetime.datetime(2015, 3, 5, x) for x in [10, 11, 12, 13, 14]]
# y1 = [10, 20, 30, 20, 10]
# y2 = [20, 10, 30, 40, 0]
#
#
# chart = c3.SplineChart()
# chart.legend_position('inset')
# chart.area(True)
# chart.plot(dts, y1, label="y1")
# chart.plot(dts, y2, label="y2")
# chart.show()



### Bar Chart

# men_height = [175, 176, 172, 172, 177]
# women_height = [156, 162, 158, 160, 164]
#
# chart = c3.BarChart()
# chart.plot(men_height, label='Men_Heights')
# chart.plot(women_height, label='Women_Heights')
# chart.set_xticklabels(('UK', 'USA', 'Japan', 'China', 'Russia'))
# chart.ylabel('Height (cm)')
# chart.show()


### Scatter Chart

# dataset_1 = {'x': [1, 2, 3, 4, 5], 'y': [6, 7, 8, 9, 10]}
# dataset_2 = {'x': [1.5, 2.5, 3.5, 4.5, 5.5], 'y': [5, 6, 7, 8, 9]}
#
#
# chart = c3.ScatterChart()
# chart.plot(dataset_1['x'], dataset_1['y'], label='Dataset1')
# chart.plot(dataset_2['x'], dataset_2['y'], label='Dataset2')
# chart.show()

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