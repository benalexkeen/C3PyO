import datetime

# from c3pyo import C3Chart, LineChart, SplineChart, StepChart, BarChart, ScatterChart
import c3pyo as c3

chart = c3.LineChart(legend_position='inset', area=True, zoom=True)

dates = [datetime.date(2015, 3, x) for x in [1,2,3,4,5]]
datetimes = [datetime.datetime(2015, 3, 5, x) for x in [10,11,12,13,14]]

chart.set_x_data({"x1": datetimes})
chart.set_y_data({"y1": [10,20,30,20,10], "y2": [20, 10, 30, 40, 0]})
chart.plot()

### Bar Chart

# chart = BarChart()
# chart.set_data({"a": 5, "b": 10, "c": 15, "d": 20})
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