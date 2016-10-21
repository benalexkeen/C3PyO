import json
import datetime

from .base import C3Chart
from c3pyo.utils import is_iterable


class ScatterChart(C3Chart):
    def __init__(self, **kwargs):
        super(ScatterChart, self).__init__(**kwargs)
        self.x_s = {}
        self.data = []
        self.chart_type = 'scatter'

    def set_data(self, data):
        if is_iterable(data):
            msg = "scatterChart data must have an even number of lists, received {}"
            assert len(data) % 2 == 0, msg.format(data)
            msg = "Data must be an iterable of iterables, received {} of type {}"
            for item in data:
                assert is_iterable(item), msg.format(item, type(item))
            for idx, iterable in enumerate(data):
                name_idx = idx // 2
                x_name = "x{}".format(name_idx)
                y_name = "y{}".format(name_idx)
                if idx % 2 == 0:
                    self.x_s[y_name] = x_name
                    data_item = [x_name]
                else:
                    data_item = [y_name]
                data_item.extend(iterable)
                self.data.append(data_item)
        elif isinstance(data, dict):
            for key in data:
                msg = "dict values for scatterChart must be iterable of length 2, received {}"
                assert is_iterable(data[key]), msg.format(data[key])
                assert len(data[key]) == 2, msg.format(data[key])
                x_key = "{}_x".format(key)
                x_data = [x_key]
                y_data = [key]
                x_data.extend(data[key][0])
                y_data.extend(data[key][1])
                self.x_s[key] = x_key
                self.data.append(x_data)
                self.data.append(y_data)
        else:
            raise TypeError("x_data must be iterable or of type dict, received {}".format(type(data)))

        

    def get_data_for_json(self):
        return {
            'xs': self.x_s,
            'columns': self.data,
            'type': self.chart_type
        }

    def get_axis_for_json(self):
        return {
            'x': {
                'label': self.x_label,
                'tick': {
                    'fit': False
                }
            },
            'y': {
                'label': self.y_label
            }
        }

    def get_chart_json(self):
        chart_json = {
            'bindto': self.chart_div,
            'data': self.get_data_for_json(),
            'legend': self.get_legend_for_json(),
            'grid': self.get_grid_for_json(),
            'axis': self.get_axis_for_json(),
        }
        chart_json = json.dumps(chart_json)
        return chart_json

    def plot(self):
        chart_json = self.get_chart_json()
        self.plot_graph(chart_json)