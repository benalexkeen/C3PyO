import datetime

from c3pyo import C3Chart, lineChart, splineChart, stepChart

chart = lineChart(legend_position='inset', area=True)

dates = [datetime.date(2015, 3, x) for x in [1,2,3,4,5]]
datetimes = [datetime.datetime(2015, 3, 5, x) for x in [10,11,12,13,14]]

chart.set_x_data({"x1": datetimes})
chart.set_y_data({"y1": [1,2,4,24,48], "y2": [2, 4, 8, 48, 96]})
chart.plot()