# C3PyO
C3PyO is a python wrapper for the data visualisation library C3.js
It will provide a framework for including dynamic graphs in your python web projects.

C3PyO is currently a Work In Progress, to check out the functionality so far, clone this repo then from the root of the repo, run:
`pip install -e .`

Then have a go at some of the commands below

```python
import c3pyo as c3
chart = LineChart()
chart = c3.LineChart()
chart.set_x_data({"x1": [1, 2, 3, 4, 5]})
chart.set_y_data({"y1": [1,2,4,24,48], "y2": [2, 4, 8, 48, 96]})
chart.plot()
```
![LineChart1]
(http://benalexkeen.com/wp-content/uploads/2016/10/linechart1.png)

