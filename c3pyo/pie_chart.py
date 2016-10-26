import json
import numbers

from .base import C3Chart
from c3pyo.utils import is_iterable


class PieChart(C3Chart):
    def __init__(self, **kwargs):
        super(PieChart, self).__init__(**kwargs)
        self.data = []
        self.chart_type = 'pie'

    def set_data(self, data):
        if is_iterable(data):
            for idx, value in enumerate(data):
                if isinstance(value, numbers.Number):
                    self.data.append(['y{}'.format(idx+1), value])
                else:
                    msg = 'Expected collection of numbers, received {}'
                    raise TypeError(msg.format(value))
        elif isinstance(data, dict):
            for key in data:
                if isinstance(data[key], numbers.Number):
                    self.data.append([key, data[key]])
                else:
                    msg = 'Expected number, received {} of type {}'
                    raise TypeError(msg.format(data[key], type(key)))
        else:
            raise TypeError("x_data must be a collection or dict, received {}".format(type(data)))

    def get_data_for_json(self):
        return {
            'columns': self.data,
            'type': self.chart_type
            }

    def get_chart_json(self):
        chart_json = {
            'bindto': self.chart_div,
            'data': self.get_data_for_json(),
            'legend': self.get_legend_for_json(),
            'zoom': self.get_zoom_for_json(),
            'size': self.get_size_for_json(),
        }
        chart_json = json.dumps(chart_json)
        return chart_json

    def plot(self):
        chart_json = self.get_chart_json()
        self.plot_graph(chart_json)


class DonutChart(PieChart):
    def __init__(self, **kwargs):
        super(DonutChart, self).__init__(**kwargs)
        self.chart_type = 'donut'
