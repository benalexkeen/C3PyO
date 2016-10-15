from c3pyo import C3Chart, lineChart, splineChart, stepChart

chart = stepChart(legend_position='inset', area=True)
chart.set_x_data({"x1": [1,2,4,8,12]})
chart.set_y_data({"y1": [1,2,4,24,48], "y2": [2, 4, 8, 48, 96]})
chart.plot()