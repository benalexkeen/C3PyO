import datetime

from c3pyo import C3Chart, LineChart, SplineChart, StepChart, BarChart, ScatterChart

# chart = LineChart(legend_position='inset', area=True)

# dates = [datetime.date(2015, 3, x) for x in [1,2,3,4,5]]
# datetimes = [datetime.datetime(2015, 3, 5, x) for x in [10,11,12,13,14]]

# chart.set_x_data({"x1": datetimes})
# chart.set_y_data({"y1": [1,2,4,24,48], "y2": [2, 4, 8, 48, 96]})
# chart.plot()

### Bar Chart

# chart = BarChart()
# chart.set_data({"a": 5, "b": 10, "c": 15, "d": 20})
# chart.plot()

### Scatter Chart

# chart = ScatterChart()
# chart.set_data(
#         {
#         "Data_1": [[1,2,3,4,5], [6,7,8,9,10]],
#         "Data_2": [[1.5, 2.5, 3.5, 4.5, 5.5], [5,6,7,8,9]]
#         }
#     )
# chart.plot()

chart = ScatterChart()
chart.set_data(
        [[1,2,3,4,5], [6,7,8,9,10], [1.5, 2.5, 3.5, 4.5, 5.5], [5,6,7,8,9]]
    )
chart.plot()
