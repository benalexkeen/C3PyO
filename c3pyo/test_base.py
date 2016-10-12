from c3pyo import C3Chart

chart = C3Chart()
chart.x_data = [1,2,3,4,6]
chart.y_data = [5, 10, 15, 20, 25]
chart.x_label = 'Hello'
chart.y_label = 'World'
chart.plot()