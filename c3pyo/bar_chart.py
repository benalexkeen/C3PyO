import json

from .base import C3Chart
from c3pyo.utils import is_iterable


class BarChart(C3Chart):
    def __init__(self, **kwargs):
        super(BarChart, self).__init__(**kwargs)
        self.bar_ratio = kwargs.get('bar_ratio', 0.8)
        self.data = []
        self.chart_type = 'bar'

    def set_data(self, data):
        if is_iterable(data):
            for i in data:
                self.data.append([i])
        elif isinstance(data, dict):
            keys = sorted([key for key in data])
            for key in keys:
                self.data.append([key, data[key]])
        else:
            raise TypeError("data must be iterable or of type dict")

    def get_data_for_json(self):
        return {
            'columns': self.data,
            'type': self.chart_type
        }

    def get_axis_for_json(self):
        return {
            'x': {
                'type': 'category',
                'categories': [self.x_label],
                'label': self.x_label
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
            'zoom': self.get_zoom_for_json(),
            'subchart': self.get_subchart_for_json(),
            'size': self.get_size_for_json(),
        }
        chart_json = json.dumps(chart_json)
        return chart_json

    def plot(self):
        chart_json = self.get_chart_json()
        self.plot_graph(chart_json)


class MultiBarChart(BarChart):
    def __init__(self, **kwargs):
        super(MultiBarChart, self).__init__(**kwargs)
        self.set_stacked(kwargs)
        self.y_labels = []
        self.x_labels = []

    def set_stacked(self, kwargs):
        self.stacked = kwargs.get('stacked', False)
        msg = 'stacked flag must be a boolean'
        assert isinstance(self.stacked, bool), msg

    def set_data(self, data):
        if isinstance(data, dict):
            y_keys = [key for key in data.keys()]
            y_keys = sorted(y_keys)
            for key in y_keys:
                if not is_iterable(data[key]):
                    msg = "data series must be iterable, received {} of type {}"
                    raise TypeError(msg.format(data[key], type(data[key])))
                data_series = [key]
                data_series.extend(data[key])
                self.data.append(data_series)
                self.y_labels.append(key)
        else:
            msg = "data type must be dict, received {} of type {}"
            raise TypeError(msg.format(data, type(data)))

    def set_x_labels(self, x_labels):
        msg = "x labels must be iterable, received {} of type {}"
        assert is_iterable(x_labels), msg.format(x_labels, type(x_labels))
        self.x_labels = ['x']
        self.x_labels.extend(x_labels)

    def get_data_for_json(self):
        data = {
            'type': 'bar'
        }
        if self.stacked:
            data['groups'] = [self.y_labels]
        if self.x_labels:
            self.data.append(self.x_labels)
            data['x'] = 'x'
        data['columns'] = self.data
        return data

    def get_axis_for_json(self):
        return {'x': {'type': 'category'}}
