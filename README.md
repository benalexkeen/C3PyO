# C3PyO
C3PyO is a python wrapper for the data visualisation library C3.js
It will provide a framework for including dynamic graphs in your python web projects.

C3PyO is currently a Work In Progress, to check out the functionality so far, clone this repo then from the root of the repo, run:
`pip install -e .`

Then have a go at some of the commands below (Note that the images shown are static but the graphs are interactive)

### Line Chart

```python
import c3pyo as c3
chart = c3.LineChart()
chart.set_x_data({"x1": [1, 2, 3, 4, 5]})
chart.set_y_data({"y1": [1,2,4,24,48], "y2": [2, 4, 8, 48, 96]})
chart.plot()
```
![LineChart1]
(http://benalexkeen.com/wp-content/uploads/2016/10/linechart1.png)

### Spline Chart

```python
import datetime
import c3pyo as c3
dts = [datetime.datetime(2015, 3, 5, x) for x in [10,11,12,13,14]]
chart = c3.SplineChart(legend_position='inset', area=True)
chart.set_x_data({"x1": dts})
chart.set_y_data({"y1": [10,20,30,20,10], "y2": [20, 10, 30, 40, 0]})
chart.plot()
```

![SplineChart1]
(http://benalexkeen.com/wp-content/uploads/2016/10/splinechart1.png)

### Bar Chart

```python
import c3pyo as c3
chart = c3.BarChart()
chart.set_data({"a": 5, "b": 10, "c": 15, "d": 20})
chart.plot()
```

![BarChart1]
(http://benalexkeen.com/wp-content/uploads/2016/10/barchart1.png)
